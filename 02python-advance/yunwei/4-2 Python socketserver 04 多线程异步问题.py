#coding:utf-8

import sys
import time
import threading
import SocketServer
#任务：
    #将while 讲过的传给大家的代码整理完成文件分发的功能
    #头文件以json的格式传递
#头文件
"""
{
    "method":"put or get",
    "name":"file_name",
    "size":"file_size",# 我们接受文件按照头文件给出的文件大小进行多次接受
                        # 3M 1024
    "date":"1991-05-17",
    "author":"file_author"
}


if __name__ == "__main__":
    command = raw_input("please enter your command")
    path = raw_input("please enter your path")
else:
    #sys.argv 获取命令行传入的参数，是一个列表，默认一个长度
    #command: put get
    #path 文件路径
    if len(sys.argv) != 3:
        #sys.argv 长度是3的话那我们有2个参数
        num = len(sys.argv)-1
        raise TypeError("this method need 2 argument %s given"%num)
    else:
        command = sys.argv[1]
        path = sys.argv[2]
        print "%s:%s is start" % (command, path)
#向客户端发送1.txt

class Myhandler(SocketServer.BaseRequestHandler):
    def setup(self):
        if command == "put":
            self.f = open(path,"rb")
            self.content = self.f.read()
        elif command == "get":
            self.f = open(path,"wb")
        else:
            raise AttributeError("command error no command named %s"%command)
    def handle(self):
        if command == "put":
            self.request.sendall(self.content)
    def finish(self):
        if self.f:
            self.f.close()
        print("finish is doing")

class MyServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass




m = MyServer(("127.0.0.1",8000),Myhandler)
th = threading.Thread(target=m.serve_forever)
th.start()
"""














