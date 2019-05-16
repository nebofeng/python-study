#coding:utf-8

#class 是我们定义类的关键字
#Person 是我们定义类的名称
#() 继承,如果没有继承对象，我们可以吧括号省略掉
"""
def person():
    pass

class Person:
    gender = "man" #域 属性
    def eat(self): #方法 属性
        print("ahhh")
"""
#类是对事物的划分，我们使用的是类的实例
#所以我们调用类又叫做类的实例化
#在实例化的过程当中，括号的作用是传参
#类名加上括号就是实例化        
#xm = Person()
#Person()
#print(Person)
#print(Person())
#print(Person())
#xm =Person()
#range(10).append(1)
#print(range(10))
#垃圾回收机制
#1 a = 1
#del a
#xm = Person()
#print(xm)
#print(Person)
#xm.eat()
#Person.eat()
#Person().ear()
#print(xrange(10))

class Person:
    def eat(self):
        print(self)
'''
p1 = Person()
p2 = Person()
print(p1)
p1.eat()

print(p2)
p2.eat()

p1 = Person()
Person.eat(p1)

#self 就是实例本身        
#example
class Person:
    number = 10
    def eat(self):
        #print(Person.number)#类的变量
        print(self.number) #
p1 = Person() #实例化Person，实例是p1
p2 = Person() #实例化Person，实例是p2

print("Person:%s"%Person.number) #打印类的number
print "p1_eat:",
p1.eat() #执行p1实例的eat方法
print "p2_eat:",
p2.eat() #执行p2实例的eat方法

print("p1:%s"%p1.number) #打印p1实例的number
print("p2:%s"%p2.number) #打印p2实例的number

p1.number += 1 #对p1实例的number加1
p2.number -= 1 #对p2实例的number减1

print("p1:%s"%p1.number) #打印p1实例的number
print("p2:%s"%p2.number) #打印p2实例的number

print "Person.number:",
print(Person.number) #打印类的number
print "p1_eat:",
p1.eat() #执行p1实例的eat方法
print "p2_eat:",
p2.eat() #执行p2实例的eat方法
'''
class Person:
    def eat(self):
        return(self)

#p1 = Person()
#p1.eat()
#Person.eat(p1)

"""
p1 = Person()
p2 = Person()

print(p1)
print(p1.eat())
print(p1 == p1.eat())
print(p1 is p1.eat())
print("+++++++++++++++++++++++")
print(p2)
print(p2.eat())
print(p2 == p2.eat())
print(p1 is p1.eat())
#self 就是实例本身

string = "hello world"
print(string.upper())
print(str.upper(string))

#isinstance 判断指定变量是否是指定类或者类型的实例
class Person:
    def eat(self):
        return(self)
p1 = Person()
p2 = "hello"
print(isinstance(p1,Person))
print(isinstance(p2,str))

string = "hello world"
print(isinstance(string,str))
print(string.upper())
print(str.upper(string))

class Person:
    def eat(self):
        return(self)

p1 = Person()
p1.eat() #----> Person.eat(p1)
p1.eat(p1)

print(p1)
print(p1.eat())
print(p1 == p1.eat())
print(p1 is p1.eat())
print("+++++++++++++++++++++++")
print(p2)
print(p2.eat())
print(p2 == p2.eat())
print(p1 is p1.eat())
#self 是实例本身

class Person:
    def eat(self):
        return(1)


p1 = Person()
#print(p1.eat()+=1)
#a = 0
#a+=1 #---> a = a+1
p1.eat() == 1
"""

class Person:
    def eat(self):
        return(self)

p1 = Person()
#p1.eat() #----> Person.eat(p1)
print(p1.eat())
print(p1)
print(p1.eat() == p1)
print(p1.eat() is p1)
#       self  
#p1.eat()-->Person.eat(p1)-->return p1
print(id(p1.eat()) == id(p1))






        



