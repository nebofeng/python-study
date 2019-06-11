#coding:gbk
#python socket
    #socket tcp/ip 部分 
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建的就是一个tcp/ip 的socket
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
        #con:接收和发送信息的
        #add:连接上来的用户的ip和端口(ip,port)
    print(con.recv(512))
    con.send("hello world")
"""
sock.close()


