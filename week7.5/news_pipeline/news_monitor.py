import hashlib
import redis
import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloudAMQP_client import CloudAMQPClient
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3
SLEEP_TIME_IN_SECONDS = 700

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
NEWS_SOURCES = ['cnn', 'abc-news', 'bbc-sport', 'bbc-news', 'the-wall-street-journal', 'the-economist', 'msnbc']

print(">>> MONITOR: START LAUNCHING...")

while True:
    print(">>> MONITOR: start monitor news cycle")
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    number_of_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).hexdigest()

        if redis_client.get(news_digest) is None:
            number_of_news += 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

            cloudAMQP_client.sendMessage(news)

    print("Fetched %d news." %number_of_news)
    print(">>> MONITOR: end monitor news cycle")
    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)
