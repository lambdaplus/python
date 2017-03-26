# coding=utf-8
import sys

from kombu import Connection, Producer, Queue, Exchange

logs_exchange = Exchange('logs', 'topic', durable=True)

URL = 'amqp://localhost'

kombu_learn = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
messages = ''.join(sys.argv[2:]) or "Hello World!"

with Connection(URL) as conn:
    producer = Producer(conn)
    producer.publish(messages, exchange=logs_exchange,
                     routing_key=kombu_learn,
                     serializer='json')
