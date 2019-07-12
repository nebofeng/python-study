#coding:utf-8

import os
import sys
import time
import json
import threading
import SocketServer

#stream
#dgram
#SocketServer.StreamRequestHandler 是tcp专用的handle
path = "1.txt"
class MyHandle(SocketServer.StreamRequestHandler):
    def setup(self):
        #该方法来源于BaseHandler,在BaseHandler当中默认为pass
            #其作用是在handle执行之前自动执行
        #self.client_address 是BaseHandler里面写好的用来接受请求地址和端口的视力属性
        print("%s:%s is connect"%self.client_address)
        #self.path.exists 可以判断一个文件是否存在
        self.have_file = os.path.exists(path)
    def hander(self):
        #我们自己定义的一个文件头部
        if self.have_file:
            name_split = path.rsplit(os.path.sep, 1)
            if len(name_split) > 1:
                file_name = name_split[1]
            else:
                file_name = name_split[0]
            hander = {
                "method":"put",
                "name": file_name,
                "size": os.path.getsize(path),
                "data": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "code": "utf-8"
            }
            json_data = json.dumps(hander)
            return json_data
        else:
            raise IOError("the file is not fond")
    def file_data(self,path):
        self.f = open(path,"rb")
        return self.f.read()
    def handle(self):
        #该方法来源于BaseHandler,在BaseHandler当中默认为pass
            #其作用是用来处理socket接受和发送的一切问题
        #self.request.recv 是BaseHandler里面写好的socket对象

        #因为我们socket发送只能发送字符串
        #所以我们将我们定义好的头部用json打包成字符串进行发送
        data = self.request.recv(512)
        print(data)
        self.request.sendall(self.hander())
        while True:
            json_request = self.request.recv(128)
            print(json_request)
            print(type(json_request))

            requests = json.loads(json_request)
            print(requests)
            self.request.send("sssss")
            # if request[u"method"] == u"get":
            #     content = self.file_data(request[u"name"])
            #     self.request.send("sssss")
            #     print("22222")
            # elif request[u"method"] == u"put":
            #     pass
            # else:
            #     print("111111")
    def finish(self):
     #   self.f.close()
        print("send is over")

class MyServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

m = MyServer(("127.0.0.1",8005),MyHandle)
th = threading.Thread(target=m.serve_forever,args=())
th.start()






















