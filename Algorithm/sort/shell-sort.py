#coding=utf-8
def shell_sort(seq):
    if len(seq) < 2:
        return seq

    n = len(seq)
    mid = n // 2
    while mid > 0:
        for i in range(mid, n):
            tmp = seq[i]
            j = i
            while j >= mid and seq[j-mid] > tmp:
                seq[j] = seq[j-mid]
                j -= mid
            seq[j] = tmp
        mid = mid // 2
    return seq

