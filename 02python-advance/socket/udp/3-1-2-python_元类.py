#Ԫ�࣬��һ��������޸��൱�����Ե�ħ������ ORM : peewee
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
print(type(A)) #������ �������
print(type(B)) #��ʽ�� �����Ͷ���

def hello(self):
    print("hello wrold")

Hello = type("Hello",(object,),dict(h = hello))
    #type ��һ�������������������������������ֵ�
    #(object,) �����ɵ�����̳е��࣬Ҳ���Ǹ���
    #���������������а����ķ���
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









    




