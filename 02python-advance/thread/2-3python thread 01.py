#coding:gbk
#python ���߳�
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
        thread.start_new_thread(loop,(ids,num))#�������ҿ�ʼһ���߳�
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
        t = threading.Thread(target = loop,args = (ids,num)) #����һ���߳�
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#��ʼִ���߳�
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
        t = threading.Thread(target = loop,args = (ids,num)) #����һ���߳�
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#��ʼִ���߳�
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
        t = threading.Thread(target = loop,args = (ids,num)) #����һ���߳�
        #t.start() 
        thread_list.append(t)
    #print(thread_list)
    for t in thread_list:
        t.start()#��ʼִ���߳�
    for t in thread_list:
        t.join()
    print("all is done at: %s"%ctime())
    
if __name__ == "__main__":
    main()
"""

#�ѷ�:4
#man8:2

#����:1
#�ѷ��man8ͬѧ��ûд����ҵ���ص��˽�����

#�ѷ�:��д����ҵ�����ٹ���(4) �ѷ�.join()
#man8:��д����ҵ�����ٹ���(2��man8.join
#2��֮��man8����
#����2���ѷ��д��
#���ҹ���:4
    
#�ѷ�:��д����ҵ�����ٹ���(4) 
#man8:2

#����4���ѷ��д��
#���ҹ���:4    

#ѭ��
    #for i in [�ѷ裬man8]:
        #���˿�ʼд��ҵ i.start() 
    #for i in [�ѷ裬man8]:
        #i.join()
            #�ѷ�:��д����ҵ�����ٹ���(4) �ѷ�.join()
            #man8:��д����ҵ�����ٹ���(2��man8.join
#2��֮��man8����
#����2���ѷ��д��
#���ҹ���:4
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


#������������⣬��Ҫ��д
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
t_list[-2].setDaemon(True) #��һ���߳�����Ϊ�ػ��̣߳����̼�鵽ֻ�и��߳�û��ִ�����
                            #���̾ͻ������Ҳ��˵���߽��̸��̲߳���Ҫ
print(t_list[-2].isDaemon())
                            
for t in t_list:
    t.start()
sleep(2)
print("main thread end")
""" 
#lock #ȫ�ֽ�������
    #Ϊ�˱�֤python�����������ͬһʱ�����ֻ��һ���¼���ִ�ж����õ�
    #�����Ժ���̲߳����Ա���ռ
    #man8 1--> 8 ���ݼ���
    #while 2 --> 8 ���ݲ�ͣ
#thread
    #allocate_lock #������
        #<thread.lock object at 0x0214A140>
            #acquire #��ȡ��
            #release #�ͷ���
            #locked #�ж��Ƿ����

        

#print(thread.allocate_lock())


#print(help(thread))
#���߳��ڲ�ִ�е�˳�򲻶�������˵
#���ǵĳ�������ȫ�ֱ�������ô�޸ĵ�˳�򽫲������ǵ�������
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
lock = thread.allocate_lock()#��������

def change_it():
    global num
    num += 1
    num -= 1
    print(num)
def main():
    for i in range(100):
        lock.acquire() #��ȡ��
        try:
            change_it()
        except:
            pass
        finally:
            lock.release() #�ͷ���

t1 = threading.Thread(target=main,args=())
t2 = threading.Thread(target=main,args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(num)


print(num)

#����
#��ռ


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

















































