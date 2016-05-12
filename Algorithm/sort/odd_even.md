对列表内的元素进行排序，奇数在前，偶数在后。如果你高兴的话也可以反过来呀。
使用列表解析式解决！
```python
# -*- coding: utf-8 -*-

from random import randrange

def odd_even(seq):
    odd = [i for i in lst if i % 2 != 0]
    even = [i for i in lst if i % 2 == 0]

    return odd + even

if __name__ == "__main__":
    lst = [randrange(100) for _ in range(10)]
    print(odd_even(lst))
```
什么，你想要奇偶数排好序的。行呀，导入之前自己写的插入排序！走起
```python
from random import randrange
from insert_sort import *

def odd_even(seq):
    odd = [i for i in lst if i % 2 != 0]
    odd = insert_sort(odd)

    even = [i for i in lst if i % 2 == 0]
    even = insert_sort(even)

    return odd + even

if __name__ == "__main__":
    lst = [randrange(100) for _ in range(10)]
    print(odd_even(lst))
```
