import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

NEWS_TABLE_NAME = "news_fetched"

import mongodb_client
import news_topic_modeling_service_client

if __name__ == '__main__':
    db = mongodb_client.get_db()
    cursor = db[NEWS_TABLE_NAME].find({})
    count = 0
    for news in cursor:
        count += 1
        print(count)
        if 'class' not in news:
            print('Populating classes...')
            title = news['title']
            topic = news_topic_modeling_service_client.classify(title)
            news['class'] = topic
            print("new title ->%s<-\nclass ->%s<-" % (title, topic))
            db[NEWS_TABLE_NAME].replace_one({'digest': news['digest']}, news, upsert=True)
