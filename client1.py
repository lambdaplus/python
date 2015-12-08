# -*- coding:utf-8 -*-
import socket
#client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#establish connection
s.connect(('127.0.0.1', 9999))
#receive a welcome message
print(s.recv(1024).decode('utf-8'))
for data in [b'Lambda', b'Bond', b'alpha']:
    #send data
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

