# -*- coding: utf-8 -*-

def hello(name):
	print('Hello {!s}'.format(name))

if __name__ == '__main__':
	name = input('Please input your name: ')
	hello(name)
