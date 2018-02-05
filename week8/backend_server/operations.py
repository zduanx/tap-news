"""operations"""
import os
import sys
import json
import pickle
import redis
import sys
from datetime import datetime

from bson.json_util import dumps
# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), '../common'))
import mongodb_client # pylint: disable=import-error, wrong-import-position
import news_recommendation_service_client
import ENV

from cloudAMQP_client import CloudAMQPClient
LOG_CLICKS_TASK_QUEUE_URL = ENV.LOG_CLICKS_TASK_QUEUE_URL
LOG_CLICKS_TASK_QUEUE_NAME = ENV.LOG_CLICKS_TASK_QUEUE_NAME
queue_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

REDIS_HOST = ENV.REDIS_HOST
REDIS_PORT = ENV.REDIS_PORT
redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

NEWS_TABLE_NAME = ENV.NEWS_TABLE_NAME
NEWS_LIST_BATCH_SIZE = 10
NEWS_LIMIT = 200
USER_NEWS_TIME_OUT_IN_SCONDS = 60

def getOneNews():
    """Get one news"""
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))

def getNewsSummaries(user_id, page_num):
    """Get news summaries"""
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE # not included

    sliced_news = []

    db = mongodb_client.get_db()
    if redis_client.get(user_id) is not None:
        print('>>> from redis: get data for user "%s"' % user_id)
        total_news_digests = pickle.loads(redis_client.get(user_id))
        sliced_news_digests = total_news_digests[begin_index: end_index]
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        print('>>> from mongodb: get data for user "%s"' % user_id)
        # mongodb iterable -> python list
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))
        total_news_digests = [x['digest'] for x in total_news]
        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SCONDS)
        sliced_news = total_news[begin_index: end_index]

    # Get preference for the user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'

    return json.loads(dumps(sliced_news))

def logNewsClickForUser(user_id, news_id):
    """log news click"""
    # message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    # db = mongodb_client.get_db()
    # db[CLICK_LOGS_TABLE_NAME].insert(message)

    #Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    queue_client.sendMessage(message)
