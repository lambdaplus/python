# coding=utf-8
from random import randrange


def bubble_sort(L):
    for m in range(len(L)):
        n = 0
        for n in range(len(L)):
            if L[m] < L[n]:
                L[m],  L[n] = L[n], L[m]
    return L

if __name__ == '__main__':
    L = [randrange(1000) for _ in range(10)]
    print(bubble_sort(L))
