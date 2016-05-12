# coding=utf-8
from random import randrange

def insert_sort(L):
    if len(L) < 2:
        return L
    for i in range(1, len(L)):
        tmp = L[i]
        j = i - 1
        while j >= 0 and L[j] > tmp:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = tmp

    return L

#if __name__ == '__main__':
#    L = [randrange(1000) for _ in range(10)]
#    print(insert_sort(L))
