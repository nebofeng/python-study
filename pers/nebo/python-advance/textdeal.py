#! /bin/python
#coding=utf-8
'''
处理文本的python

'''
import re
txt="1. dsfkajdsalfjdsfjfok"
p="^\d.*(ok)"

pattern = re.compile(p)#我们在编译这段正则表达式
matcher = re.search(pattern,txt)#在
print(matcher.group(0))

key = r"javapythonhtmlvhdl"#这是源文本
p1 = r"python"#这是我们写的正则表达式
pattern1 = re.compile(p1)#同样是编译
matcher1 = re.search(pattern1,key)#同样是查询
print(matcher1.group(0))