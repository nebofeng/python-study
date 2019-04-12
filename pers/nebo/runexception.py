#! /bin/python
#coding=utf-8
'''
version: 0.1
author: fnb
date:20190412
use: 在任务执行过程中，对配置的节点执行各种异常操作。监控任务执行的结果
逻辑：输出需要执行的任务，需要制造的异常 （v0.1为关闭杀死进程）

threadtask 执行任务
threadexception 制造

需要传入高可用节点的

'''

import threading
import time
import paramiko


class TaskThread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        end_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        while(int(end_time)-int(now_time)<10):
            print("Starting " + self.name)
            end_time =time.strftime("%Y%m%d%H%M%S", time.localtime())
            print("Exiting " + self.name)

class ExceptionThread(threading.Thread):  # 继承父类threading.Thread

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        while(thread1.is_alive()):
            print("Starting " + self.name)

            print("Exiting " + self.name)



#制造的异常种类  k v, key为异常名， v为构建异常的脚本执行路径
def exceptionlist():
    import threading
    import time
    exitFlag = 0

def getSsh(hostname,usename,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=22, username=usename, password=password)
    return ssh



if __name__ == "__main__":

    node1=getSsh("","","")
    node2=getSsh("","","")

    cmd = 'ps'
    # cmd = 'ls -l;ifconfig'       #多个命令用;隔开
    stdin, stdout, stderr = ssh.exec_command(cmd)
    result = stdout.read()

    if not result:
        result = stderr.read()

    # 创建新线程
    thread1 = TaskThread(1, "Thread-task", 1)
    thread2 = ExceptionThread(2, "Thread-exeption", 2)

    # 开启线程
    thread1.start()
    print("thread start")
    if(thread1.is_alive()):
        thread2.start()
