#元类，是一种特殊的修改类当中属性的魔术方法 ORM : peewee
"""
name = dict(zip(("abcdef"),range(6)))
print(name)
name = dict(a = 1,b = 2,c = 3,d = 4)
print(name)

def hello(self):
    print("hello wrold")

hello(1)

#print(type(hello))

class Hi(object):
    pass
print(Hi)
"""
"""
def hello(self):
    print("hello wrold")

Hello = type("Hello",(object,),dict(h = hello))
print(Hello)
he = Hello()
he.h()

print(help(type))
def hello(self):
    print("hello wrold")

Hello = type("Hello",(object,),dict(h = hello))
print(Hello)
he = Hello()
he.h()

class A:
    pass
class B(object):
    pass

print(type(type))
print(type(A)) #经典类 是类对象
print(type(B)) #新式类 是类型对象

def hello(self):
    print("hello wrold")

Hello = type("Hello",(object,),dict(h = hello))
    #type 第一个参数是用来给新生产的类型起名字的
    #(object,) 是生成的新类继承的类，也就是父类
    #第三个参数是类中包含的方法
print(Hello)
he = Hello()
he.h()

def hello(self):
    print("hello wrold")

def hi(self):
    print("hi world")
def __init__(self):
    pass

H = type("Hello",(object,),dict(he = hello,h = hi,name = "laobian"))

print(H)
hei = H()
hei.he()
hei.h()
print(hei.name)

"""
class Hello(object):
    pass

H = Hello
print(Hello)
print(H)









    




