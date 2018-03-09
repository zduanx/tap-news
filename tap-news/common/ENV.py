NEWS_DB_HOST = "localhost"
NEWS_DB_PORT = 27017
NEWS_DB_NAME = "tap-news"
NEWS_TABLE_NAME = "news_fetched"
PREFERENCE_MODEL_TABLE_NAME = "user_preference_model"

NEWS_API_ENDPOINT = "https://newsapi.org/v1/"
NEWS_API_KEY = '2762963b26bc4d66aac801c83c240d6f'

BACKEND_SERVER_HOST = "localhost"
BACKEND_SERVER_PORT = 4040
RECOMMENDATION_SERVER_HOST = "localhost"
RECOMMENDATION_SERVER_PORT = 5050
TOPIC_MODELING_SERVER_HOST = "localhost"
TOPIC_MODELING_SERVER_PORT = 6060

LOG_CLICKS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
