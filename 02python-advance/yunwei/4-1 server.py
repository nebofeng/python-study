#coding:utf-8
import socket
#import select

"""
客户端:
    1、收集并且发送数据
    2、用户可以以配置文件的形式规定监控的内容
         1、我们定制的路径可能是目录也可能是文件
         2、递归求路径
服务端:
    1、接受数据
"""
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",8000))
sock.listen(5)
con,add = sock.accept()
print("%s:%s is connected"%add)
print(con.recv(512))
sock.close()

