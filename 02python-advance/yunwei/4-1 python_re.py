#coding:utf-8

#re:(正则)是python当中的一种高级的字符串处理方式，多用于匹配
import re
#匹配
    #1、内容(类型)匹配:内容可以是任何，我们通过特定的语法对要筛选的内容的类型进行描述
        #re
            #1、匹配的规则
                #匹配内容的规则
a = 'hello world!\n I am pyt.hon,this is 2015__ zzzzzz \w'
                    #原内容匹配
#print re.findall('o',a)
                    # . 除了换行之外的任意内容
#print re.findall('.',a)
                    # \w 匹配字母数字下划线
#print re.findall('\w',a)
                    # \W 匹配非字母数字下划线
#print re.findall('\W',a)                    
                    # \d 匹配数字
#print re.findall('\d',a)                    
                    # \D 匹配非字母
#print re.findall('\D',a)                    
                    # \s 匹配所有的空格,\t,\n
#print re.findall('\s',a)                                        
                    # \S 匹配所有的非空格,\t,\n
#print re.findall('\S',a)  
                    # [az] 匹配当中的任意一个元素
#print re.findall('[az]',a)
                    # [a-z] 匹配一个指定的ascii码范围
#print re.findall('[a-z]',a)
                    # [^az] 取非
#print re.findall('[^az]',a)
                    # | 或匹配 匹配两边的任意一边
#print re.findall('[hllo]',a)
#print re.findall('hl|lo',a)
                    #() 组匹配 将组之外的匹配内容作为匹配的条件进行匹配
#print re.findall('\w\d',a)
#print re.findall('(\w)\d',a)
                    # (?P<name>)命名组 (?P=name)命名组的调用
                        #(?P<>)和(?P=)是命名组的固定格式
                        #而在尖括号之内的内容是给改成匹配起的标签名称
                        #而在?P=之后的是对标签的调用
                        #总结起来就是匹配指定命名标签匹配到的内容
#b = 'a1a b2b c3d 4e4'
#print re.findall('(?P<id>\w)\w(?P=id)',b)
#print re.findall('(\w)',b)
#print re.findall('\w',b)
                #匹配顺序的规则
                    #^ 匹配开头
#print re.findall('^\w',a)
                    #$ 匹配结尾
#print re.findall('\w$',a)
                    # \ 转义
#print re.findall('.',a)
                #匹配次数的规则
                    # * 匹配指定内容零到多次
#print re.findall('\w',a)
#print re.findall('\w*',a)
                    # ? 匹配指定内容零到一次
#print re.findall('\w',a)
#print re.findall('\w?',a)
                    # + 匹配指定内容一到多次
#print re.findall('\w',a)
#print re.findall('\w+',a)                    
                    # {3} 匹配指定次
#print re.findall('\w{3}',a)
                    # {3,5} 匹配指定范围次
#print re.findall('\w{3,5}',a)
            #2、匹配的方法
                #re.findall() 有三个参数,第一个参数是匹配的规则
                                      # 第二个参数是匹配的内容
                                      # 第三个参数是特殊匹配
                                      # 返回所有可以匹配成功的内容
                #re.search() 从指定的文章当中匹配一次
'''
ok = re.search('\d',a)
print ok
print ok.group()
'''
                #re.match() 从指定的文章的开头匹配一次
'''
ok = re.match('\d',a)
print ok
print ok.group()
'''
                #re.compile()
'''
ok = re.compile('\w')
print ok.findall(a)
'''
                #re.sub() 类似于replace
#print re.sub('\d','0',a)
                #re.split() 类似于split
#print re.split('\W',a)
                #re.S 修改.的匹配
#print re.findall('.',a,re.S)
                #re.M 修改^$的匹配
c = '''
abc
def
ghi
'''
#print re.findall('^\w',c,re.M)
                #re.I 忽略大小写匹配
#print re.findall('a','aAbA',re.I)
    #2、结构匹配:内容需要有固定的格式，通常我们通过内容的结构形成符合格式的节点，然后来匹配节点，
                #通常用于大规模的大批量的匹配
        #xpath
        #config
        #BeautifulSoup bs4
        
#work:
#1、匹配身份证号
#2、匹配邮箱
#3、匹配网址
#4、匹配指定的HTML标签
