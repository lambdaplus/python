# coding=utf-8


def binary_search(L, t):
    if len(L) <= 1:
        return L

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
    L = [1, 3, 65, 70, 77, 87, 987, 2345]  # list must be order
    print(binary_search(L, 1))
    print(binary_search(L, 3))
    print(binary_search(L, 350))
    print(binary_search(L, 987))
    print(binary_search(L, 2345))
