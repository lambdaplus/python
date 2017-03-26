# coding=utf-8
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')  # 声明 名为 hello 的 queue

if len(sys.argv) != 1:
    body = sys.argv[1]
else:
    body = "Hello World!"

channel.basic_publish(exchange='',  # 默认交换机
                      routing_key='hello',  # queue 需要指定路由键
                      body=body)

print("[x] Sent {}.".format(body))
connection.close()
