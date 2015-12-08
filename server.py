# -*- coding: utf-8 -*-
import socket, time, threading
#TCP socket based on ipv4
#server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#listening on port
s.bind(('127.0.0.1', 9999))
s.listen(5)
print("Waiting for connection...")

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

while True:
    #receive a new connect 
    sock, addr = s.accept()
    #make a new thread dispose TCPlink
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

