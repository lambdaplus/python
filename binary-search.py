# coding=utf-8


def binary_search(L, t):
    low, high = 0, len(L)
    while low < high:
        mid = int((low + high) / 2)
        if L[mid] > t:
            high = mid
        elif L[mid] < t:
            low = mid + 1
        else:
            return mid

    return low if L[low] == t else False

if __name__ == '__main__':
    L = [1, 2, 30, 55, 67, 88, 350, 670]
    print(binary_search(L, 1))
    print(binary_search(L, 30))
    print(binary_search(L, 350))
    print(binary_search(L, 20))
    print(binary_search(L, 670))
