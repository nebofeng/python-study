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
def request_page(url,header=header,xpath="//"):#��������װ�������ݵĲ��� 
    def requet_page(fun):#�������������ṩ���ڲ��������� 
        req = urllib2.Request(url, data=None, headers=header) 
        ope = urllib2.urlopen(req) 
        econtent = etree.HTML(ope.read()) 
        book_list = econtent.xpath(xpath) 
        return fun(book_list)#���ô���ĺ�������Ϊ���ʱ����õ��ڲ��ĺ�����get_book_list # 14
                            #�������Ǳ�book_list��Ϊcontent��ʵ��
    return requet_page 

@request_page(url,xpath="//a[@target='_blank']")#ʹ��װ����request_page 
#��get_book_list ����requet_page��Ϊ����


def get_book_list(content): #��ȡ������ķ���
    book_dict = {} 
    for book in content: 
        book_dict[book.attrib["title"]] = book.attrib["href"] 
    return book_dict 

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
"""
#�ַ�����ƥ�䷽ʽ(�߼����ַ�������ʽ)
    #����:
        #ƥ������
        #ɸѡ����
    #ƥ��ķ�ʽ��
        #�������ݹ����﷨������ƥ��
            #re 
        #�������ݹ����̶��ṹ��ƥ��
            #lxml
            #bs4
#man8
    #re
        #Ҫƥ��һ����m��ͷ��߼�������ĸ�ڼ�һ�����ֵ�����
    #lxml bs4
        #Ҫƥ��1608��b���1����Ա

"""
url = "http://www.xs84.me/paihangbang.php"  
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/paihangbang.php"
        } 
def request_page(url,header=header,xpath="//"):#��������װ�������ݵĲ��� 
    def requet_page(fun):#�������������ṩ���ڲ��������� 
        req = urllib2.Request(url, data=None, headers=header) 
        ope = urllib2.urlopen(req) 
        econtent = etree.HTML(ope.read()) 
        book_list = econtent.xpath(xpath) 
        return fun(book_list)#���ô���ĺ�������Ϊ���ʱ����õ��ڲ��ĺ�����get_book_list # 14
                            #�������Ǳ�book_list��Ϊcontent��ʵ��
    return requet_page 

@request_page(url,xpath="//a[@target='_blank']")#ʹ��װ����request_page 
#��get_book_list ����requet_page��Ϊ����


def get_book_list(content): #��ȡ������ķ���
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
#����������ͼƬ��ȡ
    #��ȡͼƬʵ���������������������ͼƬ��Դ

def fun(a,b,c):
    """
        a ���صĴ���
        b ��λ���ش�С
        c �ܵĴ�С
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
req = urllib2.Request(url, data=None, headers=header) #����header�����������
ope = urllib2.urlopen(req) #���շ������ķ���
content = ope.read() #�����ص����ݶ�����
html = etree.HTML(content) #���ַ��������ݹ�����html�ṹ
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
    req = urllib2.Request(url, data=None, headers=header) #����header�����������
    ope = urllib2.urlopen(req) #���շ������ķ���
    content = ope.read() #�����ص����ݶ�����
    html = etree.HTML(content) #���ַ��������ݹ�����html�ṹ
    xpath = html.xpath("//img") #����������ڼ����һҳ�Ƿ�������Ҫ��ͼƬ
    if xpath == False:
        return "http://www.qiushibaike.com/pic/"
    else:
        url = xpath.find
        return digui_spider(url)










