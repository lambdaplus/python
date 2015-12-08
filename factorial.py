# -*- coding:utf-8 -*-
def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return factorial(n-1)*n

if __name__ == '__main__':
	n = int(input('n = '))
	print(factorial(n))
