#coding:utf-8
"""
import time
import threading
import SocketServer #3.x socketserver

request_pool = []

class Myhandler(SocketServer.BaseRequestHandler):
    def setup(self):
        request_pool.append(self.request)
        print("%s:%s is connected"%self.client_address)
    def handle(self):
        request_data = self.request.recv(512)
        print(self.request)
        print(request_pool)
        while True:
            time.sleep(2)
            self.request.sendall("hello world")
    def finish(self):
        print("finish is doing")
        request_pool.remove(self.request)

class MyServer(SocketServer.TCPServer,SocketServer.ThreadingMixIn):
    pass


m = MyServer(("127.0.0.1",8006),Myhandler)
th = threading.Thread(target=m.serve_forever(),args=())
th.start()

import time
import threading
import SocketServer #3.x socketserver

request_pool = []

class Myhandler(SocketServer.BaseRequestHandler):
    def setup(self):
        request_pool.append(self.request)
        print("%s:%s is connected"%self.client_address)
    def handle(self):
        request_data = self.request.recv(512)
        print(self.request)
        print(request_pool)
        while True:
            time.sleep(2)
            self.request.sendall("hello world")
    def finish(self):
        print("finish is doing")
        request_pool.remove(self.request)

class MyServer(SocketServer.TCPServer,SocketServer.ThreadingMixIn):
    pass


m = MyServer(("127.0.0.1",8006),Myhandler)
th = threading.Thread(target=m.serve_forever(),args=())
th.start()


import time
import threading
def hello():
    while True:
        time.sleep(1)
        print("hello")
        
def hi():
    while True:
        time.sleep(1)
        print("hi")
    

t1 = threading.Thread(target=hello,args=())
t1.start()
t = threading.Thread(target=hi,args=())
t.start()
"""
import time
import threading
def hello():
    while True:
        print("hello")
        
def hi():
    while True:
        print("hi")
    

t1 = threading.Thread(target=hello,args=())
t = threading.Thread(target=hi,args=())
t1.start()
t.start()
t1.join()
t.join()


