## 翻转列表内的元素
用到list的pop和append方法。

# -*- coding: utf -8 -*-

from random import randrange

def revers(seq, L=None):
    while seq:
        if L is None:
            L = []
        L.append(seq.pop())
    return L

if __name__ == "__main__":
    lst = [randrange(100) for _ in range(10)]
    print('This is original list\n', lst)
    print('This is reversed list\n', revers(lst))
