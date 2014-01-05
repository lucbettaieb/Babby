#!/usr/bin/env python
#Server to run to accept various commands via socket.

import socket

host = ''
port = 50000
backlog = 5
size = 256
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()

while 1:

    data = client.recv(size)

    if (data == "w\n"):
        print("W received")
    if (data == "a\n"):
        print("A received")    
	if (data == "s\n"):
        print("S received")
    if (data == "d\n"):
        print("D received")

client.close()