""" service backend """
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

import operations
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../common'))
import ENV

SERVER_HOST = ENV.BACKEND_SERVER_HOST
SERVER_PORT = ENV.BACKEND_SERVER_PORT

def add(num1, num2):
    """Test method"""
    print("Add is called with %d and %d" %(num1, num2))
    return num1 + num2

def get_one_news():
    """Get one news"""
    print("get_one_news is called")
    return operations.getOneNews()

def  get_news_summaries_for_user(user_id, page_num):
    print("get_news_summaries_for_user is called with user -> %s and pageNum -> %s" % (user_id, page_num))
    return operations.getNewsSummaries(user_id, page_num)

def  log_news_click_for_user(user_id, news_id):
    print("log_news_click_for_user is called with user -> %s and news_id -> %s" % (user_id, news_id))
    return operations.logNewsClickForUser(user_id, news_id)

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'getOneNews')
RPC_SERVER.register_function(get_news_summaries_for_user, 'getNewsSummariesForUser')
RPC_SERVER.register_function(log_news_click_for_user, 'logNewsClickForUser')

print("Starting RPC server on %s:%d" % (SERVER_HOST, SERVER_PORT))

RPC_SERVER.serve_forever()
