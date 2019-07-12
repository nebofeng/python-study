#coding:gbk

#re
#bs4
#lxml

import re
import urllib
import urllib2
#urllib
#from urllib import request

#import urllib
#urllib.request

from lxml import etree
from bs4 import BeautifulSoup

#爬虫模拟浏览器
    #浏览器请求服务器的步骤
        #1、确定请求的位置，就是我们所说的地址也就是url
        #2、开始请求
            #header
                #user_agent:标记用户的身份
                #python 2.7
                #我们将自己伪装成浏览器
                    
        #3、发送请求的数据
        #4、响应头部
        #5、响应内容

"""
#url = "http://www.xs84.me/"
url = "http://www.xs84.me/210329_0/"
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }
#header 部分和 proxy_ip部分最合适使用random

#发起请求
req = urllib2.Request(url, data=None, headers=header)
#接收响应
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())#构建xpath 树状结构
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    pass



#Referer http://www.xs84.me/210329_0/
url = "http://www.xs84.me/210329_1231167/"
header["Referer"] = "http://www.xs84.me/210329_0/"
req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
content = ope.read()
content = content.replace("<br>","\n").replace("<br/>","\n")
econtent = etree.HTML(content)
dl_list = econtent.xpath("//div[@id='content']")
for i in dl_list:
    f = open(filename,"w")
    f.write(i.text)
    f.close()
    sleep(1)
#<div id="content">


    #print(dl.attrib["href"])
    #print(dl.text)
    #xpath 匹配语法
        # // 是代表所有的
        # /  代表层级
        # [] 筛选
        # @ 筛选条件
    #xpath 匹配到的内容我们又三个方法
        #tag 返回对象标签名称
        #attrib 返回对象属性
        #text 返回对象当中的文本
        
#myx = econtent.xpath("//div")
#myx = econtent.xpath("//p")

#for i in myx:
    #print(i.tag)
    #print(i.attrib)
#    print(i.text)
#for i in ope.readlines():
#    print(i)
#ope.close()
"""


header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }

def get_content(url,filename):
    print("%s is start"%filename)
    url = "http://www.xs84.me"+url
    filename = filename+".txt"
    
    header["Referer"] = "http://www.xs84.me/210329_0/"
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    content = ope.read()
    content = content.replace("<br>","\n").replace("<br/>","\n")
    econtent = etree.HTML(content)
    dl_list = econtent.xpath("//div[@id='content']")
    for i in dl_list:
        f = open(filename,"w")
        f.write(i.text)
        f.close()
        sleep(1)
    print("%s is done"%filename)
url = "http://www.xs84.me/210329_0/"

req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    print(dl.attrib["href"])
    get_content(dl.attrib["href"],dl.text)
