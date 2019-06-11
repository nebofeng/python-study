#coding:gbk
import threading
from time import sleep,ctime
#setDaemon 设置守护线程
    #当我们触发多线程之后，主线程之下会有n个子线程
    #一般的子线程，在主线程退出之后并不会退出
    #但是我们将线程标记为守护线程之后
    #在主线程退出之后，子线程会跟着退出

    #守护线程会在主线程结束的时候被杀死
    #一般的线程没有结束主线程会结束吗？
"""

class My_thread(threading.Thread):
    def __init__(self,names):
        self.names = names
        #name 本来就是threading.Thread
        threading.Thread.__init__(self)
    def run(self):
        while True:
            print("hello I am your thread %s"%self.names)


m = My_thread("xiaomin")
m1 = My_thread("xiaowang")
#m.setDaemon(True) #将一个线程设置为守护线程，必须在start之前设置
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
        #name 本来就是threading.Thread
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

    #acquire() #获取锁
    #release() #释放锁
    #locked() #判断是否加锁 
        
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
    #爬虫，spider 网络蜘蛛: 用于数据的网络上数据的采集和抓取，也有人称爬虫为采集机器人

    #爬虫我们学习的过程当中学习俩个阶段
        #初级的爬虫，我们使用python的模块对一些不需要登录的网站数据进行采集和下载
        #模拟登录，我们通过分析http协议对有登录的网站模拟浏览器进行登录
        #我们会涉及到代理(proxy)，递归，多线程，分布式几种常见的爬虫

    #爬虫的步骤
        #分析
        #请求、处理响应
        #数据筛选
        #数据存储

        #scrapy 框架
        
        #框架:
            #当你第一次开发的时候，你完全的将一个项目写下来
            #当你第二次开发同样的项目的时候，你发现第一次开发当中有一部分代码可以复用
            #当你但三次开发的时候，你把第一次二次可以复用的代码进行了封装
            #往复下来你就形成了一个框架
            #框架就是指将一类共性的项目的共性的功能写成一个可以方便复用的大的功能块儿

        #分析
            #分析http请求
            #分析HTML了请求
            #分析js、ajax请求
                #Firefox
                    #开发者工具
                    #firebug
                    #httpfox
                    #分析抓包
        #请求和响应部分
            #爬虫模块
            #urllib
            #urllib2
            #requests

            #httplib
            #cookielib
            #hashlib
        #数据筛选
            #匹配模块
            #re
            #lxml xpath
            #beautifulsoup bs4
        #数据存储
            #mysql
            #file #file 日志记录
            
#周末实战
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


















