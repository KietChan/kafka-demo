import env
from kafka import KafkaProducer


class KafkaProducerUtil:
    producer = KafkaProducer(bootstrap_servers=env.KAFKA_BOOTSTRAP_SERVER)

    @staticmethod
    def push_message(topic, message):
        KafkaProducerUtil.producer.send(topic, message.encode())
