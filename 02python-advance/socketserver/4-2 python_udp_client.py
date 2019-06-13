#coding:gbk

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",8000))
sock.sendto("hello world \n".encode(),("127.0.0.1",8001))
print(sock.recvfrom(1024))
print("this is client")
sock.close()
