## 合并两个单调递增的列表返回一个单调不减列表

简直就是一个简易版的[归并排序](https://github.com/lambdaplus/python/tree/master/Algorithm/sort/merge)

```python
# -*- coding: utf-8 -*-

from random import randrange

def merge_two_list(lst1, lst2):
    while lst1 and lst2:
        lst3.append(lst1.pop(0) if lst1[0] <= lst2[0] else lst2.pop(0))

    while lst1:
        lst3.append(lst1.pop(0))

    while lst2:
        lst3.append(lst2.pop(0))

    return lst3

if __name__ == "__main__":
    lst3 = []
    lst1 = sorted([randrange(100) for _ in range(10)])
    print(lst1)
    lst2 = sorted([randrange(100) for _ in range(6)])
    print(lst2)
    print(merge_two_list(lst1, lst2))
```
