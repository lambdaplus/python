# coding=utf-8
BROKER_URL = 'amqp://localhost'  # RabbitMQ 作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost' # Redis 作为结果存储
CELERY_TASK_SERIALIZER = 'msgpack'
# 任务序列化和反序列化格式为 msgpack, 别忘了安装 msgpack-python
CELERY_RESULT_SERIALIZER = 'json'   # 结果存储序列化格式为 json
CELERY_ACCEPT_CONTENT = ['msgpack', 'json']  # 任务接受格式类型
