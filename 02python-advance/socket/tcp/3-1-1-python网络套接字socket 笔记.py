#coding:gbk

#python 网络编程
#socket 套接字：网络接口。
#我们在网络上需要传输自己需要的数据，我们在网络上传输数据
#使用的是网络协议，而套接字就是我们将数据从本地采用协议传输
#的接口

#通信的模式
    #单工通信:通信双方占有单条信道，收发双方身份不可逆 BB机
    #半双工通信:通信双方占有单条信道，收发双方身份可逆 对讲机
    #全双工通信:通信双方占有多条信道，收发双方身份可逆 手机

    #2.x
        #unicode
        #str
    #3.x
        #bytes 
        #str

import socket

#1、创建socket对象

#socket 服务端

#sock = socket.socket()
    #socket_family:
        #AF_UNIX 被使用在类unix系统之间进行通信的socket族
        #AF_INET 被使用在网络间的通信的socket族
        #AF_INET6 被使用在ipv6协议上的socket族
    #socket_type:针对于协议说的
        #SOCK_STREAM 针对于tcp/ip协议的socket类型
        #SOCK_DGRAM 针对udp协议的socket类型

            #TCP/IP 面向连接的协议
            #UDP 无连接的协议
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2、绑定套接字
sock.bind(("127.0.0.1",8000))
    #绑定需要一个双元素的元组
        #ip 就是本机的ip ip如果写成""那么代表绑定本地所有ip
        #port 端口 0-65535 前一千个我们通常不用
        #端口会有被占用的情况，假如socket绑定了一个端口
        #但是没有关闭或者关闭没有释放端口，就会存在端口占用
#3、监听
sock.listen(5)
    #listen的参数同时监听的个数
    #被动阻塞式的接收
        #1、被动等待访问
        #2、访问进行的过程当中不可以与其他用户进行联系

#4、信息的接收和发送
con,add = sock.accept()
    #sock.accept返回两个值，我们使用序列解包的赋值方式进行赋值
    #sock.accept返回两个值
        #第一个是用来发送和接收数据的一个对象
           #con.recv(512) #是socket tcp协议独有的一个
                          #接收方式,需要制定一次接收文件的大小
           #con.send(str) #是socket tcp协议独有的一个
                          #发送方式，只能发送字符串  
        #第二个是用来显示连接者身份
#5、通信完成关闭套接字释放端口
sock.close()


#socket 客户端
#1、创建套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2、连接指定服务端
sock.connect(("127.0.0.1",8000))
    #这里的ip是要连接的服务端的ip
    #这里的端口是要连接的服务端的端口
#3、收发信息
sock.recv(512)
sock.send(str)
#4、关闭连接
sock.close()







































