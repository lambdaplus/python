# -*- coding: utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Lambda', b'Bond', b'alpha']:
	#send data
	s.sendto(data, ('127.0.0.1', 9999))
	#rev data
	print(s.recv(1024).decode('utf-8'))
s.close()
