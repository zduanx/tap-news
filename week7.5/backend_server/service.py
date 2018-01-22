""" service backend """
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

import operations

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

def add(num1, num2):
    """Test method"""
    print("Add is called with %d and %d" %(num1, num2))
    return num1 + num2

def get_one_news():
    """Get one news"""
    print("get_one_news is called")
    return operations.getOneNews()

def  get_news_summaries_for_user(user_id, page_num):
    print("get_news_summaries_for_user is called with %s and %s" % (user_id, page_num))
    return operations.getNewsSummaries(user_id, page_num)

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'getOneNews')
RPC_SERVER.register_function(get_news_summaries_for_user, 'getNewsSummariesForUser')

print("Starting RPC server on %s:%d" % (SERVER_HOST, SERVER_PORT))

RPC_SERVER.serve_forever()
