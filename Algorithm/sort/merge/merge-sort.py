# -*-coding: utf-8 -*-
from random import randrange


def merge_sort(L):
    if len(L) < 2:
        return L

    def merge(left, right):
        merged = []

        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

        while left:
            merged.append(left.pop(0))

        while right:
            merged.append(right.pop(0))

        return merged

    mid = int(len(L) / 2)
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)


if __name__ == "__main__":
    L = [randrange(1000) for _ in range(10)]
    print(merge_sort(L))

# Another
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
