#!/usr/bin/python
#coding:gbk

#python ��ά
    #���
        #����
            #����Ҫ�����ݽ��б���
            #�Ա��ݵ����ݽ��м��
        #���
            #ϵͳ���صļ��
                #top չʾ������Դռ��
                #uptime �����û���Դռ��״��
            #cpuʹ���ʼ��
                #top չʾcpuʹ��״��
            #�ڴ�ռ�õļ��
                #free �鿴�ڴ��С
                #vmstat �鿴�ڴ��С��
            #���̿ռ���
                #df -h �鿴���̴�С
            #�˿ڵļ��
                #w �鿴��¼�û�
            #���̵ļ��
                #ps -ef �鿴����
        #ͳ�ƺͷ����������
            #д����
    
        #�Զ�����ά
            #python д�ű�
            #ͼ�λ� web
                #server �����
                    #client1�û��� client2
                    #�鿴client����
                #ͨ��server��clientִ������
                    #ssh Զ�̿���
            #/proc

        #��ά�õ���ģ��
            #configparser �����ļ�ģ��
                #read()
                #sections()
                #options()
                #items()
                #get()
            #paramiko python sshԶ�̵�¼

#title_list = re.findall("^\[(.*)\]",content,re.M)
#ƥ��ǰ���'['��߼�']'��.*(����ǻ����ַ����)
#title_list = re.findall("^\[.*\]",content,re.M)
#ƥ��ǰ���'['.*(����ǻ����ַ����)��߼�']'
#"b��man8"
#"b��(man8)"
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

client = paramiko.SSHClient() #ʵ����һ��sshԶ�̵�¼����
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #��ֹû����Կ�����
client.connect(
    "192.168.0.204", #host ssh��Զ������ip
    22, #port �˿�
    username="root", # user �û���
    password="password", # password ����
    timeout=1 # timeout���ӳ�ʱ
    )
ins,out,err = client.exec_command("ls")#ִ�����������������stdin,stddout,stderr��
for i in out.readlines():
    print(i)
client.close() #�ر�����
"""
#send_mail
#python �����ʼ���ģ��



import os
# �������read �ᱨ�� linux����Ĵ���
# <open file 'ls', mode 'r' at 0x7f4a8de185d0>ls: write error: Broken pipe
#print (os.popen("ls"))
result=os.popen("ls")
print (result)
sleep(1)
#sleep  1 s ���ᱨ��


print (result.read())
























