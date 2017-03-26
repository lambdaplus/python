# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost"))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] Receive {}".format(body))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)  # 显示声明无消息确认回执

print('[*] Waitting for messages. To exit press Ctrl+C')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
