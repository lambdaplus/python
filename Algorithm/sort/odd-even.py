# -*- coding: utf-8 -*-

from random import randrange
from insert_sort import *

def odd_even(seq):
    odd = [i for i in lst if i % 2 != 0]
    even = [i for i in lst if i % 2 == 0]

    return odd + even

if __name__ == "__main__":
    lst = [randrange(100) for _ in range(10)]
    print(odd_even(lst))

def odd_even(seq):
    odd = [i for i in lst if i % 2 != 0]
    odd = insert_sort(odd)

    even = [i for i in lst if i % 2 == 0]
    even = insert_sort(even)

    return odd + even

if __name__ == "__main__":
    lst = [randrange(100) for _ in range(10)]
    print(odd_even(lst))
