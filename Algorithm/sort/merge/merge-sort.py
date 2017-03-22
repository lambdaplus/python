# -*-coding: utf-8 -*-
from random import randrange


def merge_sort(L):
    if len(L) < 2:
        return L

    def merge(left, right):
        merged = []

        while left and right:
            merged.append(left.pop(0) if left[0] <= right[0]
                          else right.pop(0))

        return merged + (left or right)

    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)


if __name__ == "__main__":
    L = [randrange(1000) for _ in range(10)]
    print(merge_sort(L))
