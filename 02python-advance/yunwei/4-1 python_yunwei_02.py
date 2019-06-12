#!/usr/bin/python
#coding:gbk

#python 运维
    #监控
        #备份
            #对需要的数据进行备份
            #对备份的内容进行检查
        #监控
            #系统负载的监控
                #top 展示进程资源占用
                #uptime 在线用户资源占用状况
            #cpu使用率监控
                #top 展示cpu使用状况
            #内存占用的监控
                #free 查看内存大小
                #vmstat 查看内存大小的
            #磁盘空间监控
                #df -h 查看磁盘大小
            #端口的监控
                #w 查看登录用户
            #进程的监控
                #ps -ef 查看进程
        #统计和分析监控数据
            #写报告
    
        #自动化运维
            #python 写脚本
            #图形化 web
                #server 服务端
                    #client1用户端 client2
                    #查看client属性
                #通过server让client执行命令
                    #ssh 远程控制
            #/proc

        #运维用到的模块
            #configparser 配置文件模块
                #read()
                #sections()
                #options()
                #items()
                #get()
            #paramiko python ssh远程登录

#title_list = re.findall("^\[(.*)\]",content,re.M)
#匹配前面加'['后边加']'的.*(任意非换行字符多次)
#title_list = re.findall("^\[.*\]",content,re.M)
#匹配前面加'['.*(任意非换行字符多次)后边加']'
#"b组man8"
#"b组(man8)"
import re

example = "hello world this is 2013"
"""
print(re.findall("\w\w",example))
print(re.findall("\w(\w)",example))
print(re.findall("(\w)\w",example))
print(re.findall("(\w)(\w)",example))

print(re.findall(".*",example))
print(re.findall(".*?",example))
print(re.findall("(.*)?",example))
"""
example = """
hello
world
"""
#print(re.findall(r"^\w",example))
#print(re.findall(r"^\w",example,re.M))


import os
from time import sleep

#result = os.popen("top")
#for i in result.readlines():
#       print(i)
#print(result.read())
#while True:
#       print(result.readline())
#sleep(1)


#f = open("/proc/cpuinfo")
#print(f.read())
#f.close()
"""
content = f.read()
print(content)
f.close()

f = os.popen("cat mycofig.cfg")
print(f.read())
print(f.read())
f = os.popen("cat mycofig.cfg")
print(f.read())

import ConfigParser as cfg

f = cfg.ConfigParser()
f.read("mycofig.cfg")
#print(f.read("mycofig.cfg"))
f = cfg.ConfigParser()
f.read("mycofig.cfg")
#print(f.read("mycofig.cfg"))
print(f.sections()) 
#print(f.options("eth0"))
#print(f.items("eth0"))
#print(f.get("eth0","netmask"))

import re
content = os.popen("cat mycofig.cfg").read()
print(content)
f.read("mycofig.cfg")
#print(f.read("mycofig.cfg"))
print(f.sections())
print(f.options("eth0"))
print(dict(f.items("eth0")))
print(f.get("eth0","netmask"))


import re
content = os.popen("cat mycofig.cfg").read()
title_list = re.findall("^\[(.*)\]",content,re.M)
title_list = re.findall("^\[.*\]",content,re.M)
print(title_list)  

import paramiko

client = paramiko.SSHClient() #实例化一个ssh远程登录对象
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #防止没有秘钥的情况
client.connect(
    "192.168.0.204", #host ssh的远程主机ip
    22, #port 端口
    username="root", # user 用户名
    password="password", # password 密码
    timeout=1 # timeout连接超时
    )
ins,out,err = client.exec_command("ls")#执行命令，返回三个量（stdin,stddout,stderr）
for i in out.readlines():
    print(i)
client.close() #关闭链接
"""
#send_mail
#python 发送邮件的模块



import os
# 如果不加read 会报错 linux自身的错误，
# <open file 'ls', mode 'r' at 0x7f4a8de185d0>ls: write error: Broken pipe
#print (os.popen("ls"))
result=os.popen("ls")
print (result)
sleep(1)
#sleep  1 s 不会报错。


print (result.read())
























