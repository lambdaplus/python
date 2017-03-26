# coding=utf-8
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
messages = ''.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=messages)

print("[x] Send {}:{}".format(routing_key, messages))
connection.close()
