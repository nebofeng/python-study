#coding:gbk

import socketserver
#import SocketServer
#����Ҫ���������Ǵ���һ��������
    #�������֣�TCP,UDP��
        #BaseServer
            #�������socketserver���еĳ��࣬
            #���Ǿ������漰���������Ǻ���ֱ��ʹ���������������²�Ľӿڡ�
        #TCPServer
        #UDPServer

#socketserver.TCPServer()
#socketserver.UDPServer()
    #server_address ����Ҫ��server�󶨵�ip��ַ�Ͷ˿�("127.0.0.1",8000)
        #���Ǽ����ĵ�ַ�����͸������ǲ��õ�Э��Ĳ�ͬ����ͬ��
        #������Э�鷽�棬����һ���ַ����ĵ�ַ�����ֵĶ˿���ɵ�Ԫ�档
    #RequestHandlerClass
        #�����û�������࣬������Ϊÿһ�����󴴽�ʵ��
        #��������������Э�������
        #�������Ҫ���Ǽ̳���д
            #BaseRequestHandler #ģ�����handler
            #StreamRequestHandler #��tcpЭ���handler
            #DatagramRequestHandler #��udpЭ���handler
            #handlerͬ����һ���࣬��Ҫ���Ƕ����д
                #setup() ��handle֮ǰ���д���Ĭ��do nothing
                #handle() �������˵����Ҫ�Ĺ��� Ĭ��do nothing
                    #self.request ����ÿ�������socket
                    #self.client_address�����ߵ�ַ
                    #self.server ����������Ϣ
                #finish() ��β�Ĺ��� Ĭ��do nothing

    #�������������������server�࣬Ŀ������ʹ���������ж��̻߳��߶���̵Ĺ���
        #ForkingMixIn  #�����
        #ThreadingMixIn #���߳�





