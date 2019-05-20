"""
a = 1
b = a+1
print(b)

#print("%s is %s"%(name,age))

def fun_name(name,age):
    print("%s is %s "%(name,age))

fun_name('a',16)
fun_name('b',15)


def connect(user,passwd):
    sql.connect(user = user,passwd = passwd,host = host)


for index in range(10):
    pass

print(index)

ls = 4 #全局的变量
def test(ls):
    #形参是该函数的局部变量
    ls = 5
    ls += 1 #局部的变量
    print(ls)

test(100)
print(ls)
print(dir())
import os
print(dir())

def outer():
    value = 1 #局部的作用域
    def inner():
        value = 2 #局部作用域
        return value
    return inner()

outer()

def outer():
    value = 1 #局部的作用域
    def inner():
        return value #嵌套作用域
    return inner()

print(outer())

value = 1
def outer():
    #value = 1 #局部的作用域
    def inner():
        return value #嵌套作用域
    return inner()

print(outer())

import sys #内置作用域
#sys.path = 10 #全局作用域
def outer():
    #sys.path = 10 #嵌套作用域
    def inner():
        #sys.path = 10 #局部作用域
        return sys.path
    return inner()

print(outer())

def outer():
    def inner():
        return 1

print(outer())

def outer():
    return 1

print(outer)
print(outer())

#函数的嵌套
def outer():
    def inner():
        return 1

print(outer())

#闭包
def outer():
    def inner():
        return 1
    return inner

def outer():
    def inner():
        return 1
    return inner()

print(outer())

def outer(num):
    def inner():
        return num
    return inner

print(outer(3)())

def outer(fun):
    #fun = name
    def inner():
        print("inner is start")
        fun()#name() --> I am while
        print("inner is done")
        #return "while is cool"
    return inner

def name():
    print("I am while")

#print(name)
#print(outer(name))
print(outer(name)())
    #name 是一个普通的函数
    #outer(name) 是一个接收name函数作为参数的outer函数的调用，
    #            返回inner
    #outer(name)() 就是对返回的以name作为嵌套作用域的
    #            inner函数的调用
    #print(outer(name)()) 打印inner


def outer(fun):
    def inner():
        print("inner is start")
        fun()
        print("inner is done")
    return inner
@outer #--> name = outer(name)
def name():
    print("I am while")

name()

#name = outer(name)
#print(name())

def outer(fun):
    def inner():
        print("hello this is our school")
        fun()
        print("this teacher is our teacher")
    return inner
@outer #while_name = outer(name)
def while_name():
    print("I am while")

@outer #for_name = outer(name
def for_name():
    print("I am for")

while_name()
print("I am +++++++++++++++++++++++++")
for_name()

import time
def zs_loger(fun):
    def inner():
        types,data = fun()
        content = "[%s]:[%s]%s"
        return content%(time.ctime(),types,data)
    return inner

@zs_loger
def loger1():
    return "Error","your password error"

@zs_loger
def loger2():
    return "woring","your are logout"

print(loger1())
print(loger2())
"""
import time
def zs_loger(fun):
    types,data = fun()
    content = "[%s]:[%s]%s"
    return content%(time.ctime(),types,data)

@zs_loger #loger1 = zs_loger(loger1) 
def loger1():
    return "Error","your password error"

@zs_loger #loger2 = zs_loger(loger2)
def loger2():
    return "woring","your are logout"

print(loger1)
print(loger2)




























