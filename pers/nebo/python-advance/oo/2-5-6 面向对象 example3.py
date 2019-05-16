#coding:utf-8
#python 面向对象的三大特征
        #继承
            #object 基类,是python定义的所有类的父类
            #经典类:不继承object的类称作经典类
            #新式类:继承object的类称作新式类
            #python 3.x统一为新式类
            #经典类是类对象，新式类是类型对象
'''

class Person:
    pass
print(type(Person))
class Person(object):
    pass
print(type(Person))
print(type(str))
#继承，并且继承父类的所有
class Parent:
    def __init__(self):
        self.age = 0
    def sing(self):    
        print("sing a song")
        
class Child(Parent):
    pass

c = Child()
print(c.age)
c.sing()
#在子类有自己的方法的同时，完全继承父类
class Parent:
    def __init__(self):
        self.age = 0
    def sing(self):    
        print("sing a song")
        
class Child(Parent):
    def sleep(self):
        print("Z~ZZ~ZZZ")

p = Parent()
c = Child()
print(c.age)
c.sing()
c.sleep()
p.sleep()
#重写，保留父类的部分属性
class Parent:
    def __init__(self):
        self.age = 0
    def sing(self):    
        print("sing a song 2")
        
class Child(Parent):
    def sleep(self):
        print("Z~ZZ~ZZZ")
    def sing(self):
        print("Sing a Song 1")

p = Parent()
c = Child()
print(c.age)
c.sing()


#重写，保留父类属性的同时有自己的属性
class Parent:
    def __init__(self):
        self.age = 0
    def sing(self):    
        print("sing a song 2")
        
class Child(Parent):
    def sleep(self):
        print("Z~ZZ~ZZZ")
    def sing(self):
        Parent.sing(self)
        print(self)
        print("Sing a Song 1")

p = Parent()
c = Child()
print(c.age)
c.sing() #--->Child.sing(c)
#经典类的继承是按照继承的顺序进行继承的

class A:
    def __init__(self):
        print("I am A")

class B(A):
    pass
    
class C(A):
    def __init__(self):
        print("I am C")
class D(C,B):
    pass

d = D()

#新式类是按照修改的优先级来继承,越后修改优先级就越高。

class A(object):
    def __init__(self):
        print("I am A")

class B(A):
    pass
    
class C(A):
    def __init__(self):
        print("I am C")
class D(B,C):
    pass

d = D()

    #super
class Parent(object):
    def __init__(self):
        print("his is parent")
    def eat(self):
        print("parent eat")
class Parent1(object):
    def __init__(self):
        print("his is parent1")
    def eat(self):
        print("parent1 eat")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("his is child")
    def eat(self):
        Parent.eat(self)
        print("child eat")

c = Child()
c.eat()

class Parent(object):
    def __init__(self):
        print("his is parent")
    def eat(self):
        print("parent eat")
class Parent1(object):
    def __init__(self):
        print("his is parent1")
    def eat(self):
        print("parent1 eat")
class Child(Parent1):
    def __init__(self):
        Parent1.__init__(self)
        print("his is child")
    def eat(self):
        Parent1.eat(self)
        print("child eat")
c = Child()
c.eat()

class Parent(object):
    def __init__(self):
        print("his is parent")
    def eat(self):
        print("parent eat")
class Parent1(object):
    def __init__(self):
        print("his is parent1")
    def eat(self):
        print("parent1 eat")
class Child(Parent1):
    def __init__(self):
        super(Child,self).__init__()
        print("his is child")
    def eat(self):
        super(Child,self).eat()
        print("child eat")
c = Child()
c.eat()

class Parent(object):
    def __init__(self):
        print("his is parent")
    def eat(self):
        print("parent eat")
class Parent1(object):
    def __init__(self):
        print("his is parent1")
    def eat(self,food):
        print("parent1 eat "+food)
class Child(Parent1):
    def __init__(self):
        super(Child,self).__init__()
        print("his is child")
    def eat(self,foods):
        super(Child,self).eat(foods)
        print("child eat")
c = Child()
c.eat('apple')

#感觉super没有啥用，只是简化了我们的继承代码

class GrandParents(object):
    def __init__(self):
        print("this is GradParents")
class Parent1(GrandParents):
    def __init__(self):
        GrandParents.__init__(self)
        print("this is Parent1")
class Parent2(GrandParents):
    def __init__(self):
        GrandParents.__init__(self)
        print("this is Parent2")
class Child(Parent1,Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("this is Child")

c = Child()

class GrandParents(object):
    def __init__(self):
        print("this is GradParents")
class Parent1(GrandParents):
    def __init__(self):
        super(Parent1,self).__init__()
        print("this is Parent1")
class Parent2(GrandParents):
    def __init__(self):
        super(Parent2,self).__init__()
        print("this is Parent2")
class Child(Parent1,Parent2):
    def __init__(self):
        super(Child,self).__init__()
        print("this is Child")
#super 但我们重复继承一个父类的时候，
#我们使用super只会让我们继承的父类执行一次
c = Child()
'''
#用户画像
        #封装
            #私有化
            #__
'''
class Person(object):
    def __init__(self):
        self.__gender = "nan" #在类的属性名称前面加__
p = Person()
print(p.__gender)
p.__gender = "nv"
print(p.__gender)

class Person(object):
    def __init__(self):
        self.gender = "nan" #在类的属性名称前面加__
p = Person()
print(p.gender)
p.gender = "nv"
print(Person.gender)

class Person(object):
    def __init__(self):
        self.__gender = "nan" #在类的属性名称前面加__
    def show_gender(self):
        return self.__gender
    
p = Person()
print(p.show_gender())

class Person(object):
    def __init__(self):
        self.__gender = "nan" #在类的属性名称前面加__
        self.__age = 0    
    def __add_age(self): #私有的方法
        self.__age += 1
    def show_gender(self):
        return self.__gender
    def get_up(self):
        print("get_up")
        self.__add_age()
        print(self.__age)
    
p = Person()
print(p.show_gender())

class Person(object):
    def gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender
p = Person()
p.set_gender("男")
print(p.gender())
'''
# class Person(object):
#     def gender(self):
#         return self.__gender
#     def set_gender(self,gender):
#         if isinstance(gender,str) and gender in("男","女"):
#             self.__gender = gender
#         else:
#             raise TypeError("the gender must in (\"男\",\"女\")")
# p = Person()
# p.set_gender("hello")
# print(p.gender())

class Person(object):
    @property
    def gender(self): #1
        return self.__gender
    @gender.setter
    def gender(self,gender): #2
        if isinstance(gender,str) and gender in("男","女"):
            self.__gender = gender
        else:
            raise TypeError("the gender must in (\"男\",\"女\")")

p = Person()
p.gender = "女" #--->p.gender("女") 2
print(p.gender) #---->p.gender() 1
'''
p = Person()
p.gender = "男"
print(p.gender)

p = Person()
p.gender = "hello"
print(p.gender)
'''
        #多态

    
