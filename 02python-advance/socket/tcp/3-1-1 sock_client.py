#coding:gbk
#python socket
    #socket tcp/ip ���� 
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#�����ľ���һ��tcp/ip ��socket
sock.connect(("127.0.0.1",8003))
while True:
    send_data = input(">>>")
    sock.send(send_data.encode())
    if send_data == "break":
        break
    recv_data = sock.recv(512)
    print(recv_data)
    if recv_data == "break":
        break
sock.close()
