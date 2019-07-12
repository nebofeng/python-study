#coding:gbk
import socket
"""
#socket udp

#1、创建socket对象
    #TCP SOCK_STREAM 面向连接的
    #UDP SOCK_DGRAM 无连接的
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#2、绑定socket对象
sock.bind(("127.0.0.1",8000))
#3、接收数据
con,add = sock.recvfrom(512)
#4、发送数据
sock.sendto("I am you friend",("127.0.0.1",9000))
#5、关闭数据
sock.close()

print("this is server ? 8009")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",8009))
while True:
    con,add = sock.recvfrom(512)
    print("%s:%s is connected"%add)
    print(con)
    if con == "break":
        break
    send_data = raw_input(">>>")
    sock.sendto(send_data,("127.0.0.1",8010))
    if send_data == "break":
        break
sock.close()
"""
print("this is server ? 8009")
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",8009))
while True:
    con,add = sock.recvfrom(512)
    print("%s:%s is connected"%add)
    print(con)
    if con == "break":
        break
    #send_data = raw_input(">>>")
    #sock.sendto(send_data,("127.0.0.1",8010))
    #if send_data == "break":
    #    break
sock.close()


select
Twisted







