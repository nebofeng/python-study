#coding:gbk
import threading
from time import sleep,ctime
#setDaemon �����ػ��߳�
    #�����Ǵ������߳�֮�����߳�֮�»���n�����߳�
    #һ������̣߳������߳��˳�֮�󲢲����˳�
    #�������ǽ��̱߳��Ϊ�ػ��߳�֮��
    #�����߳��˳�֮�����̻߳�����˳�

    #�ػ��̻߳������߳̽�����ʱ��ɱ��
    #һ����߳�û�н������̻߳������
"""

class My_thread(threading.Thread):
    def __init__(self,names):
        self.names = names
        #name ��������threading.Thread
        threading.Thread.__init__(self)
    def run(self):
        while True:
            print("hello I am your thread %s"%self.names)


m = My_thread("xiaomin")
m1 = My_thread("xiaowang")
#m.setDaemon(True) #��һ���߳�����Ϊ�ػ��̣߳�������start֮ǰ����
m1.setDaemon(True)
m.start()
m1.start()

print("all done")

class My_thread(threading.Thread):
    def __init__(self,names,times):
        self.names = names
        self.times = times
        threading.Thread.__init__(self)
    def run(self):
        print("%s is start"%self.names)
        sleep(self.times)
        print("%s is done"%self.names)


m = My_thread("xiaomin",3)
m1 = My_thread("xiaowang",4)
m.setDaemon(True)
m.start()
m1.start()
sleep(1)

class My_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        f = open("1.txt","w")
        while True:
            f.write("hello world")
        f.close()
print("all is start")
f = My_thread()
f.setDaemon(True)
f.start()
print("all is done")
print("all done")
"""


#join()
"""
class My_thread(threading.Thread):
    def __init__(self,names):
        self.names = names
        #name ��������threading.Thread
        threading.Thread.__init__(self)
    def run(self):
        while True:
            print("hello I am your thread %s"%self.names)


m = My_thread("xiaoming")
m1 = My_thread("xiaowang")
m.start()
m.join()

class My_thread(threading.Thread):
    def __init__(self,names,times):
        self.names = names
        self.times = times
        threading.Thread.__init__(self)
    def run(self):
        print("%s is start"%self.names)
        sleep(self.times)
        print("%s is done"%self.names)


m = My_thread("xiaomin",3)
m1 = My_thread("xiaowang",4)
print(ctime())
m.start()
m1.start()
m.join()
m1.join()
print(ctime())
"""
#lock
    #thread 3.x _thread
        #lock = allocate_lock
    #threading
        #lock = Lock

    #acquire() #��ȡ��
    #release() #�ͷ���
    #locked() #�ж��Ƿ���� 
        
"""
class My_thread(threading.Thread):
    def __init__(self,names,locks,times):
        self.locks = locks
        self.names = names
        self.times = times
        threading.Thread.__init__(self)
    def run(self):
        self.locks.acquire()
        sleep(self.times)
        print("this is Threads %s"%self.names)
        self.locks.release()

threads = []
l = threading.Lock()
for i in range(10):
    t = My_thread(i,l,i)
    threads.append(t)
    
for i in threads:
    i.start()
    
for i in threads:
    i.join()

class My_thread(threading.Thread):
    def __init__(self,names,locks,times):
        self.locks = locks
        self.names = names
        self.times = times
        threading.Thread.__init__(self)
    def run(self):
        self.locks.acquire()
        sleep(self.times)
        print("this is Threads %s"%self.names)
        self.locks.release()

threads = []

for i in range(10):
    l = threading.Lock()
    t = My_thread(i,l,i)
    threads.append(t)
    
for i in threads:
    i.start()
    
for i in threads:
    i.join()
"""

#spider
    #���棬spider ����֩��: �������ݵ����������ݵĲɼ���ץȡ��Ҳ���˳�����Ϊ�ɼ�������

    #��������ѧϰ�Ĺ��̵���ѧϰ�����׶�
        #���������棬����ʹ��python��ģ���һЩ����Ҫ��¼����վ���ݽ��вɼ�������
        #ģ���¼������ͨ������httpЭ����е�¼����վģ����������е�¼
        #���ǻ��漰������(proxy)���ݹ飬���̣߳��ֲ�ʽ���ֳ���������

    #����Ĳ���
        #����
        #���󡢴�����Ӧ
        #����ɸѡ
        #���ݴ洢

        #scrapy ���
        
        #���:
            #�����һ�ο�����ʱ������ȫ�Ľ�һ����Ŀд����
            #����ڶ��ο���ͬ������Ŀ��ʱ���㷢�ֵ�һ�ο���������һ���ִ�����Ը���
            #���㵫���ο�����ʱ����ѵ�һ�ζ��ο��Ը��õĴ�������˷�װ
            #������������γ���һ�����
            #��ܾ���ָ��һ�๲�Ե���Ŀ�Ĺ��ԵĹ���д��һ�����Է��㸴�õĴ�Ĺ��ܿ��

        #����
            #����http����
            #����HTML������
            #����js��ajax����
                #Firefox
                    #�����߹���
                    #firebug
                    #httpfox
                    #����ץ��
        #�������Ӧ����
            #����ģ��
            #urllib
            #urllib2
            #requests

            #httplib
            #cookielib
            #hashlib
        #����ɸѡ
            #ƥ��ģ��
            #re
            #lxml xpath
            #beautifulsoup bs4
        #���ݴ洢
            #mysql
            #file #file ��־��¼
            
#��ĩʵս
    #Twisted
    #select

import re
import urllib
import urllib2

from lxml import etree


url = "http://www.pengfu.com/qutu_1.html"
hander = {
    "User-agent":"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04"
    }
req = urllib2.Request(url,data=None,headers=hander)
ope = urllib2.urlopen(req)
content = ope.read()
res = re.findall('<img src="(.*)?"',content,re.M)
#print(content)
for i in res:
    urls = i.split("\"",1)[0]
    print(urls)
    name = urls.rsplit("/",1)[1]
    print(name)
    urllib.urlretrieve(urls,name)


















