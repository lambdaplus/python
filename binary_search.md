
---
title: 二分法查找
date: 2016-09-23 15:32:24
tags: Algorithm
---

二分法查找，顾名思义，二分、二分就是分成两半呗。(有的翻译是`折半法搜索`比如SICP里翻译的就是`折半法搜索`)。它的复杂度为O(logn)，在列表(已排序)中对给定值`value`进行查找并输出其索引(index)值。

```python
# -*- coding: utf-8 -*-


def binary_search(lst, value):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        middle = int((left + right) / 2) # 取`lst`中值索引
        
        if value > lst[middle]:
            left = middle + 1 # value大于`lst`中值，让左边界等于 middle + 1
        elif value < lst[middle]:
            right = middle - 1 # 类似上
            
        else:
            return "The value's index is {}".format(middle)
    return "There is no {}".format(value)

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9]
    value = int(input("Please input the value(1-10): "))
    print(binary_search(lst, value))

```

再来个递归(recursion)版的吧， 不作过多解释啦！
```python
# -*- coding: utf-8 -*-


def binary_search_rec(lst, value, left, right):
    middle = int((left + right) / 2)

    if left > right:
        return "I'm sorry, there is no {}".format(value)

    if value < lst[middle]:
        return binary_search_rec(lst, value, left, middle - 1)

    elif value > lst[middle]:
    	return binary_search_rec(lst, value, middle + 1, right)

    else:
        return "Congratulations, the value's({}) index is {}".format(value, middle)


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9]
    left, right = 0, len(lst)
    value = int(input("Please input the value: "))
    print(binary_search_rec(lst, value, left, right))
```
没事。温习以下二分搜索！

被拼写错误折磨了一晚上。好好的lft被我写成ltf。debug生无可恋！
```python
from random import randrange
def binary_search(seq, sit, lft, rgt):
    mid = (lft + rgt) // 2
    
    if lft > rgt:
        return 'The seq no {}'.format(sit)
    
    if sit > seq[mid]:
        return binary_search(seq, sit, mid+1, rgt)
    
    elif sit < seq[mid]:
        return binary_search(seq, sit, lft, mid-1)
    
    else:
        return 'The {} in the seq and the station is {}'.format(sit, mid)
        
if __name__ == '__main__':
    seq = [1, 4, 6, 8, 9, 12, 44, 56]
    lft, rgt = 0, len(seq)
    print(binary_search(seq, 4, lft, rgt))
```
昨天面试,面试官出了一道算法题:

> 有一个数组,其内元素先递增后递减,请找出其中的最大值.

对于我来说,当时第一个想起来的是,排序但是转念间就知道肯定不是最好的啦.于是就在哪儿想啊想,还是想不起来.气氛挺尴尬的,外面也挺冷的(电话面试,外面安静).我想不起来,面试小哥也不急着催我,最后也算是在小哥的提示下,想起了怎么做啦!(太感谢小哥啦, 小哥好人! 喂, 你们几个不许笑啊喂!)

当然是**二分**啦,下面是算法实现!

```python
# coding=utf-8
def search_max_num(seq, left, right):
    mid = (right + left) // 2
    if left > right:
        return seq[mid]
    if seq[mid] > seq[mid - 1]:
        return search_max_num(seq, mid + 1, right)
    else:
        return search_max_num(seq, left, mid - 1)
if __name__ == "__main__":
    seq = [32, 55, 54, 54, 54, 54, 32, 15, 6, 4, 2, 1]
    print(search_max_num(seq, 0, len(seq)))
```
###  二维数组的查找
class Solution:
    # array 二维列表

    def find(self, target, array):
        # write code here
        for arr in array:
            lft, rgt =0, len(arr) - 1
            while lft <= rgt:
                mid = (lft + rgt) // 2
                if target > arr[mid]:
                    lft = mid + 1
                elif target < arr[mid]:
                    rgt = mid - 1
                else:
                    return arr[mid]
        return 'No target'


target = 8
array = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10]
]
solution = Solution()
solution.find(target, array)
```
