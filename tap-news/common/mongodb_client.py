"""mongo db client"""
from pymongo import MongoClient
import ENV

MONGO_DB_HOST = ENV.NEWS_DB_HOST
MONGO_DB_PORT = ENV.NEWS_DB_PORT

DB_NAME = ENV.NEWS_DB_NAME

CLIENT = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT)

def get_db(db=DB_NAME): # pylint: disable=invalid-name
    """get database"""
    db = CLIENT[db]
    return db
