#coding:gbk

#python 爬虫

    #urllib
    #urllib2
    #re
    #lxml
    #beautifulsoup

import re
import urllib
import urllib2
#3.x urllib
    #urllib.request
    #import urllib.request
    #from urllib import request

from lxml import etree #xpath
from bs4 import BeautifulSoup as btf 

#pip 问题
    #当我们在一个空环境下需要搭建python环境
    #1、下载自己需要的版本的python
    #2、安装setuptools，这个需要到百度百度到官网下载
        #有的下载下来是一个.exe执行文件
        #如果下载下来是一个压缩包没有执行文件，我们需要cmd命令python setup.py install
        #python 是环境变量 setup.py 是包里面的文件， install 是安装命令

        #安装完setuptools 我们拥有了python模块管理工具 easy_install
            #easy_install.exe

    #3、我们用easy_install 安装pip
        #easy_install pip
    #4、然后我们用pip安装lxml和bs4
        #pip.exe install lxml
    #5、安装beautifulsoup
        #pip.exe install BeautifulSoup4 #bs4
    #import BeautifulSoup 慢
    #from bs4 import BeautifulSoup

#爬虫是模拟浏览器向http服务器发送请求接收服务器响应的一种程序
    #模拟浏览器
        #URL 统一资源定位符
        #URI 统一资源标识符
    #URI 大于 URL
    ##浏览器请求服务器的步骤
        #1、确定请求的位置，就是我们所说的地址也就是url
            #我们在写爬虫的过程当中，第一个要用到的知识点就URL
                #url example：http://business.sohu.com/20161015/n470353142.shtml
                    #http/https 协议
                        #这个描述了我们访问或者请求的网站的协议类型
                    #business.sohu.com 主机名
                        #主机名也是根目录的意思
                    #/20161015/ 路径
                    #n470353142.shtml 资源名称
        #2、开始请求
            #发送请求头
                #原始头信息
"""
            #{
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",#接收内容类型
                "Accept-Encoding":"gzip, deflate",#接收的方式
                "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",#接收的语言
                "Connection":"keep-alive",#请求的一个状态，如果是keep-alive代表在你浏览的过程当中一直保持连接
                "Cookie":\"""SUV=1512091847247909; vjuids=-3463a8159.151b8fdeec5.0.206aa7d4ebb2e; vjlast=1450507628.1476537570.23
                ; sohutag=8HsmeSc5NCwmcyc5NCwmYjc5NSwmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NCwmaSc5NCwmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0
                ; IPLOC=CN5000"\"",#标注用户身份 #曲奇 小饼干
                #在http请求当中cookie是一个身份的标识
                    #在以前的一个时期我们访问网站的时候是一种匿名的状态
                    #cookie 类似于麻辣烫当中的号牌
                        #当while吃麻辣的时候，店主给while 01号牌来标识while
                            #while 吃鸡蛋 店主把账记到01上
                            #while 吃白菜 店主把账记到01上
                        #当用户请求服务器的时候，服务器响应并且给用户一身份
                            #那么用户保存此身份，并以此身份访问整个网站
                "Host":"business.sohu.com",#请求主机
                "If-Modified-Since":"Sat, 15 Oct 2016 09:28:31 GMT",#时间
                "User-Agent":"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04"#浏览器信息
                #浏览器的身份
                    #爬虫的礼貌
                        #如果是真的浏览器，我们人为的访问速度是有限的,但是我们用爬虫那么访问速度可以极快，给服务器造成压力
                            #希望大家有类似于sleep的功能
                        #使用爬虫有一部分程序员带着不纯的目的，爬取一下禁止爬取的内容，比如付费内容
                    #正是因为有好多不礼貌的爬虫，所以，有部分网站反爬虫
                        #1、user_agent
                        #2、页面从定向
                        #3、页面加码
                        #4、ajax或js异步请求
                        #5、各种加密
                        #6、统统的藏起来，不让你找到请求地址
                        #7、身份的严格识别
                #}
"""
            #发送请求的数据
                #请求方式
                    #POST 隐藏的请求方式
                    #GET 存放在url上的请求方式
                        #get 请求以问号开始，以“&”分割，呈“键=值”的形式
                        #https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=man8&rsv_pq=b33f65e700032038&rsv_t=8a81Gk9yDukgCvKLbPdgn%2B%2BoFqDB6ltm76EXGi41a5QMQGbactjxhPV3VE0&rqlang=cn&rsv_enter=0&rsv_sug3=5&rsv_sug1=3&rsv_sug7=100&inputT=4222&rsv_sug4=5637
            
            #响应头部
"""
            {
                "Cache-Control":"no-transform, max-age=120",
                "Connection":"keep-alive",
                "Content-Encoding":"gzip",
                "Content-Length":21388,
                "Content-Type":"text/html",
                "Date":"Sat, 15 Oct 2016 14:04:23 GMT",
                "Expires":"Sat, 15 Oct 2016 14:06:23 GMT",
                "FSS-Cache":"HIT from 8802488.15945922.9802277",
                "FSS-Proxy":"Powered by 2969695.4280425.3969395",
                "Last-Modified":"Sat, 15 Oct 2016 09:28:32 GMT",
                "Server":"SWS", #用户请求的服务器的类型
                "Vary":"Accept-Encoding",
                "X-RS":"10587158.19762208.11340962"
                }
"""
            #响应内容
                #text/html
                #img/jpg
            
            #加载编译响应内容
                #由于浏览器不同
                #所以导致写前端的同学都会遇到兼容性的问题
                
#判断内容编码
    #chardet 是一个三方的用来判断字符串编码的模块但是不太准确
        


#设置url
url = "http://business.sohu.com/20161015/n470353142.shtml"
url = "http://www.qiushibaike.com/"
#设置头部
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04"
    }
#发起请求
#req = urllib2.Request(header,data = None,)
req = urllib2.Request(url, data=None, headers=header)
#接收响应
ope = urllib2.urlopen(req)
#print(ope)
#print(ope.read())
econtent = etree.HTML(ope.read())#构建xpath 树状结构
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
myx = econtent.xpath("//p")

for i in myx:
    #print(i.tag)
    #print(i.attrib)
    print(i.text)
#for i in ope.readlines():
#    print(i)
#ope.close()


















    
    



