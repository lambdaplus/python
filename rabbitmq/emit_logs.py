# coding: utf-8
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', type='fanout')
messages = ''.join(sys.argv[1:]) or 'info: Hello World!'

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=messages)

print("[x] Send {}".format(messages))
connection.close()
