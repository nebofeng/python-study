#coding:gbk

#thread
    #setDaemon #设置守护线程
    #lock #全局解释权锁
#spider 爬虫的基础
    #2节课
    #scrapy 爬虫的框架

    #从具体到urllib request urllib2 这些模块开始讲
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
        #name 本来就是threading.Thread
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

















