import os
import time
from kafka import KafkaConsumer

bootstrap_server = os.getenv('BOOTSTRAP_SERVER', '127.0.0.1:9092')
consumer_group = os.getenv('CONSUMER_GROUP', 'simple_consumer')
topic = os.getenv('TOPIC', 'task')

if __name__ == '__main__':
    print('Consuming topic "{}" with consumer group ID "{}"'.format(topic, consumer_group))
    consumer = KafkaConsumer(topic, group_id=consumer_group)
    for msg in consumer:
        print('Consuming message: ' + msg.value.decode())
        time.sleep(10)
        consumer.commit()
