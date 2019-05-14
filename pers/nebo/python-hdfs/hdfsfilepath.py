#! /bin/python
#coding=utf-8
'''
根据文件名获取blocks 在linux上的location
需要传递的参数：
文件/文件夹 路径
每个节点存放hdfs数据的目录： TODO: 改为配置文件读取，或是直接读取hdfs的配置文件。


'''

import  os
hdfsfilename="/tmp/256Mfile0"
hdfsfindcmd="sudo -u hdfs  hdfs fsck  {}  -files -blocks -locations".format(hdfsfilename)

result=os.popen(hdfsfindcmd).read()
resultarr=result.split("\n")

'''
从第二行开始，每一行都是一个blockid 以及三个备份节点
思路：
远程执行命令并返回：

关系的参数： block个数 ，每个block 的备份个数，以及备份的节点，所在磁盘目录

'''
for i in range(len(resultarr)):
    print ("第 {} 行: {} ".format(i,resultarr[i]))


#localget cmd 后面可以优化为多线程
localdatadir="/home/hadoop"

blkid=""
localgetcmd="find {}  ".format(localdatadir,blkid)





