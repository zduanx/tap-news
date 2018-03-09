import click_log_processor
import os
import sys

from datetime import datetime

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import ENV
import mongodb_client

PREFERENCE_MODEL_TABLE_NAME = ENV.PREFERENCE_MODEL_TABLE_NAME

NUM_OF_CLASSES = 8

# Start MongoDB before running following tests.
def test_basic():
    db = mongodb_client.get_db()
    db[PREFERENCE_MODEL_TABLE_NAME].delete_many({"userId": "test_user"})

    msg = {"userId": "test_user",
           "newsId": "67f8b39c8954bfb8865505f2cc416a9b",
           "timestamp": str(datetime.utcnow())}

    click_log_processor.handle_message(msg)

    model = db[PREFERENCE_MODEL_TABLE_NAME].find_one({'userId':'test_user'})
    assert model is not None
    assert len(model['preference']) == NUM_OF_CLASSES

    print('test_basic passed!')


if __name__ == "__main__":
    test_basic()
