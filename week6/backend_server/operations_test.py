import operations

def test_getOneNews_basic():
    news = operations.get_one_news()
    print(news)
    assert news is not None
    print("test passed")

if __name__ == "__main__":
    test_getOneNews_basic()
