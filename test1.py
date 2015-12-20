# -*- coding: utf-8 -*-
#q = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
q = '0123456789'
Q = list(q)
for i in range(len(q)):
	print(q)
	ss = Q.pop(0)
	Q.append(ss)
	q = ''
	q = q.join(Q)
