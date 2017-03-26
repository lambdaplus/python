# coding=utf-8
import sys

from kombu import Exchange, Queue, Connection, Consumer
from kombu.async import Hub


logs_exchange = Exchange(name='logs', type="topic", durable=True)

URL = 'amqp://localhost'
hub = Hub()

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: {} [binding_keys]...\n".format(sys.argv[0]))
    sys.exit()

tasks_queues = [Queue(binding_key,
                      logs_exchange,
                      exclusive=True,
                      routing_key=binding_key)
                for binding_key in binding_keys]

print("[*] Waitting for logs. To exit press Ctrl+C")


def on_messages(body, messages):
    print("""
        Body: {0}
        Properties: {1}
        DeliveryInfo: {2}
        """.format(body, messages.properties, messages.delivery_info)
          )

with Connection(URL) as conn:
    conn.register_with_event_loop(hub)
    with Consumer(conn, tasks_queues, callbacks=[on_messages]):
        try:
            hub.run_forever()
        except KeyboardInterrupt:
            exit()
