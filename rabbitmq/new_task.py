# -*- coding: utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
# durable 持久化，即便rabbitMQ挂了也不会丢失信息
messages = ''.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=messages,
                      properties=pika.BasicProperties(
                          delivery_mode=2))
print('[x] Send {}'.format(messages))
connection.close()
