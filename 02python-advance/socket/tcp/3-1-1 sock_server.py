#coding:gbk
#python socket
    #socket tcp/ip ���� 
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#�����ľ���һ��tcp/ip ��socket
sock.bind(("127.0.0.1",8003))
sock.listen(5)
while True:
    con,add = sock.accept()
    print(con)
    print(sock)
    print(add)
    print("%s:%s is connect"%add)#(ip,port)
    while True:
        recv_data = con.recv(512)
        print(recv_data)
        if recv_data == "break":
            break
        send_data = raw_input(">>>")
        con.send(send_data)
        if send_data == "break":
            break
    if send_data == "break":
            break    
sock.close()    
    
"""
while True:
    con,add = sock.accept()
        #con:���պͷ�����Ϣ��
        #add:�����������û���ip�Ͷ˿�(ip,port)
    print(con.recv(512))
    con.send("hello world")
"""
sock.close()


