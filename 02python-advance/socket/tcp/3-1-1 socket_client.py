#coding:gbk


import socket
'''
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("this is socket_client")
sock.connect(("127.0.0.1",8000))
sock.send("hello I am your client")
print(sock.recv(512))
sock.close()

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8003))
while True:
    sends = raw_input("��˵ɶ>>>")
    sock.send(sends)
    if sends == "break":
        break
    recvs = sock.recv(512)
    print(recvs)
    if recvs == "break":
        break
sock.close()
'''

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8003))
while True:
    sends = raw_input("��˵ɶ>>>")
    sock.send(sends)
    if sends == "break":
        break
    recvs = sock.recv(512)
    print(recvs)
    if recvs == "break":
        break
sock.close()
