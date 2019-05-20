#! /bin/python
#coding=utf-8
import re
'''
根据文件名获取blocks 在linux上的location
需要传递的参数：
文件/文件夹 路径
每个节点存放hdfs数据的目录： TODO: 改为配置文件读取，或是直接读取hdfs的配置文件。

单个文件info:

FSCK started by hdfs (auth:SIMPLE) from /28.28.33.73 for path /user/hbase/kill1 at Wed May 15 09:59:12 CST 2019
/user/hbase/kill1 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782666_42424 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-59b0f40d-bacc-4540-85d8-38d4e7ec5c59,DISK], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]

Status: HEALTHY
 Number of data-nodes:	5
 Number of racks:		2
 Total dirs:			0
 Total symlinks:		0

Replicated Blocks:
 Total size:	118 B
 Total files:	1
 Total blocks (validated):	1 (avg. block size 118 B)
 Minimally replicated blocks:	1 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	3
 Average block replication:	3.0
 Missing blocks:		0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)

Erasure Coded Block Groups:
 Total size:	0 B
 Total files:	0
 Total block groups (validated):	0
 Minimally erasure-coded block groups:	0
 Over-erasure-coded block groups:	0
 Under-erasure-coded block groups:	0
 Unsatisfactory placement block groups:	0
 Average block group size:	0.0
 Missing block groups:		0
 Corrupt block groups:		0
 Missing internal blocks:	0
FSCK ended at Wed May 15 09:59:12 CST 2019 in 0 milliseconds

The filesystem under path '/user/hbase/kill1' is HEALTHY



第 0 行: FSCK started by hdfs (auth:SIMPLE) from /28.28.33.73 for path /user/hbase at Wed May 15 10:00:06 CST 2019
/user/hbase <dir>
/user/hbase/128Mfile 134217728 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782655_42413 len=134217728 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.74:50010,DS-59b0f40d-bacc-4540-85d8-38d4e7ec5c59,DISK], DatanodeInfoWithStorage[28.28.33.73:50010,DS-60fa715b-af81-44c5-83d1-733aaf911726,DISK], DatanodeInfoWithStorage[28.28.33.76:50010,DS-6ad7802b-4a8b-4bcd-b4f2-2bba99a62b10,DISK]]
第 1 行: /user/hbase/kill.sh 118 bytes, replicated: replication=3, 1 block(s):  Replica placement policy is violated for BP-540626610-10.58.33.81-1552889464019:blk_1073782663_42421. Block should be additionally replicated on 2 more rack(s). Total number of racks in the cluster: 2
 MISSING 1 blocks of total size 118 B
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782663_42421 len=118 MISSING!
第 2 行: /user/hbase/kill1 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782666_42424 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-59b0f40d-bacc-4540-85d8-38d4e7ec5c59,DISK], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]
第 3 行: /user/hbase/kill2 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782672_42431 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-7ace0af9-7eb8-4640-8b34-bec5b1768a9c,ARCHIVE], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]
第 4 行: /user/hbase/kill3 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782675_42434 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-7ace0af9-7eb8-4640-8b34-bec5b1768a9c,ARCHIVE], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]
第 5 行: /user/hbase/kill4 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782681_42444 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.
'''



import  os

# def pareitem(item):







def getfile(items):
    fileinfo = items[1]
    print(fileinfo)
    filepattern = re.compile(".*?=(\d), (\d) .*:  (.*)")  # 我们在编译这段正则表达式
    filematcher = re.match(filepattern, fileinfo)  # 在
    filerep = filematcher.group(1)
    fileblk = filematcher.group(2)
    filebklsta = filematcher.group(3)
    print("文件的备份是： ", filematcher.group(1))
    print("文件的块是： ", filematcher.group(2))
    for blkline in items[2:2 + int(fileblk)]:
        getblock(blkline)




def getblock(blkline):
    print("blkline:",blkline)

    blkpattern = re.compile("(\d).\s.*:(\w+)\s.*=(\d+)\s.*=(\d+)\s\s(.*)")  # 我们在编译这段正则表达式
    blkmatcher = re.match(blkpattern, blkline)  # 在

    print(blkmatcher.group())
    blknum = blkmatcher.group(1)
    blkid = blkmatcher.group(2)
    blklen = blkmatcher.group(3)
    blkrepnum = blkmatcher.group(4)
    blkdatainfo=blkmatcher.group(5)
    #[DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-59b0f40d-bacc-4540-85d8-38d4e7ec5c59,DISK], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]
    print(blknum,blkid,blklen,blkrepnum,blkdatainfo)

    p1 = r"(?<=DatanodeInfoWithStorage)\[(\d+.\d+.\d+.\d+):\d+,\w+-\w+-\w+-\w+-\w+-\w+,\w+(?=])"#r"(?<=<h1>).+?(?=<h1>)
    blkldp=re.compile(p1)#re.compile((?<=DatanodeInfoWithStorage).*(?=\\]>))
    #blkldp=re.compile("DatanodeInfoWithStorage\\[(\d+.\d+.\d+.\d+)\:\d+,(.*)\\]") #DatanodeInfoWithStorag.e[(\w+):(\d+),.*
    blkdatam=re.finditer(blkldp,blkdatainfo)

    for match in blkdatam:
        print("==============", match.group())
        print("==============",match.group(1))
        # print("==============", match.group(2))





hdfsfilename="/tmp/256Mfile0"
hdfsfindcmd="sudo -u hdfs  hdfs fsck  {}  -files -blocks -locations".format(hdfsfilename)

#result=os.popen(hdfsfindcmd).read()

result='''FSCK started by hdfs (auth:SIMPLE) from /28.28.33.73 for path /user/hbase/kill1 at Wed May 15 09:59:12 CST 2019
/user/hbase/kill1 118 bytes, replicated: replication=3, 1 block(s):  OK
0. BP-540626610-10.58.33.81-1552889464019:blk_1073782666_42424 len=118 Live_repl=3  [DatanodeInfoWithStorage[28.28.33.72:50010,DS-34510fda-b7d7-4822-bde7-92827f4ac009,ARCHIVE], DatanodeInfoWithStorage[28.28.33.74:50010,DS-59b0f40d-bacc-4540-85d8-38d4e7ec5c59,DISK], DatanodeInfoWithStorage[28.28.33.73:50010,DS-a9dd6688-f6c1-478b-a558-771ec4598a37,ARCHIVE]]

Status: HEALTHY
 Number of data-nodes:	5
 Number of racks:		2
 Total dirs:			0
 Total symlinks:		0

Replicated Blocks:
 Total size:	118 B
 Total files:	1
 Total blocks (validated):	1 (avg. block size 118 B)
 Minimally replicated blocks:	1 (100.0 %)
 Over-replicated blocks:	0 (0.0 %)
 Under-replicated blocks:	0 (0.0 %)
 Mis-replicated blocks:		0 (0.0 %)
 Default replication factor:	3
 Average block replication:	3.0
 Missing blocks:		0
 Corrupt blocks:		0
 Missing replicas:		0 (0.0 %)

Erasure Coded Block Groups:
 Total size:	0 B
 Total files:	0
 Total block groups (validated):	0
 Minimally erasure-coded block groups:	0
 Over-erasure-coded block groups:	0
 Under-erasure-coded block groups:	0
 Unsatisfactory placement block groups:	0
 Average block group size:	0.0
 Missing block groups:		0
 Corrupt block groups:		0
 Missing internal blocks:	0
FSCK ended at Wed May 15 09:59:12 CST 2019 in 0 milliseconds

The filesystem under path '/user/hbase/kill1' is HEALTHY
'''
resultarr=result.split("\n\n")

'''
从第二行开始，每一行都是一个blockid 以及三个备份节点
思路：
远程执行命令并返回：

关系的参数： block个数 ，每个block 的备份个数，以及备份的节点，所在磁盘目录

'''
item=resultarr[0]
items = item.split("\n")
getfile(items)







#localget cmd 后面可以优化为多线程
localdatadir="/home/hadoop"

blkid=""
localgetcmd="find {}  ".format(localdatadir,blkid)





