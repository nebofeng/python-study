#coding:utf-8
#python 运维需求
'''
需求： 利用python实现自动监控服务器性能


python相关知识
1.流程控制
2.面向对象及面向过程开发。


主要模块：
os
sys


'''
import os
print("===")
print(os.getcwd())


'''
 #监控
 # 备份
 #对备份内容进行校验
 
 #监控
  系统负载监控
    top
    uptime 在线用户的资源占用情况
  cpu使用率监控
    top 展示cpu使用状况
  内存占用监控
    free  查看内存大小
    vmstat 查看内存大小的
   磁盘空间大小
    df -h 查看磁盘大小
   端口的监控
    w 查看登录用户
    进程的监控
     ps -ef
      
   统计和分析监控数据
      写报告
    自动化运维
      python 脚本
      
      图形化 web
        server服务器
          client客户端
          
          通过server让client执行命令
          
      proc
      
      运维用到的模块
       Config
       
       f=open("","r")
       
       print()
       f.close()   
     
     ConfigParser 模块
     
 
'''

result = os.popen("dir")
for i in result.readlines():
        print(i)

        #print(result)
