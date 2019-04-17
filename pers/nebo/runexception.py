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
import os
import random
import commands

def getSsh(hostname,usename,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=hostname, port=22, username=usename, password=password)
    return ssh


def kill_process_by_name(name):
    cmd = "ps -e | grep %s" %name
    f=os.popen(cmd)
    txt = f.readlines()
    if len(txt) == 0:
        print("no process \"%s\"!!" % name)
        return
    else:
       for line in txt:
           colum = line.split()
           pid = colum[0]
           cmd = "kill -9 %d" % int(pid)
           rc = os.system(cmd)
           if rc == 0 :
               print("exec \"%s\" success!!" % cmd)
           else:
               print("exec \"%s\" failed!!" % cmd)

    return

def  localCmd(cmd):
    stdin, stdout, stderr = os.popen(cmd)
    os.popen(cmd)
    result = stdout.read()
    if not result:
        result = stderr.read()  # 读取错误信息
    return result

def sshCmd(node,cmd):
    stdin, stdout, stderr = os.open(cmd)
    result = stdout.read()
    if not result:
        list[0] = node
        result = stderr.read()  # 读取错误信息
        list[1] = result
        # log write
    else:
        list[0] = node
        list[1] = result
    return list

def  checkStatus():
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    dict = {'node1': 'acvite', 'node3': 'standby'}
    node1=""
    node2=""
    #首先判断 rm1 rm2 状态 转为本地操作 node3 rm2   node1  rm1
    rm1status_cmd="sudo -u yarn yarn rmadmin -getServiceState rm1 "
    rm2status_cmd = "sudo -u yarn yarn rmadmin -getServiceState rm2 "
    #本节点执行 查询状态
    node1_status = localCmd(rm1status_cmd)
    node3_status = localCmd(rm1status_cmd)
    flag = True
    if node1_status == "active":
        dict['node1'] = "acvite"
        if node3_status == "active":
            print(now_time,"error  both active")
            flag = False
        elif node3_status == "standby":
            print(now_time,"node1 ac   node3 standy")
            dict['node3'] = "standby"
        else:
            print(now_time,"node1 ac node3 stop")
            dict['node3'] = "stop"
    elif node1_status == "standby":
        dict['node1'] == "standby"
        if node3_status == "acvite":
            print(now_time,"node1 standby node3 active")
        elif node3_status == "standby":
            print(now_time,"node1 node 3 both standby : Error")
            flag = False
        else:
            print(now_time,"node1 standby node3 stop : Error")
            flag = False
    else:
        dict['node1'] = "stop"
        if node3_status == "acvite":
            print(now_time,"node1 stop node3 active")
        elif node3_status == "standby":
            print(now_time,"node1 stop node3 standby :Error")
            flag = False
        else:
            print(now_time,"node1 stop node2 stop: Error")
            flag = False
    return  dict,flag

#开启服务
def start():

    return

#关闭服务
def stop(node,service):
    cmd_find="jps -ml | grep %s " %service
    stdin, stdout, stderr=node.exec_command(cmd_find)
    pid=stdout.read
    cmd_kill="kill -9 %s" %pid
    node.exec_command(cmd_kill)
    return

if __name__ == "__main__":
    node1=getSsh("","","")
    node3=getSsh("","","")
    stopInfo="Connection refused"
    #
    dict = {'node1': ' ', 'node3': ' '}
    dict,flag=checkStatus()
    while(flag):
        #关闭

        #随机休眠
        sleeptime = random.randint(0, 300)
        time.sleep(sleeptime)
        if dict['node1']=="active":
            if dict['node3']=="standby":
                print("这里关闭node1")
                stop(node1,"ResourceManager")
                #node1.exec_command()
            elif dict['node3']=="stop":
                print("这里等待 node3重启")
                dict,flag=checkStatus()
                node3.exec_command("")
        elif dict['node1']=='standby':
                print("这里关闭node3")
                stop(node3,"ResourceManager")
                dict, flag = checkStatus()

        else:
            print("这里等待node1重启")






