#coding:gbk

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",8001))
print(sock.recvfrom(1024))
print("this is server")
sock.sendto("hi world \n".encode(),("127.0.0.1",8000))

sock.close()
