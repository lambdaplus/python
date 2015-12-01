#/home/mouse python3
#-*- coding: utf-8 -*-

#倒入os模块
import os

#当前进程
print('Process (%s) start...' % os.getpid())

#获得父进程
pid = os.fork()
if pid == 0:
	print('I am child process (%s) and my partent is %s.' 
		% (os.getpid(), os.getppid()))
else:
	print("I (%s) just created a child process (%s)." 
		% (os.getpid(), pid))
