# coding=utf-8
import random

def quick_sort(L):
    if L == []:
        return L
    mid = random.choice(L)
    small = [x for x in L if x < mid]
    big = [x for x in L if x > mid]
    return quick_sort(small) + [mid] + quick_sort(big)

if __name__ == '__main__':
    L = [23, 3, 45, 1, 6, 89, 345, 8, 345]
    print(quick_sort(L))
