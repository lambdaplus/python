# coding: utf-8
# %load python/Algorithm/joseph-ring.py
def joseph_ring(n, m):
    if n < 1:
        return -1
    
    result = -1
    start = 0

    ring_num = list(range(n))
    while ring_num:
        k = (start + m - 1) % n
        result = ring_num.pop(k)
        n -= 1
        start = k
    return result
