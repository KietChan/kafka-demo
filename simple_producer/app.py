import env

from flask import Flask
from kafka_producer_util import KafkaProducerUtil

app = Flask(__name__)

index = 1


@app.route("/kafka/push", methods=['GET'])
def produce_message():
    global index
    message = 'Message ' + str(index)
    index += 1
    topic = env.TOPIC
    KafkaProducerUtil.push_message(topic, message)
    return 'Pushed message <b>{}</b> into topic <b>{}</b>'.format(message, topic)
