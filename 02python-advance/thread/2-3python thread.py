#coding:gbk

#python ���߳�
    #����:�ǳ����һ������ process
    #�߳�:�ǽ��̵��еķ�֧

#import os
#print(os.getpid())#���ؽ��̺�
    
#�Զ��̵߳�����
    #1��������ǳ��������Ч��
    #2��׷�󲢷�

#��������ʹ�õļ�����󲿷ֶ��ǵ�cpu�ļ������
#��CPU�������һ��ʱ����ϣ�ֻ�ܴ���һ������

#python �����������:python �������ģ�ⵥcpu��������еĹ��̽���python���������
#����python �������������ͬһ��ʱ����ϣ�ֻ����һ������
#���������Ĳ�����python���в������ڣ����ǲ�ȡ����ʱ��Ƭ����ʽ���첽����
#Ϊ�˱�֤�������ԣ�������ȫ�ֽ��������ĸ���:��һ���¼����б������Ժ��ڸ��¼�������
#�ͷ�֮ǰ�������¼��޷���ϸ��¼������С�

#A A1 A2 A3
#B B1 B2
#A1 B1 A2 A3 B2

#�Զ��� �� ��
#��һ��ʱ����ϣ���׽���ʳ��ֻ������һ��
#�����Ͳ˶���ڶ���Ȼ���
#��ʵ��һ��ʱ����ϣ���׽���ʳ��ֻ������һ��
#����������������

#���߳�:�߳��ǽ����µķ�֧�����߳���ﵽһ�������µļ�����֧ͬʱ���е�Ч��
#�����:�����ǳ����һ�����У������ͬʱ���ж�����������

#���̶����Լ��������ڴ�ռ䣬����֮��������ݵ�ͨ�Ų��Ǻܷ���
#ͬһ�������µ��̹߳���ý��̵��ڴ�ռ䣬�������ݽ����ȽϷ��㣬
#����Ҳ���׵���ȫ�ֱ�����Ī���޸�

#���̵߳ļ�������
    #ָ�� ÿ���̶߳�������ָ��ָ�����߳�ִ�еĻ�����˳��ִ�У�������
    #�ж� �߳������еĹ����б���ռ���ж�
    #���� �߳����еĹ��̵��й��𣬽�������
    #�ò� һ���߳��������߳��Ƚ�������

#���д��������ǽ���
    #ÿ�����ھ����߳� �����̼߳����ݵĽ���Ҫ�Ƚ��̼䷽��
    #ÿ�����ڰ���ҵ���ʱ�򶼻����ź�(˳��),����ִ�У�,����(����)�ı�ʶ
    #������������vip�û������λ�ÿ��ܱ���ռ
    #�����£����ߵ����Ȱ����������
    #����һ��̫̫�Ȱ������ò�


#python ���̵߳�ģ��
    #2.x
        #thread
        #threading
    #3.x
        #_thread
        #threading
    
#thread(_thread) ��python ���̵߳ײ��һ��ģ�顣threadingʵ�����Ƕ�
#thread��һ���ٷ�װ��thread(_thread)��֧���ػ��̡߳����ҰѺö�ײ�ķ�����¶����
#�������ٷ�װ��threading���ӷ���ʹ�ã�����֧���ػ��߳�
#�ػ��߳�:
    #��ʬ����:�����̱�ִ������Ժ�,�ڴ�û���ͷ� kill
    #����������һ�����̣����̽������߳�û�н�����ʱ��
        #1�����̹رգ��̱߳�ǿ�ƹر�
        #2�����̹رգ��߳���Ȼռ���ڴ�������У�û�йرգ�
        #���߳�ִ������Ժ�û�з������ߴ�ʩ�����ڴ��ͷ�
        #�γ��˽�ʬ����
    #���������ʱ�����ǻᰲ��һ���߳���Ϊ�ػ��̣߳��ػ��̻߳������ִ��
    #����ػ��߳�û��ִ�У����̲����Թر�
"""

from time import sleep,ctime
    #sleep ����ָ��ʱ��
    #ctime ���ص�ǰʱ����ַ�����ʽ��ʱ��
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

#__name__ ��python��һ�����÷�������ӵ������ֵ����
    #���ű��Լ�ִ�е�ʱ��__name__ ��ֵ�� ��__main__
    #���ű�������ִ�е�ʱ��__name__ ��ֵ��ģ������
if __name__ == "__main__":#ͨ��������������ж�������
    #���ǵĽ����ǵ���main����
        #�����ں���������������֧
            #loop0
            #loop1
    main()

"""
#import thread #3.x _thread
import _thread
from time import sleep,ctime
    #sleep ����ָ��ʱ��
    #ctime ���ص�ǰʱ����ַ�����ʽ��ʱ��
    #thread.start_new_thread ����һ���߳�
        #��һ���������߳�Ҫ���õĹ��ܻ��ߺ���
        #�ڶ��������Ǳ����õĹ��ܻ��ߺ�����Ҫ�Ĳ���������û�в�����д��Ԫ��
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
#threading �̳���д��thread,֧���ػ��߳�
    #threading ͨ���Լ��������Thread���������߳�
    #���Ҹ������� start���������̣߳�join���������߳�
    #getName ��ȡ�̵߳�����
    #setName �����̵߳�����
    #isAlive �ж��̵߳�״̬
    #isDaemon �����߳�daemon�ı�׼ 
    #setDaemon ����daemon�ı�׼

    #����daemonһ��Ҫ�ڶ��߳�����֮ǰ

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
        #threading.Thread ͨ���÷��������߳�
            #target ָ�����õĺ���
            #args ָ������
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
    thread_list = [] #����һ���յ��б�
    
    print("main is start at:%s"%ctime()) #��ӡһ�仰
    
    for ids,num in enumerate(c_list): #��c_list��ö�ٽ���ѭ��
        t = threading.Thread(target = loop,args = (ids,num)) #����ѭ��������ֵ�����߳�
        
        thread_list.append(t)#���߳���ӵ�������б���
        
    for t in thread_list: #ѭ�����̣߳����ҿ�ʼ����
        t.start()
        
    for t in thread_list: #����Щ��ʼ���̹߳������
        t.join()
    print("main is done at:%s"%ctime()) #��ӡһ�仰

if __name__ == "__main__":
    main(a_list)


#1��lock
#2�����������߳�











































    















