#coding:utf-8
"""
客户端
    自动监听本地的信息并且发送给服务器
    采用的socket TCP协议
"""

import os
import sys
import time
import socket
import configparser #ConfigParser 2.x
import queue #队列模块，Queue


class Client:
    """
        我们要实现
          1、读取配置文件
          2、发送数据
    """
    def __init__(self,addr=("127.0.0.1",8000)):
        """
            addr must be a tuple as ("ipaddress",port)
        """
        #创建socket对象，并赋值给实例变量
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.log_file = open("err_log.txt","a") #创建错误日志文件
        try:
            self.sock.connect(addr)#链接服务器
        except TimeoutError as e:
            self.sock = None
            self.logger(e) #记录日志
            raise TimeoutError(e)

    def reader(self,path):
        #使用os模块执行Linux cat 命令，对指定路径下的文件进行查看
        #并以文件的形式将监控的文件的内容进行返回
        self.file = os.popen("cat %s"%path)
        self.content = self.file.read()#读出文件的内容
        self.file.close()#关闭文件对象
        return self.content #返回执行结果的字符串形式

    def sender(self):
        if self.sock and self.content:#判断套接字和发送的内容存在且为真
            self.sock.send(self.content)#发送内容
        else:#发生错误
            if self.sock:
                self.logger("send content should not be None")
                raise TypeError("send content should not be None")
            else:
                raise TypeError("connection should not be None")

    def logger(self,content):
        content = "[%s]:[%s]\n"%(time.ctime(),content)#格式化一个字符串
        self.log_file.write(content)#写到文件里

    def __del__(self):
        self.sock.close() #将套接字关闭
        if not self.log_file.closed: #判断错误日志是否关闭
            self.log_file.close() #关闭错误日志


#递归是一个深度遍历
#for 是广度遍历
#while 是个深度遍历








