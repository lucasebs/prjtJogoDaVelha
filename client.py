#!/usr/bin/env python
import socket, jogo

host = 'localhost'
port = 50001
size = 1024
MSG_CLIENT = jogo.get_Pos2()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

def client():
    s.send(jogo.online.get_Pos2())
    msgServer = s.recv(size)
    i = msgServer[0]
    j = msgServer[1]
    testejogo.Matriz[i][j] = 'O'
    s.close()