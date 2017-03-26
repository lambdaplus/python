# coding=utf-8
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: {} [binding_keys]...\n".format(sys.argv[0]))
    sys.exit()

for binding_key in binding_keys:
    channel.queue_bind(queue=queue_name,
                       exchange='topic_logs',
                       routing_key=binding_key)

print("[*] Waitting for logs. To exit press Ctrl+C")


def callback(ch, method, properties, body):
    print("[x] {}:{}".format(method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
