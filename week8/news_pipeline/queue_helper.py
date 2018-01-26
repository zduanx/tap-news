import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

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
