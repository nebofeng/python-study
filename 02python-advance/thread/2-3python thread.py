#coding:gbk

#python 多线程
    #进程:是程序的一次运行 process
    #线程:是进程当中的分支

#import os
#print(os.getpid())#返回进程号
    
#对多线程的需求
    #1、提高我们程序的运行效率
    #2、追求并发

#我们现在使用的计算机大部分都是单cpu的计算机，
#单CPU计算机在一个时间点上，只能处理一个任务。

#python 的虚拟机概念:python 虚拟机在模拟单cpu计算机运行的过程进行python代码的运行
#所以python 的虚拟机决定在同一个时间点上，只处理一个任务
#所以真正的并发在python当中并不存在，我们采取的是时间片的形式的异步并发
#为了保证以上特性，采用了全局解释器锁的概念:当一个事件运行被加锁以后，在该事件的锁被
#释放之前，其他事件无法打断该事件的运行。

#A A1 A2 A3
#B B1 B2
#A1 B1 A2 A3 B2

#吃东西 肉 菜
#在一个时间点上，你咀嚼的食物只可能是一种
#你把肉和菜剁成馅儿，然后吃
#其实在一个时间点上，你咀嚼的食物只可能是一种
#错觉是你吃了猪肉大葱

#多线程:线程是进程下的分支，多线程想达到一个进程下的几个分支同时进行的效果
#多进程:进程是程序的一次运行，多进程同时进行多个程序的运行

#进程都有自己独立的内存空间，进程之间进行数据的通信不是很方便
#同一个进程下的线程共享该进程的内存空间，所以数据交互比较方便，
#但是也容易导致全局变量的莫名修改

#多线程的几个概念
    #指针 每个线程都必须有指针指出该线程执行的环境（顺序，执行，结束）
    #中断 线程在运行的过程中被抢占，中断
    #休眠 线程运行的过程当中挂起，叫做休眠
    #让步 一个线程让其他线程先进行运行

#银行储蓄所就是进程
    #每个窗口就是线程 所以线程间数据的交互要比进程间方便
    #每个窗口办理业务的时候都会有排号(顺序),办理（执行）,结束(结束)的标识
    #假如你遇到了vip用户，你的位置可能被抢占
    #你有事，你后边的人先办理，你叫休眠
    #你让一老太太先办理，叫让步


#python 多线程的模块
    #2.x
        #thread
        #threading
    #3.x
        #_thread
        #threading
    
#thread(_thread) 是python 多线程底层的一个模块。threading实际上是对
#thread的一个再封装，thread(_thread)不支持守护线程。并且把好多底层的方法暴露出来
#而经过再封装的threading更加方便使用，并且支持守护线程
#守护线程:
    #僵尸进程:当进程被执行完成以后,内存没有释放 kill
    #当我们运行一个进程，进程结束，线程没有结束的时候，
        #1、进程关闭，线程被强制关闭
        #2、进程关闭，线程依然占用内存进行运行，没有关闭，
        #当线程执行完成以后，没有方法或者措施进行内存释放
        #形成了僵尸进程
    #所以在这个时候我们会安排一个线程作为守护线程，守护线程会在最后被执行
    #如果守护线程没有执行，进程不可以关闭
"""

from time import sleep,ctime
    #sleep 休眠指定时间
    #ctime 返回当前时间的字符串格式的时间
def loop0():
    print("loop0 is start at %s"%ctime())
    sleep(4)
    print("loop0 is done at %s"%ctime())

def loop1():    
    print("loop1 is start at %s"%ctime())
    sleep(2)
    print("loop1 is done at %s"%ctime())

def main():
    print("main is start %s"%ctime())
    loop0()
    loop1()
    print("main_done at %s"%ctime())

#__name__ 是python的一个内置方法，他拥有两个值，，
    #当脚本自己执行的时候，__name__ 的值是 “__main__
    #当脚本被调用执行的时候，__name__ 的值是模块名称
if __name__ == "__main__":#通常我们在用这个判断做调试
    #我们的进程是调用main函数
        #但是在函数当中有两个分支
            #loop0
            #loop1
    main()

"""
#import thread #3.x _thread
import _thread
from time import sleep,ctime
    #sleep 休眠指定时间
    #ctime 返回当前时间的字符串格式的时间
    #thread.start_new_thread 创建一个线程
        #第一个参数是线程要调用的功能或者函数
        #第二个参数是被调用的功能或者函数需要的参数，若果没有参数，写空元组
"""
def loop0():
    print("loop0 is start at %s"%ctime())
    sleep(4)
    print("loop0 is done at %s"%ctime())

def loop1():    
    print("loop1 is start at %s"%ctime())
    sleep(2)
    print("loop1 is done at %s"%ctime())

def main():
    print("main is start %s"%ctime())
    thread.start_new_thread(loop0,()) 
    thread.start_new_thread(loop1,())
    print("main_done at %s"%ctime())

if __name__ == "__main__":
    main()


a_list = [4,2]
def loop(ids,num):
    print("loop%s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop%s is done at:%s"%(ids,ctime()))

def main(c_list):
    print("main is start at:%s"%ctime())
    for ids,num in enumerate(c_list):
        loop(ids,num)
    print("main is done at:%s"%ctime())

if __name__ == "__main__":
    main(a_list)

a_list = [4,2]
def loop(ids,num):
    print("loop%s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop%s is done at:%s"%(ids,ctime()))

def main(c_list):
    print("main is start at:%s"%ctime())
    for ids,num in enumerate(c_list):
        thread.start_new_thread(loop,(ids,num))
    sleep(4)
    print("main is done at:%s"%ctime())

if __name__ == "__main__":
    main(a_list)

#threading
#threading 继承重写了thread,支持守护线程
    #threading 通过自己的下面的Thread方法创建线程
    #并且给出方法 start用来开启线程，join用来挂起线程
    #getName 获取线程的名称
    #setName 设置线程的名称
    #isAlive 判断线程的状态
    #isDaemon 返回线程daemon的标准 
    #setDaemon 设置daemon的标准

    #设置daemon一定要在多线程运行之前

import threading

a_list = [4,2]
def loop(ids,num):
    print("loop%s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop%s is done at:%s"%(ids,ctime()))

def main(c_list):
    thread_list = []
    print("main is start at:%s"%ctime())
    for ids,num in enumerate(c_list):
        t = threading.Thread(target = loop,args = (ids,num))
        #threading.Thread 通过该方法创建线程
            #target 指定调用的函数
            #args 指定参数
        t.setName("while-%s"%ids)
        print(t)
        print(t.getName())
        thread_list.append(t)
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()
    print("main is done at:%s"%ctime())

if __name__ == "__main__":
    main(a_list)

"""
import threading

a_list = [4,6]
def loop(ids,num):
    print("loop%s is start at:%s"%(ids,ctime()))
    sleep(num)
    print("loop%s is done at:%s"%(ids,ctime()))

def main(c_list):
    thread_list = [] #创建一个空的列表
    
    print("main is start at:%s"%ctime()) #打印一句话
    
    for ids,num in enumerate(c_list): #对c_list的枚举进行循环
        t = threading.Thread(target = loop,args = (ids,num)) #利用循环出来的值生成线程
        
        thread_list.append(t)#将线程添加到上面的列表里
        
    for t in thread_list: #循环出线程，并且开始他们
        t.start()
        
    for t in thread_list: #将这些开始的线程挂起到最后
        t.join()
    print("main is done at:%s"%ctime()) #打印一句话

if __name__ == "__main__":
    main(a_list)


#1、lock
#2、面向对象多线程











































    















