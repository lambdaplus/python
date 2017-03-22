# coding=utf-8
# 性能更好
from random import randrange


def merge_sort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)

    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:  # 取lft和rgt序列中最大的值
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()              # 反序一下
    return (lft or rgt) + res


if __name__ == '__main__':
    seq = [randrange(100) for _ in range(10)]
    print(merge_sort(seq))
