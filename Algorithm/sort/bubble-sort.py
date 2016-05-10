# coding=utf-8
from random import randrange


def bubble_sort(L):
    '''
    冒泡排序主要使用两次循环实现排序。外循环中的一个数字依次与内层循环中的每个数字进行比较，如果索引值小的数字大于索引值大的数字，交换位置。否则，不变。直至循环结束
    '''
    if len(L) < 2: # 列表内元素低于2，直接返回！
        return L
    for i in range(len(L)):
        for j in range(1, len(L)):
            if L[j - 1] > L[j]:
                L[j - 1], L[j] = L[j], L[j - 1]
    return L

if __name__ == '__main__':
    L = [randrange(1000) for _ in range(10)]
    print(bubble_sort(L))
