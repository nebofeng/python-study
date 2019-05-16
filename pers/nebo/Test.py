#coding=utf-8
import ssl
import random


for i in range(100):
    sleeptime=random.randint(0, 3)
    a = random.uniform(0, 1)
    print(sleeptime)
    print(a)

#! /bin/python
#coding=utf-8
import threading
import  time


def fun1(t):
    print(t.isAlive)


def fun2():
    for i in range(10):
        print("function 2 {}".format(i))


def worker():
    print("worker")
    time.sleep(1)
    return


# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.start()
if __name__ == '__main__':
     t2=threading.Thread(target=fun2)
     t1=threading.Thread(target=fun1,args=(t2,))

     t1.start()
     t2.start()
     print (t2.isAlive())


