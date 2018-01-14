from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://tgfywhzj:rGu2ImqiXK0PnjlgaiUcwJc0Arq5vo9-@donkey.rmq.cloudamqp.com/tgfywhzj"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test": "test"}
    client.sendMessage(sentMsg)

    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print("test_basic passed!")

if __name__ == "__main__":
    test_basic()
