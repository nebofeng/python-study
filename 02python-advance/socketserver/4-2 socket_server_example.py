#coding:gbk

import socketserver
"""
class MyTCPHandler(socketserver.BaseRequestHandler):
    #����д�������Ϊ�˸�socketserver��handler

    def handle(self):
        #��дsocketserver.BaseRequestHandler���е�handle
        #socketserver.BaseRequestHandler���е�handle���������������һ�е�
        #����Ĭ��do noting
        #handle Ĭ�ϵ�ʵ������
            #self.request �ò�������socket���������
            #self.client_address �ò����������������û���ip�Ͷ˿�
            #self.server �Ƿ���������Ϣ
        self.data = self.request.recv(1024).strip()
            #���ܿͻ��˷����������󣬲��ҽ���ȥ�����˿ո�Ĵ���
        print("{} wrote:".format(self.client_address[0]))
            #��ӡ�����ߵ�ip
        print(self.data)
        self.request.sendall(self.data.upper()) #��������
        print(self.server)
if __name__ == "__main__":
    HOST, PORT = "localhost",8000 #���н����ֵ
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    #ʵ����һ��TCPServer
    server.serve_forever()
    #�÷���������һ��һֱ�ڼ�����״̬

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        print(self.rfile)#�����������γɻ���ķ���
        print(self.wfile)#����Ӧ�����γɻ���ķ���        
        print(self.request)#�Ǹ����ӵ�socket���� 
        print(self.client_address)#�������ߵĵ�ַ�Ͷ˿�
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
    #����һ���Լ��Ķ��̵߳�TCP������handler
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')#��������
        cur_thread = threading.current_thread() #ָ����ǰ�߳��߳�
            #current_thread ����������class���е�self ���ص�ǰ���߳�
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')#�����̵߳����ƺ�����
        self.request.sendall(response)#������Ϣ

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

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)#ʵ����������
    ip, port = server.server_address#��ȡ��������ip�Ͷ˿�


    server_thread = threading.Thread(target=server.serve_forever)#�Է����������н��ж��߳�
    server_thread.daemon = True#�����߳�����Ϊ�ػ��߳�
    server_thread.start()#��ʼ���߳�
    print("Server loop running in thread:", server_thread.name)

    client(ip, port, "Hello World 1") #���������ͻ��˽�������
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    server.shutdown() #ֹͣ������
    server.server_close() #�رշ�����




