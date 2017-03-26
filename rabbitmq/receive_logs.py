# coding: utf-8
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
# disconnect consumer the queue is down

queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print("[*] Waitting for logs. To exit press Ctrl+C")


def callback(ch, method, properties, body):
    print("[x] {}".format(body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
