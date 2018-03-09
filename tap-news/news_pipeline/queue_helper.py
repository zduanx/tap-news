import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import ENV
from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = ENV.SCRAPE_NEWS_TASK_QUEUE_URL
SCRAPE_NEWS_TASK_QUEUE_NAME = ENV.SCRAPE_NEWS_TASK_QUEUE_NAME
DEDUPE_NEWS_TASK_QUEUE_URL = ENV.DEDUPE_NEWS_TASK_QUEUE_URL
DEDUPE_NEWS_TASK_QUEUE_NAME = ENV.DEDUPE_NEWS_TASK_QUEUE_NAME

def clearQueue(queue_url, queue_name):
    queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if queue_client is not None:
            msg = queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages in queue %s." % (num_of_messages, queue_name))
                return
            num_of_messages += 1


if __name__ == '__main__':
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
    clearQueue(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
