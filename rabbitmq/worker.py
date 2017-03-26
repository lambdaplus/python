# coding=utf-8
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print("[*] Waitting for messages. To exit press Ctrl+C")


def callback(ch, method, properties, body):
    print("[x] Received {}".format(body))
    time.sleep(body.count(b'.'))  # 模拟耗时操作
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)  # 负载均衡
channel.basic_consume(callback, queue='task_queue')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
