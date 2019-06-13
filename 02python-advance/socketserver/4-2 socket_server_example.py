#coding:gbk

import socketserver
"""
class MyTCPHandler(socketserver.BaseRequestHandler):
    #我们写这个类是为了给socketserver做handler

    def handle(self):
        #重写socketserver.BaseRequestHandler当中的handle
        #socketserver.BaseRequestHandler当中的handle是用来处理请求的一切的
        #但是默认do noting
        #handle 默认的实例属性
            #self.request 该参数就是socket本身的链接
            #self.client_address 该参数是链接上来的用户的ip和端口
            #self.server 是服务器的信息
        self.data = self.request.recv(1024).strip()
            #接受客户端发上来的请求，并且进行去掉两端空格的处理
        print("{} wrote:".format(self.client_address[0]))
            #打印请求者的ip
        print(self.data)
        self.request.sendall(self.data.upper()) #发送数据
        print(self.server)
if __name__ == "__main__":
    HOST, PORT = "localhost",8000 #序列解包赋值
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    #实例化一个TCPServer
    server.serve_forever()
    #让服务器保持一种一直在监听的状态

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        print(self.rfile)#将请求内容形成缓冲的方法
        print(self.wfile)#将响应内容形成缓冲的方法        
        print(self.request)#是该链接的socket对象 
        print(self.client_address)#是链接者的地址和端口
        print(self.server)
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost",8000 
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()


import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        print(socket)
        
        socket.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
"""

import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    #构造一个自己的多线程的TCP的请求handler
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')#接收数据
        cur_thread = threading.current_thread() #指出当前线程线程
            #current_thread 类似于我们class当中的self 返回当前的线程
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')#返回线程的名称和数据
        self.request.sendall(response)#发送消息

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)#实例化服务器
    ip, port = server.server_address#获取服务器的ip和端口


    server_thread = threading.Thread(target=server.serve_forever)#对服务器的运行进行多线程
    server_thread.daemon = True#将该线程设置为守护线程
    server_thread.start()#开始跑线程
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, "Hello World 1") #启动三个客户端进行连接
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    server.shutdown() #停止服务器
    server.server_close() #关闭服务器




