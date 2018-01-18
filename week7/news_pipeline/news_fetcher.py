import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
# sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
# import cnn_news_scraper
from newspaper import Article

from cloudAMQP_client import CloudAMQPClient
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

SLEEP_TIME_IN_SECONDS = 4

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print('message is borken')
        return

    task = msg

    """
    text = None
    if task['source'] == 'cnn':
        print('scraping CNN news')
        text = cnn_news_scraper.extract_news(task['url'])
    else:
        print('News source [%s] is not supported.' % task['source'])
    task['text'] = text
    """

    article = Article(task['url'])
    article.download()
    article.parse()
    task['text'] = article.text

    dedupe_news_queue_client.sendMessage(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
