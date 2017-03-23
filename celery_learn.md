# Celery 的简单使用

标签： python celery

---
***代码[在这里](https://github.com/lambdaplus/python/tree/master/celeries)***


Celery 是一个简单、灵活并且可靠的处理大量消息的分发系统。并且是自带电池的，本身提供了维护和操作这个系统的工具。

Celery 专注于实时处理的任务队列，并且支持任务调度。
优点：
1. 简单
2. 高可用
3. 快速
4. 灵活

## Celery 架构

+ Celery Beat: 任务调度器
+ Celery Worker: 消费者
+ Broker: 消息中间件，常用的是 RabbitMQ 和 Redis
+ Producer：任务生产者
+ Result Backend：用于结果保存。

## Celery 序列化



## 一个简单的简单例子
项目目录为
```bash
celeries/proj/
├── celeryconfig.py
├── celery.py
├── __init__.py
└── tasks.py
```
---
主程序 celery.py
```python
from __future__ import absolute_import
from celery import Celery

app = Celery('proj', include=['proj.tasks'],
app.config_from_object('proj.celeryconfig')


if __name__ == "main":
    app.start()
```


任务函数 tasks.py
```python
# coding=utf-8
from __future__ import absolute_import

from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y
```
接下来是 配置文件 celeryconfig.py
```python
# coding=utf-8
BROKER_URL = 'amqp://localhost'  # RabbitMQ 作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Redis 作为结果存储
CELERY_TASK_SERIALIZER = 'msgpack'
# 任务序列化和反序列化格式为 msgpack, 别忘了安装 msgpack-python
CELERY_RESULT_SERIALIZER = 'json'   # 结果存储序列化格式为 json
CELERY_ACCEPT_CONTENT = ['msgpack', 'json']  # 任务接受格式类型
```
因为没有任务调度，所以直接启动消费者就行了。在启动之前，要先去安装 RabbitMQ 和 Redis， 并启动。

现在启动我们的消费者函数, 命令行直接启动：

    > cd celeries
    > celery -A celeries worker -l info

看到下面的提示信息，表示成功启动
```python
  -------------- celery@mouse-pc v4.0.2 (latentcall)
---- **** ----- 
--- * ***  * -- Linux-4.9.15-1-MANJARO-x86_64-with-glibc2.2.5 2017-03-22 21:53:05
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         celeries:0x7f9737da7a58
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     redis://localhost/
- *** --- * --- .> concurrency: 2 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . celeries.tasks.add
  . celeries.tasks.mul
  . celeries.tasks.xsum

[2017-03-22 21:53:06,011: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2017-03-22 21:53:06,034: INFO/MainProcess] mingle: searching for neighbors
[2017-03-22 21:53:07,088: INFO/MainProcess] mingle: all alone
[2017-03-22 21:53:07,115: INFO/MainProcess] celery@mouse-pc ready.
```
打开 IPython 测试一下我们的几个函数。
```python
~ ▶︎︎ ipython
Python 3.6.0 |Anaconda 4.3.1 (64-bit)| (default, Dec 23 2016, 12:22:00) 
Type "copyright", "credits" or "license" for more information.


In [1]: from celeries.tasks import add, mul, xsum

In [2]: add.delay(1, 9)
Out[2]: <AsyncResult: 38022eec-2d3d-4ee0-8c7e-367ef92b5f1f>
In [3]: r = mul.delay(2, 4)

In [4]: r.status
Out[4]: 'SUCCESS'

In [5]: r.result
Out[5]: 8

In [6]: r.successful
Out[6]: <bound method AsyncResult.successful of <AsyncResult: 17af4e48-736d-44c9-a8be-a50a35bbc435>>

In [7]: r.backend
Out[7]: <celery.backends.redis.RedisBackend at 0x7f5aebbbcba8> # 结果存储在 redis 里

```
delay() 是 apply_async() 的快捷方式。你也直接调用 apply_async() ：
```python
In [24]: r = mul.apply_async((2, 4))

In [25]: r.result
Out[25]: 8
```
delay() & apply_async 返回的都是 AsyncResult 实例，可用于查看任务的执行状态，但首先你要配置好 result backend.
此时，在worker终端上可以看到，任务信息和结果
```bash
[2017-03-22 22:05:13,689: INFO/MainProcess] Received task: celeries.tasks.add[38022eec-2d3d-4ee0-8c7e-367ef92b5f1f]  
[2017-03-22 22:05:14,765: INFO/PoolWorker-2] Task celeries.tasks.add[38022eec-2d3d-4ee0-8c7e-367ef92b5f1f] succeeded in 0.007736653999018017s: 10
[2017-03-22 22:08:36,378: INFO/MainProcess] Received task: celeries.tasks.mul[17af4e48-736d-44c9-a8be-a50a35bbc435]  
[2017-03-22 22:08:37,010: INFO/PoolWorker-2] Task celeries.tasks.mul[17af4e48-736d-44c9-a8be-a50a35bbc435] succeeded in 0.011531784999533556s: 8
```
仔细看，每个任务都有一个 task_id。我们可以通过 task_id 获得任务的结果。

取 add 任务的 id：
```bash
task_id = '38022eec-2d3d-4ee0-8c7e-367ef92b5f1f'
In [8]: task_id = '38022eec-2d3d-4ee0-8c7e-367ef92b5f1f'

In [9]: add.AsyncResult(task_id).get()
Out[9]: 10
```
关联任务

    In [2]: m = mul.apply_async((2, 2), link=mul.s(3))
    
在 Worker 终端里会看到两个值，关联之前和之后的。
```
[2017-03-23 13:27:13,045: INFO/MainProcess] Received task: proj.tasks.mul[40492357-44bb-41e4-979f-6eb197107a5b]  
[2017-03-23 13:27:13,731: INFO/PoolWorker-2] Task proj.tasks.mul[40492357-44bb-41e4-979f-6eb197107a5b] succeeded in 0.0023383530005958164s: 4
[2017-03-23 13:27:13,732: INFO/MainProcess] Received task: proj.tasks.mul[b01be1b8-f957-48b2-9d72-8187af6ac161]  
[2017-03-23 13:27:13,734: INFO/PoolWorker-2] Task proj.tasks.mul[b01be1b8-f957-48b2-9d72-8187af6ac161] succeeded in 0.0006868359996587969s: 12
```


## 指定队列
在 celeries 目录下新建一个目录 projb, 代码使用 proj 中的。
```bash
celeries/projb
├── celeryconfig.py
├── celery.py
├── __init__.py
└── tasks.py
```
在 celeryconfig.py 添加些配置：
```
# coding=utf-8
from kombu import Queue

BROKER_URL = 'amqp://localhost'  # RabbitMQ 作为消息代理
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # Redis 作为结果存储
CELERY_TASK_SERIALIZER = 'msgpack'
# 任务序列化和反序列化格式为 msgpack, 别忘了安装 msgpack-python
CELERY_RESULT_SERIALIZER = 'json'   # 结果存储序列化格式为 json
CELERY_ACCEPT_CONTENT = ['msgpack', 'json']  # 任务接受格式类型

CELERY_QUEUES = {
    Queue('foo', routing_key='task.#'), # 路由键以 task. 开头的消息进入此队列
    Queue('feed_task', routing_key='*.feed'), # 路由键以 .feed 结尾的消息进入此队列
}
CELERY_DEFAULT_QUEUE = 'foo' # 默认队列

CELERY_DEFAULT_EXCHANGE = 'tasks' # 默认交换机

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic' # 默认交换机类型 topic

CELERY_DEFAULT_ROUTING_KEY = 'task.foooooooo' # 默认交换机路由键, task. 后的值不影响

CELERY_ROUTES = {
    'projb.tasks.mul': {
        'queue': 'feed_task',  # 消息全都进入 feed_task 队列
        'routing_key': 'mul.feed',
    },
}
```
然后，我们以指定队列的方式启动：

    >  celery -A projb worker -Q foo,feed_task -l info

tasks.py 中的 mul 函数只会通过队列 feed_task 被执行。add 函数通过默认队列 foo 执行。
 ```python
In [84]: from projb.tasks import mul, add

In [85]: r = add.delay(3, 3)

In [86]: r.result
Out[86]: 6

In [87]: res = mul.delay(3, 3)

In [88]: res.result
Out[88]: 9
```
不过，我们可以使用 apply_async() 函数来指定队列。
```python
In [90]: r = add.apply_async((3, 3), queue='feed_task', routing_key='mul.feed')

In [91]: r.result
Out[91]: 6

In [92]: res = mul.apply_async((3, 3), queue='foo', routing_key='task.foooooo')

In [93]: res.result
Out[93]: 9
```

## 任务调度
依法炮制，基于 projb 的代码，创建目录 projc，在 proc/celeryconfig.py 中添加如下配置。
```
CELERYBEAT_SCHEDULE = {
    'mul-every-30-seconds': {
        'task': 'projc.tasks.mul',
        'schedule': 30.0,
        'args': (2, 2),
    }
}
```
执行

    > celery -B -A projc worker -l info

就可以在终端看到每 30s 执行一次任务。
```
[2017-03-23 12:23:13,920: INFO/Beat] Scheduler: Sending due task mul-every-30-seconds (projc.tasks.mul)
[2017-03-23 12:23:13,923: INFO/MainProcess] Received task: projc.tasks.mul[9c414257-d627-4c36-a9d8-9daed7e295c0]  
[2017-03-23 12:23:15,177: INFO/PoolWorker-3] Task projc.tasks.mul[9c414257-d627-4c36-a9d8-9daed7e295c0] succeeded in 0.0010301589991286164s: 4
```

## 任务绑定、日志记录和错误重试

任务绑定、记录日志和重试是 Celery 3 个常用的高级功能。接下来，修改 proj 的 tasks.py 文件。添加一个 div 函数。
```
@app.task(bind=True)
def div(self, x, y):
    logger.info(
        '''
        Executing task : {0.id}
        task.args      : {0.args!r}
        task.kwargs    : {0.kwargs!r}
        '''.format(self.request)
    )
    try:
        res = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=3, max_retries=3)
    else:
        return res
```
在 Ipython 调用：

    In [3]: d = div.delay(2, 1)

在 worker 中可以看到
```
[2017-03-23 14:57:17,361: INFO/PoolWorker-2] proj.tasks.div[68ef1584-16ac-4236-9858-b00842891bbc]: 
        Executing task : 68ef1584-16ac-4236-9858-b00842891bbc
        task.args      : [2, 1]
        task.kwargs    : {}
        
[2017-03-23 14:57:17,369: INFO/PoolWorker-2] Task proj.tasks.div[68ef1584-16ac-4236-9858-b00842891bbc] succeeded in 0.007741746998362942s: 2.0
```
换成可以引起异常的参数：

    In [4]: d = div.delay(2, 0)

可以看到，在 worker 中每 3s 重试一次，总共重复三次(执行了 4 次)，然后抛出异常！