# -*- coding:utf-8 -*-
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

if __name__ == '__main__':
	n = int(input('n = '))
	print(factorial(n))
