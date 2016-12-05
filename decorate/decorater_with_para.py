# coding=utf-8

from functools import wraps


def logs(file="info.log"):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kw):
            log = func.__name__ + " was called"
            print(log)
            with open(file, 'a') as f:
                f.write(log + '\n')
        return wrapper
    return decorate


@logs()
def hello():
    print('Hello World!')

hello()


@logs(file='info2.log')
def hello2():
    print('Hello World!')

hello2()
