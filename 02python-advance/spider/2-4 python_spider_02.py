#coding:gbk

#python ����

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

#pip ����
    #��������һ���ջ�������Ҫ�python����
    #1�������Լ���Ҫ�İ汾��python
    #2����װsetuptools�������Ҫ���ٶȰٶȵ���������
        #�е�����������һ��.exeִ���ļ�
        #�������������һ��ѹ����û��ִ���ļ���������Ҫcmd����python setup.py install
        #python �ǻ������� setup.py �ǰ�������ļ��� install �ǰ�װ����

        #��װ��setuptools ����ӵ����pythonģ������� easy_install
            #easy_install.exe

    #3��������easy_install ��װpip
        #easy_install pip
    #4��Ȼ��������pip��װlxml��bs4
        #pip.exe install lxml
    #5����װbeautifulsoup
        #pip.exe install BeautifulSoup4 #bs4
    #import BeautifulSoup ��
    #from bs4 import BeautifulSoup

#������ģ���������http����������������շ�������Ӧ��һ�ֳ���
    #ģ�������
        #URL ͳһ��Դ��λ��
        #URI ͳһ��Դ��ʶ��
    #URI ���� URL
    ##���������������Ĳ���
        #1��ȷ�������λ�ã�����������˵�ĵ�ַҲ����url
            #������д����Ĺ��̵��У���һ��Ҫ�õ���֪ʶ���URL
                #url example��http://business.sohu.com/20161015/n470353142.shtml
                    #http/https Э��
                        #������������Ƿ��ʻ����������վ��Э������
                    #business.sohu.com ������
                        #������Ҳ�Ǹ�Ŀ¼����˼
                    #/20161015/ ·��
                    #n470353142.shtml ��Դ����
        #2����ʼ����
            #��������ͷ
                #ԭʼͷ��Ϣ
"""
            #{
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",#������������
                "Accept-Encoding":"gzip, deflate",#���յķ�ʽ
                "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",#���յ�����
                "Connection":"keep-alive",#�����һ��״̬�������keep-alive������������Ĺ��̵���һֱ��������
                "Cookie":\"""SUV=1512091847247909; vjuids=-3463a8159.151b8fdeec5.0.206aa7d4ebb2e; vjlast=1450507628.1476537570.23
                ; sohutag=8HsmeSc5NCwmcyc5NCwmYjc5NSwmYSc5NCwmZjc5NCwmZyc5NCwmbjc5NCwmaSc5NCwmdyc5NCwmaCc5NCwmYyc5NCwmZSc5NCwmbSc5NCwmdCc5NH0
                ; IPLOC=CN5000"\"",#��ע�û���� #���� С����
                #��http������cookie��һ����ݵı�ʶ
                    #����ǰ��һ��ʱ�����Ƿ�����վ��ʱ����һ��������״̬
                    #cookie �����������̵��еĺ���
                        #��while��������ʱ�򣬵�����while 01��������ʶwhile
                            #while �Լ��� �������˼ǵ�01��
                            #while �԰ײ� �������˼ǵ�01��
                        #���û������������ʱ�򣬷�������Ӧ���Ҹ��û�һ���
                            #��ô�û��������ݣ����Դ���ݷ���������վ
                "Host":"business.sohu.com",#��������
                "If-Modified-Since":"Sat, 15 Oct 2016 09:28:31 GMT",#ʱ��
                "User-Agent":"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04"#�������Ϣ
                #����������
                    #�������ò
                        #���������������������Ϊ�ķ����ٶ������޵�,����������������ô�����ٶȿ��Լ��죬�����������ѹ��
                            #ϣ�������������sleep�Ĺ���
                        #ʹ��������һ���ֳ���Ա���Ų�����Ŀ�ģ���ȡһ�½�ֹ��ȡ�����ݣ����縶������
                    #������Ϊ�кö಻��ò�����棬���ԣ��в�����վ������
                        #1��user_agent
                        #2��ҳ��Ӷ���
                        #3��ҳ�����
                        #4��ajax��js�첽����
                        #5�����ּ���
                        #6��ͳͳ�Ĳ��������������ҵ������ַ
                        #7����ݵ��ϸ�ʶ��
                #}
"""
            #�������������
                #����ʽ
                    #POST ���ص�����ʽ
                    #GET �����url�ϵ�����ʽ
                        #get �������ʺſ�ʼ���ԡ�&���ָ�ʡ���=ֵ������ʽ
                        #https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=man8&rsv_pq=b33f65e700032038&rsv_t=8a81Gk9yDukgCvKLbPdgn%2B%2BoFqDB6ltm76EXGi41a5QMQGbactjxhPV3VE0&rqlang=cn&rsv_enter=0&rsv_sug3=5&rsv_sug1=3&rsv_sug7=100&inputT=4222&rsv_sug4=5637
            
            #��Ӧͷ��
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
                "Server":"SWS", #�û�����ķ�����������
                "Vary":"Accept-Encoding",
                "X-RS":"10587158.19762208.11340962"
                }
"""
            #��Ӧ����
                #text/html
                #img/jpg
            
            #���ر�����Ӧ����
                #�����������ͬ
                #���Ե���дǰ�˵�ͬѧ�������������Ե�����
                
#�ж����ݱ���
    #chardet ��һ�������������ж��ַ��������ģ�鵫�ǲ�̫׼ȷ
        


#����url
url = "http://business.sohu.com/20161015/n470353142.shtml"
url = "http://www.qiushibaike.com/"
#����ͷ��
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04"
    }
#��������
#req = urllib2.Request(header,data = None,)
req = urllib2.Request(url, data=None, headers=header)
#������Ӧ
ope = urllib2.urlopen(req)
#print(ope)
#print(ope.read())
econtent = etree.HTML(ope.read())#����xpath ��״�ṹ
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
myx = econtent.xpath("//p")

for i in myx:
    #print(i.tag)
    #print(i.attrib)
    print(i.text)
#for i in ope.readlines():
#    print(i)
#ope.close()


















    
    



