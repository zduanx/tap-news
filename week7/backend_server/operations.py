"""operations"""
import os
import sys
import json
from bson.json_util import dumps
# import utils packages
sys.path.append(os.path.join(os.path.dirname(__file__), '../common'))
import mongodb_client # pylint: disable=import-error, wrong-import-position

NEWS_TABLE_NAME = "news"

def get_one_news():
    """Get one news"""
    db_name = mongodb_client.get_db()
    news = db_name[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))
