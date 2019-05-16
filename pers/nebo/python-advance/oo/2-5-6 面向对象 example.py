#coding:utf-8

class Person:
    age = 0
    def eat(self,food):
        print(self)
        print("we will eat %s"%food)

p = Person()
"""
print(p)
p = Person()
print(p)

p.eat("apple")#Person.eat(p)
              #Person.eat(p,"apple") 

class Person:
    age = 5 #类变量，静态变量
    def eat(self):
        self.age = 10 #self是实例，是实例变量
        Person.age = 10 #person 是类，是类变量

p = Person() #实例化并赋值给变量p
print(p.age) #p是实例，所以p.age是实例变量
p.eat() #他对个体p的年龄进行定制
print(p.age)
print(Person.age)
"""

#print(p.age)
#p.eat()
#print(p.age)
#print(Person.age)
#在python 的面向对象当中，
#类和实例以及实例和实例之间都是拥有独立的内存空间的

"""
class Person:
    age = 5 
    def eat(self):
        self.age = 10 

p1 = Person()
p2 = Person()

p1.eat()
print(Person.age)
Person.age = 8
print(Person.age)
p2.age = 15
print(p1.age)
print(p2.age)
"""
#python magic python 魔术方法
    #__method__
#class Model:
#    def method(self):
#        pass
    #构造函数
        #__init__ 初始化，在类被实例化之后自动执行
"""
class Person:
    def __init__(self):
        print("hello I am a person")
p = Person()

class Person:
    def __init__(self):
        self.age = 0
        print("hello world")
    def eat(self,food):
        print("A ha ha I like %s"%food)
        
p = Person()
print(p.age)
p.eat('banana')


class Person:
    def __init__(self,gender):
        self.age = 0
        self.gender = gender
        if gender == "nan":
            print("this is a boy")
        elif gender == "nv":
            print("this is a girl")
    def eat(self,food):
        print("A ha ha I like %s"%food)    


p = Person("nan")
p.eat("apple")

p1 = Person("nv")
p.eat("milk")

xiao_ming = Person("nan")
xiao_liu = Person("nv")

print(xiao_ming.gender)
print(xiao_liu.gender)


class Person:
    def __init__(self,gender):
        self.age = 0
        return self
p = Person("nan") #---> p = 0 p int
p.age
#1、构造函数是指类实例化之后自动执行的
#2、构造函数传参需要在实例化的过程中在类的括号当中传
#3、构造函数必须没有返回值


class Person:
    def __init__(self,gender):
        self.age = 0
        self.gender = gender
        #"nan" = self.gender
    def show_gender(self):
        print(self.gender)   
p = Person("nan") #__init__自动执行
p.show_gender()

#变量 = 值
"""

    #析构函数
        #__del__ 在实例被删除自动执行
"""
class Person:
    def __init__(self):
        print("hello world")
    def __del__(self):
        print("goodbye  world")

xiaoming = Person()
del xiaoming

class Bird:
    hungry = 10
    def __init__(self):
        Bird.hungry += 1
    def __del__(self):
        Bird.hungry -= 1
    def how(self):
        print(Bird.hungry)

b1 = Bird()
b1.how()
b2 = Bird()
b2.how()
b3 = Bird()

#del b3
b1.how()      
b2.how()
b3.how()


class Bird:
    hungry = 10
    def __init__(self):
        Bird.hungry += 1
    def __del__(self):
        Bird.hungry -= 1
    def how(self):
        print(self.hungry)

b1 = Bird()
b2 = Bird()
b3 = Bird()
        
b1.how()      
b2.how()
b3.how()
      
class Bird:
    hungry = 10
    def __init__(self):
        self.hungry += 1
    def __del__(self):
        self.hungry -= 1
    def how(self):
        print(self.hungry)

b1 = Bird()
b2 = Bird()
b3 = Bird()
        
b1.how()      
b2.how()
b3.how()    
"""
class Person:
    age = 10 #类变量
    def how_old(self):
        print(self.age) #实例变量

#如果实例变量有定义，那么实例变量采用自己的值
#如果实例变量没有定义，那么采用类变量的值
#如果类变量也没有定义，那么报错
#但是实例变量无法对其他实例的实例变量产生影响
#也不能对类变量产生影响
"""
class Bird:
    hungry = 10
    def __init__(self):
        self.hungry += 1
    def __del__(self):
        self.hungry -= 1
    def how(self):
        print(Bird.hungry)

b1 = Bird()
b2 = Bird()
b3 = Bird()

b1.how()
b2.how()
b3.how()

class bird:
   hungry=10
   def __init__(self):
     self.hungry+=1
   def __del__(self):
     bird.hungry-=1
   def how(self):
     print(bird.hungry)

b4=bird()
b5=bird()
b6=bird()

b4.how()
b5.how()
b6.how()
"""
class Person:
    age = 10
    def how(self):
        print(self.age)
        del Person.age
        

h = Person()
"""
h.how()
Person.age = 15
h.how()
print(h.age)
print(Person.age)

Person.gender = "Man"
print h.gender
"""
def how(self):
    print("hello world")
Person.how = how
h.how()

















        



