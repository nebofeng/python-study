#coding:gbk

import socketserver
#import SocketServer
#我们要做到事情是创建一个服务器
    #的两大种（TCP,UDP）
        #BaseServer
            #这个类是socketserver当中的超类，
            #我们经常会涉及到他，但是很少直接使用它，他定义了下层的接口。
        #TCPServer
        #UDPServer

#socketserver.TCPServer()
#socketserver.UDPServer()
    #server_address 我们要给server绑定的ip地址和端口("127.0.0.1",8000)
        #我们监听的地址，类型根据我们采用的协议的不同而不同，
        #在网络协议方面，这是一个字符串的地址和数字的端口组成的元祖。
    #RequestHandlerClass
        #处理用户请求的类，这个类会为每一个请求创建实例
        #定义服务器处理的协议的类型
        #这个类需要我们继承重写
            #BaseRequestHandler #模板类的handler
            #StreamRequestHandler #是tcp协议的handler
            #DatagramRequestHandler #是udp协议的handler
            #handler同样是一个类，需要我们定义从写
                #setup() 在handle之前进行处理，默认do nothing
                #handle() 完成请求说有需要的工作 默认do nothing
                    #self.request 就是每次请求的socket
                    #self.client_address请求者地址
                    #self.server 服务器的信息
                #finish() 收尾的工作 默认do nothing

    #这两种类是两种特殊的server类，目的用来使服务器具有多线程或者多进程的功能
        #ForkingMixIn  #多进程
        #ThreadingMixIn #多线程





