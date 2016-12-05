# coding=utf-8

from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print("I'm a log ^*^")
        result = func(*args, **kw)
        return result
    return wrapper


@log
def hello():
    print('Hello everybody')

hello()
