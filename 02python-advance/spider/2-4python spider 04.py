#coding:gbk

import re
import urllib
import urllib2
from time import sleep

from lxml import etree
from bs4 import BeautifulSoup

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
        print(i.text)
#        f = open(filename,"w")
#        f.write(i.text)
#        f.close()
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
"""
#python �Զ�����ά
    #�Զ�����ά
    #ƫ��ά����Ŀ���

    #3.x �ȶ�
    #linux centos ubuntn 2.4 2.6 2.7
    
#��������
#2.x
    #str
        #�ַ���
        #unicode
        #encode #����
        #decode #����
#3.x
    #bytes decode
    #str encode
    

#�κ����Ե��ַ����������Լ��ĺ��ı���
    #2.x python ���ı����� unicode
        #������Դ      utf-8
        #����Ŀ�ĵ�     gbk
        #utf-8 ---> gbk
            #1��������Ҫ����utf-8�ĸ�ʽ��utf-8���ַ��������unicode decode
            #2�������ٽ�ת��������unicode�ַ�����gbk�ķ�ʽ�����gbk  encode

            #Ӣ����(˵��) #Ӣ����˵ hello world
                

            #�й���(����) #�Ƚ� hello world ����Ӣ����˼��������� ���
                         #�ٽ� ��� �����﷨����˼���복 o ha yi you
    
            #�ձ���(����) o ha yi you
            
    #3.x python  ���ı����� bytes
            #bytes decode ����
            #str  encode ����
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
        print(i.text)
        #f = open(filename,"w")
        #f.write(i.text)
        #f.close()
        #sleep(1)
    print("%s is done"%filename)
url = "http://www.xs84.me/210329_0/"

req = urllib2.Request(url, data=None, headers=header)
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())
dl_list = econtent.xpath("//dl/dd/a")
for dl in dl_list:
    print(dl.attrib["href"])
    get_content(dl.attrib["href"],dl.text)
"""
#�������������ʱ��
    #����
        #1������Ҫ��ȡһ��С˵
        #2������Ҫ��ȡ������С˵
        #3������Ҫ��ȡָ����С˵
            #��Ҫ��ȡ��վ��С˵
    #1���ֽ�����
        #������������£�ʵ���Ͼ�������һ����
        #��������б�����������վ

        #1����Ҫ�й�����ȡһ�µ�����
        #2������Ҫ��ȡ���������½ڵĹ���
        #3������Ҫ��ȡ��վ������Ĺ���
#1��
"""
book_list = {}#��������������·��
page_list = []#���������������½ڵ�·��

book_list = {"zx":page_list,"hd":page_list}
for book in book_list:
    for page in book_list[book]:
        get(page) #��ȡһ�µ�����


def book_list(): #��ȡ������ķ���
    url = "http://www.xs84.me/paihangbang.php"
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }
    book_dict = {}
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    econtent = etree.HTML(ope.read())
    book_list = econtent.xpath("//a[@target='_blank']")
    for book in book_list:
        book_dict[book.attrib["title"]] = book.attrib["href"]
    return book_dict
    
def page_list(): #��ȡ�����µķ���
    return page_list
def get_page(): #��ȡÿҳ���ݵķ���
    return page_content

def main(): #�����߼�Э������ķ���
    book_dict = book_list()
    for name,href in book_dict.items():
        print(name)
        print(href)
if __name__ == "__main__":
    main()

header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }
def requet_page(url,header=header,xpath="//"):
    req = urllib2.Request(url, data=None, headers=header)
    ope = urllib2.urlopen(req)
    econtent = etree.HTML(ope.read())
    book_list = econtent.xpath(xpath) 
    return book_list


def get_book_list(): #��ȡ������ķ���
    book_dict = {}
    url = "http://www.xs84.me/paihangbang.php"
    book_list = requet_page(url,xpath="//a[@target='_blank']")
    for book in book_list:
        book_dict[book.attrib["title"]] = book.attrib["href"]
    for name,href in book_dict.items():
        print(name)
        print(href)

get_book_list()

"""
"""
    
    #for book in book_list:
    #    book_dict[book.attrib["title"]] = book.attrib["href"]
    #return book_dict
    
def page_list(): #��ȡ�����µķ���
    return page_list
def get_page(): #��ȡÿҳ���ݵķ���
    return page_content

def main(): #�����߼�Э������ķ���
    get_book_list()
    #book_dict = get_book_list()
    #for name,href in book_dict.items():
    #    print(name)
    #    print(href)
if __name__ == "__main__":
    main()





def outer(fun):
    def inner(a,b):
        print("this is inner function")
        fun()
    return inner
@outer
def hello():
    print("hello world")
hello(1,2)


def outerr(a,b):
    def outer(fun):
        def inner():
            print(a,b)
            print("this is inner function")
            fun()
        return inner
    return outer
@outerr(1,2)
def hello():
    print("hello world")
hello()

"""
url = "http://www.xs84.me/paihangbang.php"  # 1
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        }  # 2
def request_page(url,header=header,xpath="//"):#��������װ�������ݵĲ��� # 3
    def requet_page(fun):#�������������ṩ���ڲ��������� # 4
        req = urllib2.Request(url, data=None, headers=header) # 6
        ope = urllib2.urlopen(req) # 7
        econtent = etree.HTML(ope.read()) # 8
        book_list = econtent.xpath(xpath) #9
        return fun(book_list)#���ô���ĺ�������Ϊ���ʱ����õ��ڲ��ĺ�����get_book_list # 14
                            #�������Ǳ�book_list��Ϊcontent��ʵ��
    return requet_page #15

@request_page(url,xpath="//a[@target='_blank']")#ʹ��װ����request_page #5
#��get_book_list ����requet_page��Ϊ����


def get_book_list(content): #��ȡ������ķ���
    book_dict = {} # 10
    for book in content: # 11
        book_dict[book.attrib["title"]] = book.attrib["href"] # 12
    return book_dict # 13

for name,href in get_book_list.items():
    print(name)
    print(href)
#1�����Ƕ���һ��url
#2�����Ƕ���һ��ͷ��
#3�����Ǵ���request_page
#4�����Ǵ���get_book_list
#5�����ǽ�url,xpath��header����request_page
#6�����ǽ�get_book_list����requet_page
#7������ִ��requet_page���룬����fun()Ҳ����get_book_list
#8��get_book_list���ղ���ִ��
#9������funҲ����get_book_list�Ľ��
#10����ɱհ� return requet_page






