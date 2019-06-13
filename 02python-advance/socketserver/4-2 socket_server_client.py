#coding:gbk
"""
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",9999))
sock.send("hello world \n".encode())
print(sock.recv(1024))
sock.close()

"""
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("",8000))
sock.sendto("hello world \n".encode(),("127.0.0.1",9999))
print(sock.recvfrom(1024))
sock.close()
