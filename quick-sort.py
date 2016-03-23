# coding=utf-8


def quick_sort(L):
    if L == []:
        return L
    mid = L[0]
    small = [x for x in L if x < mid]
    big = [x for x in L if x >= mid]
    return small + [mid] + big

if __name__ == '__main__':
    L = [23, 1, 45, 3, 6, 89, 345, 8, 345]
    print(quick_sort(L))
