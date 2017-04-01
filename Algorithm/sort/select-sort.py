# coding=utf-8
from random import randrange


def select_sort(seq):
    if len(seq) < 2:
        return seq

    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]

    return seq


if __name__ == '__main__':
    seq = [randrange(100) for _ in range(10)]
    print(select_sort(seq))
