# -*- coding: utf-8 -*-
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write(
        "Usage: {} [info] [warning] [error]\n".format(sys.argv[0]))
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print("[*] Waitting for logs. To exit press Ctrl+C")


def callback(ch, method, properties, body):
    print("[x] {}:{}".format(method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
