#!/usr/bin/env python
import socket, testejogo

host = ''
port = 50001
backlog = 5
size = 1024
MSG_SERVER = testejogo.get_Pos1()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

def do():
    while 1:
        client, address = s.accept()
        client2, address = s.accept()
        msgClient = client.recv(size)
        i = msgClient[0]
        j = msgClient[1]
        testejogo.Matriz[i][j] = 'x'
        client.send(testejogo.online.get_Pos1())
        client.close()
