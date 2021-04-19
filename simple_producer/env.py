import os

TOPIC = os.getenv('TOPIC', 'task')
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER', '127.0.0.1:9092')
