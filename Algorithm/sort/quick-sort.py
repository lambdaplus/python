# coding=utf-8
import random


def quick_sort(seq):
    if len(seq) < 2:
        return seq

    mid = random.choice(seq)
    small = [x for x in seq if x < mid]
    big = [x for x in seq if x > mid]
    return quick_sort(small) + [mid] + quick_sort(big)


if __name__ == '__main__':
    L = [random.randrange(1000) for _ in range(10)]
    print(quick_sort(L))
