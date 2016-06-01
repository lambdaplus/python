# 题目
调整数组顺序使奇数位于偶数前面
## 描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

马上熄灯啦，直接贴渣渣代码！！
```python
# -*- coding: utf-8 -*-
import random


def foo(L):
    L1 = []
    L2 = []
    for i in L:
        if i % 2 != 0:
            L1.append(i)
        else:
            L2.append(i)

    return L1 + L2

if __name__ == '__main__':
    L = [random.randrange(100) for _ in range(10)]
    print(L)
    print(foo(L))

```
代码很渣，有空继续优化！！
就酱。。。洗裤子去啦。。。。。。。。
