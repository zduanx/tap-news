import news_topic_modeling_service_client as client

def test_basic():
    newsTitle = "Pentagon might propose ground troops for Syria"
    topic = client.classify(newsTitle)
    assert topic == "U.S."
    print('test_basic passed!')
    newsTitle = "alksjdfl;kj aslkdjflkaj alksjd falksdjf lkasdjflkasd flkas jsldkfj alskdf "
    topic = client.classify(newsTitle)

    newsTitle = ""
    topic = client.classify(newsTitle)

if __name__ == "__main__":
    test_basic()
