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

#����ģ�������
    #���������������Ĳ���
        #1��ȷ�������λ�ã�����������˵�ĵ�ַҲ����url
        #2����ʼ����
            #header
                #user_agent:����û������
                #python 2.7
                #���ǽ��Լ�αװ�������
                    
        #3���������������
        #4����Ӧͷ��
        #5����Ӧ����

"""
#url = "http://www.xs84.me/"
url = "http://www.xs84.me/210329_0/"
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Referer":"http://www.xs84.me/"
    }
#header ���ֺ� proxy_ip���������ʹ��random

#��������
req = urllib2.Request(url, data=None, headers=header)
#������Ӧ
ope = urllib2.urlopen(req)
econtent = etree.HTML(ope.read())#����xpath ��״�ṹ
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
    #xpath ƥ���﷨
        # // �Ǵ������е�
        # /  ����㼶
        # [] ɸѡ
        # @ ɸѡ����
    #xpath ƥ�䵽��������������������
        #tag ���ض����ǩ����
        #attrib ���ض�������
        #text ���ض����е��ı�
        
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
