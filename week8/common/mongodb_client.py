"""mongo db client"""
from pymongo import MongoClient

MONGO_DB_HOST = "localhost"
MONGO_DB_PORT = 27017

DB_NAME = "tap-news"

CLIENT = MongoClient(MONGO_DB_HOST, MONGO_DB_PORT)

def get_db(db=DB_NAME): # pylint: disable=invalid-name
    """get database"""
    db = CLIENT[db]
    return db
