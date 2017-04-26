from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://oomygusi:BI9ObKHcBcHdmxGk6ZaNkkVMJQZ95cC1@clam.rmq.cloudamqp.com/oomygusi"

TEST_QUEUE_NAME = 'cs503_tap_news_scrape_news_task_queue'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test": "demo"}
    client.sendMessage(sentMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()
