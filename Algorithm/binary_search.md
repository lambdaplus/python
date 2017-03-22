# 二分法查找

二分法查找，顾名思义，二分、二分就是分成两半呗。(有的翻译是`折半法搜索`比如SICP里翻译的就是`折半法搜索`)。它的复杂度为O(logn)，在列表(已排序)中对给定值`value`进行查找并输出其索引(index)值。

```python
# -*- coding: utf-8 -*-


def binary_search(lst, value):
    left, right = 0, len(lst) - 1

    while left <= right:
        middle = (left + right) // 2 # 取`lst`中值索引

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
    middle = (left + right) // 2

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

昨天面试,面试官出了一道算法题:

> 有一个数组,其内元素先递增后递减,请找出其中的最大值.

对于我来说,当时第一个想起来的是,`排序`但是转念间就知道肯定不是最好的啦.于是就在哪儿想啊想,还是想不起来.气氛挺尴尬的,外面也挺冷的(电话面试,外面安静).我想不起来,面试小哥也不急着催我,最后也算是在小哥的提示下,想起了怎么做啦!(太感谢小哥啦, 小哥好人! 喂, 你们几个不许笑啊喂!)

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
