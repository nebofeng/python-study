#!F:\soft\python27\python
#coding:utf-8

import cgi

request_data = cgi.FieldStorage()

try:
    save_data = request_data['data'].value
except:
    save_data = ""
if save_data:
    f = open("cgi-bin/1.txt","w")
    f.write(save_data)
    f.close()
