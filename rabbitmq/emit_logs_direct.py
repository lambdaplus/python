# coding=utf-8
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
messages = ''.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange="direct_logs",
                      routing_key=severity,
                      body=messages)
print('[x] Send {}:{}'.format(severity, messages))
connection.close()
