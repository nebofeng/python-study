#coding:gbk
#��������װ(˽�л�)�Ͷ�̬
    #��װ(˽�л�):���Ǹ���ĵ�����һ���̶��ĵ��÷�ʽ�ͽӿڣ�
        #���淶���ʹ��
        #��������ǰ�����"__"(�����»��ߣ��������˽������
    #�̳�
    #��̬
"""
class Person(object):
    def __init__(self,age = 0,name = ""):#���캯��
        self.__age = age #˽�е���
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#˽�еķ���
        self.__age += 1
        return self.__age
    def age(self):
        self.__add_age()
        print(self.__age)
    
p = Person(12,"laobian")
#print(p.name)
#print(p.__age)
p.age()
#p.__add_age()
"""
#���ִ��˳��
"""
class Person(object):
    def __init__(self,age = 0,name = ""):#���캯��
        self.__age = age #˽�е���
        self.name = name
        self.__add_age()
        #self.__age = self.__add_age()
        print("this is person")
    def __add_age(self):#˽�еķ���
        self.__age += 1
        #return self.__age
    def age(self):
        self.__add_age()
        print(self.__age)
    
p = Person(12,"laobian")
print(p)
#1��<__main__.Person object at 0x02C6AF50>������ڴ��ַ����
#������Ѿ�ʵ���õ�Personʵ�������з���
#2��ʵ����֮������ִ��__init__����
    #1�����ȸ�˽����self.__age��ֵ
    #2��Ȼ��self.name��ֵ
    #3��Ȼ�����self.add_age()
    #4��print("this is person")
p.age()
#3��ִ��p�ķ���age

class Person(object):
    def __init__(self,age = 0,name = ""):
        self.__age = age 
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#˽�еķ���
        self.__age += 1
    def age(self):
        print("he is %s years old"%self.__age)
p = Person(12,"laobian")
p.__age = 16
print(p.__age)
p.age()

class Person(object):
    def __init__(self,age = 0,name = ""):
        self.__age = age 
        self.name = name
        self.__add_age()
        print("this is person")
    def __add_age(self):#˽�еķ���
        self.__age += 1
    def change_age(self,age):
        self.__age = age
    def age(self):
        print("he is %s years old"%self.__age)
p = Person(31,"laobian")#����ִ����__init__
p.age() #32
p.change_age(18)#18
#p.__init__(18,"laobian")
p.age() #18

#@property
class Person(object):
    @property #��self.age()1 ���������ɱ�������ʽ
    def age(self):#1
        return self.__age
    #��self.age()2 ���һ����ֵ�Ĺ���
    @age.setter #������װ������ɵ�һ���Ժ�
    def age(self,age):#2 �Զ�����@age.setter���װ����
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError("age must be int")
    
p = Person()
p.age = 15 #���õ���p.age 2
print(p.age)#���õ���p.age 1

class Person(object):
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            raise TypeError("age must be int")
    
p = Person()
p.set_age(15)#p.age = 15 
print(p.get_age())
"""
#��̬:��̬���������ڵ���ͬһ��������ʱ��
#��Ϊ���õ�ʵ����һ�����½����һ��
    # +
#print(1+1) #�������
#print("1"+"1") #�ַ���ƴ��
    
#Ѽ������:��еĶ���Ѽ��
"""
class Bird(object):
    def sing(self):
        print("a ha ha")

class Duck(Bird):
    def sing(self):
        print("a ga ga")


b = Bird()
d = Duck()
b.sing()
d.sing()

class Ints(object):
    def add(self,a,b):
        return a+b
    
class Strs(object):
    def add(self,a,b):
        return "%s%s"%(a,b)

print(1+1) #�������
print("1"+"1") #�ַ���ƴ��

#����������Ϊ��
#����������Ϊ��
#���ǽ����Ϻͻ�����������ʵ��
#��ô���ǵ���ͬ���������ӵķ���������Ͳ�һ��
#��ͬ��ʵ���ڵ���ͬ���ķ�����ʱ�򣬷��صĽ����һ��

class Parent(object):
    def __init__(self):
        print("I am a Person")
    def gender(self):
        print("I am a man")

class Child(Parent):
    def gender(self):
        print("I am a girl")

p = Parent()
c = Child()

p.gender()
c.gender()

class Parent(object):
    def __init__(self):
        print("I am a Person")
    def gender(self):
        print("I am a man")

class Child(Parent):
    def gender(self):
        #Parent.gender(self)
        #super(Child,self).gender()
        print("I am a girl")

p = Parent()
c = Child()

p.gender()
c.gender()
"""
#__init__
#__del__

#__str__
#__repr__
#__iter__
#__call__
"""
class Person(object):
    def __str__(self):
        return "this is a person"
    def __repr__(self):
        return "this is a person"
p = Person()
print(p)

class Person(object):
    def __str__(self):
        return "this is a person"
    __repr__ = __str__
        
p = Person()
print(p)
"""        
#iter ������

#d = dict(zip("abcdef",range(6)))
#print(d)
#enumerate #ö��
#d_iter = d.iteritems()

#iterable �ɵ�����

#for i in range(3):
#    print(i)

#a = iter("abcdef")
#print(a)
#yield ������
#a = iter("abcdef")
#print(a.next())
"""
class Myiter(object):
    def __init__(self,a,b):
        self.a,self.b = a,b
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    
m = Myiter(1,2)
for i in m:
    print(i)

class Myiter(object):
    def __init__(self,a,b):
        self.a,self.b = a,b
    def __iter__(self):
        \"""
            __iter__��һ��pythonħ������
            �������þ��ǽ�����һ��ָ���Ŀɵ����Ķ���
            ������2.x�汾���������next����
            ��3.x�汾�����__next__
        \"""
        return self
    def next(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    
m = Myiter(1,2)
for i in m:
    print(i)

#callable �����񱻺���һ�����ã��ɵ��õ�
def hello():
    print("hello world")
print(callable(hello))

class Person(object):
    pass

p = Person()
p()

class Person(object):
    def __call__(self):
        return "�����Ҹ�ɶ��"

p = Person()
print(p())

"""
class Person(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        return self.a + self.b
    def __call__(self):
        return self.a + self.b

p = Person(1,2)
print(p())


















    








