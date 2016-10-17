斐波那契数列的几种算法

1. 普通的循环
```python
# -*- coding: utf-8 -*-

def fib(n):
    lst = []
    m, a, b = 0, 0, 1
    for m in range(n):
        lst.append(a)
        a, b = b, a + b

    return lst

if __name__ == "__main__":
    n = int(input('Please input n > '))
    print(fib(n))
```

2. 高效的生成器
```python
def fib(n):
    m, a, b = 0, 0, 1
    for m in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    lst = []
    n = int(input('Please input n > '))
    for i in fib(n):
        lst.append(i)
    print(lst)
```
## 当然还有各种lambda奇淫技巧，不写了！

------分割线------

## 复杂度为O(n)的递归fibonacci seq。
```python
def fib(n):
	if n <= 1:
		return (n, 0)
	else:
		(a, b) = fib(n-1)
		return (a+b, a)
```
