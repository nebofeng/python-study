#coding:gbk

import re
import urllib
import urllib2
from time import sleep

from lxml import etree
from bs4 import BeautifulSoup

"""
url = "http://www.xs84.me/paihangbang.php"  
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        } 
def request_page(url,header=header,xpath="//"):#用来接收装饰器传递的参数 
    def requet_page(fun):#用来生成数据提供给内部函数调用 
        req = urllib2.Request(url, data=None, headers=header) 
        ope = urllib2.urlopen(req) 
        econtent = etree.HTML(ope.read()) 
        book_list = econtent.xpath(xpath) 
        return fun(book_list)#调用传入的函数，因为这个时候调用的内部的函数是get_book_list # 14
                            #所以我们报book_list作为content的实参
    return requet_page 

@request_page(url,xpath="//a[@target='_blank']")#使用装饰器request_page 
#让get_book_list 传入requet_page作为参数


def get_book_list(content): #获取所有书的方法
    book_dict = {} 
    for book in content: 
        book_dict[book.attrib["title"]] = book.attrib["href"] 
    return book_dict 

for name,href in get_book_list.items():
    print(name)
    print(href)
#1、我们定义一个url
#2、我们定义一个头部
#3、我们创建request_page
#4、我们创建get_book_list
#5、我们将url,xpath，header传入request_page
#6、我们将get_book_list传入requet_page
#7、我们执行requet_page代码，调用fun()也就是get_book_list
#8、get_book_list接收参数执行
#9、返回fun也就是get_book_list的结果
#10、完成闭包 return requet_page
"""
#字符串的匹配方式(高级的字符串处理方式)
    #作用:
        #匹配内容
        #筛选内容
    #匹配的方式：
        #按照内容构建语法描述来匹配
            #re 
        #按照内容构建固定结构来匹配
            #lxml
            #bs4
#man8
    #re
        #要匹配一个以m开头后边加连个字母在加一个数字的名称
    #lxml bs4
        #要匹配1608班b组第1个成员

"""
url = "http://www.xs84.me/paihangbang.php"  
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        } 
def request_page(url,header=header,xpath="//"):#用来接收装饰器传递的参数 
    def requet_page(fun):#用来生成数据提供给内部函数调用 
        req = urllib2.Request(url, data=None, headers=header) 
        ope = urllib2.urlopen(req) 
        econtent = etree.HTML(ope.read()) 
        book_list = econtent.xpath(xpath) 
        return fun(book_list)#调用传入的函数，因为这个时候调用的内部的函数是get_book_list # 14
                            #所以我们报book_list作为content的实参
    return requet_page 

@request_page(url,xpath="//a[@target='_blank']")#使用装饰器request_page 
#让get_book_list 传入requet_page作为参数


def get_book_list(content): #获取所有书的方法
    book_dict = {} 
    for book in content: 
        book_dict[book.attrib["title"]] = book.attrib["href"] 
    return book_dict

page_header = header
page_header["Referer"] = "http://www.xs84.me/paihangbang.php"
@request_page("http://www.xs84.me/104428_0/",xpath="//dl/dd/a",header = header)
def get_page_list(content):
    return content

for i in get_page_list:
    print(i.text)
"""
#基本的爬虫图片爬取
    #爬取图片实际上是向服务器请求下载图片资源

def fun(a,b,c):
    """
        a 下载的次数
        b 单位下载大小
        c 总的大小
    """
    num = 1.0*a*b/c
    if num > 1:
        num = 1
    print("%.3f%%"%(num*100))

"""
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.qiushibaike.com/"
        }
url = "http://www.qiushibaike.com/pic/"
req = urllib2.Request(url, data=None, headers=header) #带着header来请求服务器
ope = urllib2.urlopen(req) #接收服务器的返回
content = ope.read() #将返回的内容读出来
html = etree.HTML(content) #将字符串的内容构建出html结构
xpath = html.xpath("//div[@class='article block untagged mb15']/div[@class='thumb']/a/img")
for i in xpath:
    src = i.attrib["src"]
    name = src.rsplit("/",1)
    print("%s is start"%name[1])
    urllib.urlretrieve(src,name[1],fun)
    print("%s is done"%name[1])


def fun(num):
    if num > 10:
        return num
    else:
        return fun(num+1)+num

print(fun(5))

"""

def digui_spider(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.qiushibaike.com/"
        }
    url = "http://www.qiushibaike.com/pic/"
    req = urllib2.Request(url, data=None, headers=header) #带着header来请求服务器
    ope = urllib2.urlopen(req) #接收服务器的返回
    content = ope.read() #将返回的内容读出来
    html = etree.HTML(content) #将字符串的内容构建出html结构
    xpath = html.xpath("//img") #这个代码是在检查下一页是否有我们要的图片
    if xpath == False:
        return "http://www.qiushibaike.com/pic/"
    else:
        url = xpath.find
        return digui_spider(url)










