
class Myhandler(SocketServer.BaseRequestHandler):
    def setup(self):
        self.file = file(path,"r")
        self.content = self.file.read()
        self.file_header = take_hander(path)
    def handle(self):
        print("%s:%s is connected"%self.client_address)
        request_data = self.request.recv(512)
        print(request_data)
        self.request.sendall(self.content)
    def finish(self):
        print("%s is done"%self.name)
        if self.file.closed == False:
            self.file.close()

#通过多继承形成新的支持多线程的服务器
class Myserver(SocketServer.TCPServer,SocketServer.ThreadingMixIn):
    pass

#实例化我们的服务器
    #将我们要绑定的地址和写好的handler作为参数传入
m = Myserver(("127.0.0.1",8000),Myhandler)
#用多线程进行启动
th = threading.Thread(target=m.serve_forever(),args=())
th.start()

m.shutdown()
m.server_close()
