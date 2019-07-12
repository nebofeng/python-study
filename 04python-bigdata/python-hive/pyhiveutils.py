import os,sys
import datetime
from pyhive import hive


#pyhive 操作
cursor = hive.connect(host='localhost', username='hive', database='fnbtest').cursor()
query="xxx "
cursor.execute(query)