# -*- coding: utf-8 -*-

from collections import Iterable

def my_reduce(func, seq, init=None):
    ```
    参考官网例子('https://docs.python.org/3.5/library/functools.html?highlight=reduce#functools.reduce')
    ```
    if not isinstance(seq, Iterable):
        raise 'The seq must be iterbale'
    
    it = iter(seq)
    if init is None:
        value = next(it)
    else:
        value = init
    
    for i in it:
        value = func(value, i)
    
    return value
