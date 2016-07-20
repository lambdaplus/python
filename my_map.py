# -*-coding: utf-8 -*-
from collections import Iterable

def my_map(func, seq):
    if not isinstance(seq, Iterable):
        raise 'seq must be iterable'

    result = []
    for i in seq:
        result.append(func(i))
    return result
