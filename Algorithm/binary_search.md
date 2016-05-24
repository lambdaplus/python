# 二分法查找

标签（空格分隔）： python

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