## 合并两个单调递增的列表返回一个单调不减列表

简直就是一个简易版的[归并排序](https://github.com/lambdaplus/python/tree/master/Algorithm/sort/merge)

```python
# -*- coding: utf-8 -*-

from random import randrange

def merge_two_list(lst1, lst2):
    rst = []
    while lst1 and lst2:
        if lst1[-1] > lst2[-1]:
            rst.append(lst1.pop())
        else:
            rst.append(lst2.pop())
    rst.reverse()        
    return (lst1 or lst2) + rst

if __name__ == "__main__":
    lst1 = sorted([randrange(100) for _ in range(10)])
    print('lst1 is : ', lst1)
    lst2 = sorted([randrange(100) for _ in range(6)])
    print('lst2 is : ', lst2)
    print('The merged list is\n', merge_two_list(lst1, lst2))
```
