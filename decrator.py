# -*- coding: utf-8 -*-
from time import time
from functools import wraps, reduce


def log(func):

    def wrapper(*args, **kw):
        begin = time()
        print('开始时间是 %s' % begin)
#        print('call %s()' % func.__name__)
        back = func(*args, **kw)
        over = time()
        print('结束时间是 %s' % over)
        result = over - begin
        print('用时 %s' % result)
        return back
    return wrapper


@log
def add_(n):
    return reduce(lambda x: x * x, range(n))

print(add_(10))
