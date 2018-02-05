import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
# sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
# import cnn_news_scraper
from newspaper import Article
import ENV
from cloudAMQP_client import CloudAMQPClient
SCRAPE_NEWS_TASK_QUEUE_URL = ENV.SCRAPE_NEWS_TASK_QUEUE_URL
SCRAPE_NEWS_TASK_QUEUE_NAME = ENV.SCRAPE_NEWS_TASK_QUEUE_NAME
DEDUPE_NEWS_TASK_QUEUE_URL = ENV.DEDUPE_NEWS_TASK_QUEUE_URL
DEDUPE_NEWS_TASK_QUEUE_NAME = ENV.DEDUPE_NEWS_TASK_QUEUE_NAME

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

SLEEP_TIME_IN_SECONDS = 2

print(">>> FETCHER: START LAUNCHING...")

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
    print(">>> fetcher: text extracted")
    dedupe_news_queue_client.sendMessage(task)
    print(">>> fetcher: dedupe message sent")

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
        dedupe_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
