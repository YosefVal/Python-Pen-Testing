#!/usr/bin/python3

import socket

#Creating socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 444

serversocket.bind((host, port))

#Starting TCP Listener
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept() #starting connection

    print("Recieved connection from %s" % str(address)) 

    message = 'Hello, thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii')) 


    clientsocket.close()
