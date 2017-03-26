# coding=utf-8
import sys

from kombu import Exchange, Queue, Connection
from kombu.mixins import ConsumerMixin


class Worker(ConsumerMixin):
    logs_exchange = Exchange(name='logs', type="topic", durable=True)

    def __init__(self, connection):
        self.connection = connection

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write('Usage: {} [binding_keys] ...\n'.format(sys.argv[0]))

    def get_consumers(self, Consumer, channel):
        return [Consumer([Queue(binding_key,
                                self.logs_exchange,
                                exclusive=True,
                                routing_key=binding_key)
                          for binding_key in self.binding_keys],
                         callbacks=[self.on_messages])]

    def on_messages(self, body, messages):
        print('Body: {}'.format(body))


URL = 'amqp://localhost'
with Connection(URL) as connection:
    Worker(connection).run()
