#coding:gbk

#thread
    #setDaemon #�����ػ��߳�
    #lock #ȫ�ֽ���Ȩ��
#spider ����Ļ���
    #2�ڿ�
    #scrapy ����Ŀ��

    #�Ӿ��嵽urllib request urllib2 ��Щģ�鿪ʼ��
        #re
        #bs4
        #lxml 

        #file
        #sql

#setDeamon


import threading

class My_thread(threading.Thread):
    def __init__(self,names):
        self.names = names
        #name ��������threading.Thread
        threading.Thread.__init__(self)
    def run(self):
        while True:
            print("hello I am your thread %s"%self.names)


m = My_thread("xiaomin")
print(m.isDaemon())
m.setDaemon(True)
print(m.isDaemon())
m.start()

print("all done")

















