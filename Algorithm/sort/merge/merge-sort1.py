# coding: utf-8 -*-
from random import randrange
from heapq import merge
'''

Help on function merge in module heapq:

merge(*iterables, key=None, reverse=False)
    Merge multiple sorted inputs into a single sorted output.

    Similar to sorted(itertools.chain(*iterables)) but returns a generator,
    does not pull the data into memory all at once, and assumes that each of
    the input streams is already sorted (smallest to largest).

    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
    [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

    If *key* is not None, applies a key function to each element to determine
    its sort order.

    >>> list(merge(['dog', 'horse'], ['cat', 'fish', 'kangaroo'], key=len))
    ['dog', 'cat', 'fish', 'horse', 'kangaroo']
'''


def merge_sort(L):
    if len(L) < 2:
        return L

    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return list(merge(left, right))


if __name__ == "__main__":
    L = [randrange(100) for _ in range(10)]
    print(merge_sort(L))
