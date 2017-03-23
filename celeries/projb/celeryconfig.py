# coding=utf-8
from kombu import Queue

BROKER_URL = 'amqp://localhost'  # RabbitMQ 作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Redis 作为结果存储
CELERY_TASK_SERIALIZER = 'msgpack'
# 任务序列化和反序列化格式为 msgpack, 别忘了安装 msgpack-python
CELERY_RESULT_SERIALIZER = 'json'   # 结果存储序列化格式为 json
CELERY_ACCEPT_CONTENT = ['msgpack', 'json']  # 任务接受格式类型

CELERY_QUEUES = {
    Queue('foo', routing_key='task.#'),
    Queue('feed_task', routing_key='*.feed'),
}
CELERY_DEFAULT_QUEUE = 'foo'

CELERY_DEFAULT_EXCHANGE = 'tasks'

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'

CELERY_DEFAULT_ROUTING_KEY = 'task.foooooo'

CELERY_ROUTES = {
    'projb.tasks.mul': {
        'queue': 'feed_task',
        'routing_key': 'mul.feed',
    },
}
