import jsonrpclib
import ENV
URL = "http://" + ENV.TOPIC_MODELING_SERVER_HOST + ":" + str(ENV.TOPIC_MODELING_SERVER_PORT)

client = jsonrpclib.ServerProxy(URL)

def classify(text):
    topic = client.classify(text)
    print("Topic: %s" % str(topic))
    return topic
