# -*-coding: utf-8 -*-
from random import randrange


def insert_srot(L):
    if len(L) <= 0:
        return L
    for i in range(1, len(L)):
        tmp = L[i]
        j = i - 1
        while j >= 0 and tmp < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = tmp

    return L

if __name__ == '__main__':
    L = [randrange(100) for _ in range(10)]
    print(L)
    print(insert_srot(L))
