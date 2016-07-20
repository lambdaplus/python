# -*- coding: utf-8 -*-

def your_range(start, stop=None, step=1):
    '''
    实现你自己的range函数
    '''
    if stop is None:
        start, stop = 0, start

    if step == 0:
        raise ValueError('step cannot be 0')

    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    
    return result

print(your_range(8))
print(your_range(1, 8))
print(your_range(3, 8))
print(your_range(3, 8, 2))
print(your_range(-8, 0))
print(your_range(-8, 2))
print(your_range(-8, -2, 2))

'''运行结果
mouse@debian ~/python> python3 your_range.py 
[0, 1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[3, 4, 5, 6, 7]
[3, 5, 7]
[-8, -7, -6, -5, -4, -3, -2, -1]
[-8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
[-8, -6, -4]
'''
