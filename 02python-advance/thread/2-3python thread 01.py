#coding:gbk
#python 多线程
from time import ctime,sleep
import thread #_thread
"""
control_list = [4,2]
def loop(ids,num):
    print("loop %s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop %s is done at:%s"%(ids,ctime()))

def main():
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        thread.start_new_thread(loop,(ids,num))#创建并且开始一个线程
    sleep(4)
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()

import threading

control_list = [4,2]
def loop(ids,num):
    print("loop %s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop %s is done at:%s"%(ids,ctime()))

def main():
    thread_list = []
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        t = threading.Thread(target = loop,args = (ids,num)) #创建一个线程
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#开始执行线程
    for t in thread_list:
        t.join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()

def myfun(name="",age="",gender=""):
    print(name)
    print(age)
    print(gender)

myfun(name="while",gender="nan")



import threading

control_list = [4,6]
#control_list = [4,2]
def loop(ids,num):
    print("loop %s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop %s is done at:%s"%(ids,ctime()))

def main():
    thread_list = []
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        t = threading.Thread(target = loop,args = (ids,num)) #创建一个线程
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#开始执行线程
    thread_list[0].join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()


import threading

control_list = [4,2]
def loop(ids,num):
    print("loop %s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop %s is done at:%s"%(ids,ctime()))

def main():
    thread_list = []
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        t = threading.Thread(target = loop,args = (ids,num)) #创建一个线程
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#开始执行线程
    for t in thread_list:
        t.join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()
"""

#已疯:4
#man8:2

#教室:1
#已疯和man8同学都没写完作业被关到了教室里

#已疯:我写完作业，你再关门(4) 已疯.join()
#man8:我写完作业，你再关门(2）man8.join
#2秒之后man8走了
#还有2秒已疯才写完
#教室关门:4
    
#已疯:我写完作业，你再关门(4) 
#man8:2

#还有4秒已疯才写完
#教室关门:4    

#循环
    #for i in [已疯，man8]:
        #两人开始写作业 i.start() 
    #for i in [已疯，man8]:
        #i.join()
            #已疯:我写完作业，你再关门(4) 已疯.join()
            #man8:我写完作业，你再关门(2）man8.join
#2秒之后man8走了
#还有2秒已疯才写完
#教室关门:4
"""
import threading

class MyThread(threading.Thread):
    pass

control_list = [4,2]
def loop(ids,num):
    print("loop %s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop %s is done at:%s"%(ids,ctime()))

def main():
    thread_list = []
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        t = MyThread(target = loop,args = (ids,num))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()

control_list = [4,2]
import threading

class MyThread(threading.Thread):
    def __init__(self,ids,num):
        self.ids = ids
        self.num = num
        threading.Thread.__init__(self)
    def run(self):
        print("loop %s is start at:%s"%(self.ids,ctime()))
        sleep(self.num)
        print("loop %s is done at:%s"%(self.ids,ctime()))
        
def main():
    thread_list = []
    print("all is start at: %s"%ctime())
    for ids,num in enumerate(control_list):
        t = MyThread(ids,num)
        #t = threading.Thread(target = loop,args = (ids,num))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()

import threading

def myfun():
    print("start myfun")
    sleep(2)
    print("end fun")

print("main thread")
t = threading.Thread(target=myfun,args=())
t.start()
sleep(2)
print("main thread end")


#这个例子有问题，需要从写
import threading

def myfun(ids):
    print("start myfun %s"%ids)
    sleep(2)
    print("end fun %s"%ids)

t_list = []
print("main thread")
for i in range(10):
    t = threading.Thread(target=myfun,args=(i,))
    t.setName("thread-%s"%i)
    t_list.append(t)
    
print(t_list)
print(t_list[-2])
print(t_list[-2].isDaemon())
t_list[-2].setDaemon(True) #将一个线程设置为守护线程，进程检查到只有该线程没有执行完成
                            #进程就会结束，也就说告诉进程该线程不重要
print(t_list[-2].isDaemon())
                            
for t in t_list:
    t.start()
sleep(2)
print("main thread end")
""" 
#lock #全局解释器锁
    #为了保证python虚拟机当中在同一时间点上只有一个事件在执行而设置的
    #加锁以后的线程不可以被抢占
    #man8 1--> 8 电梯加锁
    #while 2 --> 8 电梯不停
#thread
    #allocate_lock #生成锁
        #<thread.lock object at 0x0214A140>
            #acquire #获取锁
            #release #释放锁
            #locked #判断是否加锁

        

#print(thread.allocate_lock())


#print(help(thread))
#多线程内部执行的顺序不定，假如说
#我们的程序当中有全局变量，那么修改的顺序将不是我们的期望的
"""
import threading
num = 1
def change_it(n):
    global num
    num += 1
    num -= 1
    print(num)
def main(n):
    for i in range(100):
        change_it(n)

t1 = threading.Thread(target=main,args=(5,))
t2 = threading.Thread(target=main,args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()
"""

import threading
num = 1
lock = thread.allocate_lock()#生成了锁

def change_it():
    global num
    num += 1
    num -= 1
    print(num)
def main():
    for i in range(100):
        lock.acquire() #获取锁
        try:
            change_it()
        except:
            pass
        finally:
            lock.release() #释放锁

t1 = threading.Thread(target=main,args=())
t2 = threading.Thread(target=main,args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(num)


print(num)

#并发
#抢占


"""
import threading
num = 1
def change_it():
    global num
    num += 1
    num -= 1
    print(num,"hello")
def main():
    for i in range(100):
        change_it()

t1 = threading.Thread(target=main,args=())
t2 = threading.Thread(target=main,args=())

t1.start()
t2.start()

t1.join()
t2.join()
"""

















































