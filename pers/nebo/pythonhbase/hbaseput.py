from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *
import re
import sys
import time
current_row=0
transport = TSocket.TSocket('192.168.106.36', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Hbase.Client(protocol)
transport.open()
startTime = time.time()
print str(startTime)
file1 = open("./hbaseput.txt", "r")
while True:
    line=file1.readline()
    if line:
        line=line.strip('\n')
        m=re.split("[,]",line)
        mutations = [Mutation(column = "cf1:finishTime", value =m[1]),
                     Mutation(column = "cf1:requestLine", value =m[2]),
                     Mutation(column = "cf1:returnCode", value = m[3])]
        client.mutateRow('employees', m[0], mutations, None)
        current_row = current_row + 1
    else :
        break
endTime = time.time()
print str(endTime)
print "total insert rows:" + str(current_row)
print "cost time:" + str(endTime - startTime)