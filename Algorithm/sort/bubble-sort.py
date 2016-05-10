# coding=utf-8
from random import randrange


def bubble_sort(L):
    if len(L) < 2:
        return L
    for i in range(len(L)):
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                L[j - 1], L[j] = L[j], L[j - 1]
    return L

if __name__ == '__main__':
    L = [randrange(1000) for _ in range(10)]
    print(bubble_sort(L))
