# -*- coding: utf-8 -*-

import socket, time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind port
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999')
while True:
	#receive data
	data, addr = s.recvfrom(1024)
	time.sleep(2)
	print("Received from %s:%s." % addr)
#	s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)
#	s.sendto(b'Hello '+ data, addr)
	s.sendto(b'Hello, %s!' % data, addr)

