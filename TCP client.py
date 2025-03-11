#!/usr/bin/python3

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '10.214.30.200'
host = socket.gethostbyname

port = 444

clientSocket.connect('10.214.30.200', port)

#Sets maximum amount of data client accepts at once
message = clientSocket.recv(1024) 

clientSocket.close()

print(message.decode('ascii'))