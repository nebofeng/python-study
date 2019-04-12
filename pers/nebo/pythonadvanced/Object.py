# #coding=utf-8
#
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print "Total Employee %d" % Employee.empCount
#
#     def displayEmployee(self):
#         print "Name : ", self.name,  ", Salary: ", self.salary
#
#
# # class Employee:
# #     '所有员工的基类'
# #     empcount=0
# #
# #     def __int__(self,name,salary):
# #         self.name = name
# #         self.salary = salary
# #         Employee.empcount +=1;
# #
# #     def displayCount(self):
# #         print "Total Employee %d"  %Employee.empcount
# #
# #     def displayEmployee(self):
# #         print "name :",self.name,",Salary: ",self.salary
#
# # class Test:
# #     def prt(self):
# #         print(self)
# #         print(self.__class__)
# #
# # t = Test()
# # t.prt()
#
#
#
# emp1 = Employee( "Zara", 2000)
# emp1.displayEmployee()
# # emp1.age = 7  # 添加一个 'age' 属性
# # emp1.age = 8  # 修改 'age' 属性
# # del emp1.age  # 删除 'age' 属性
#
# # 你也可以使用以下函数的方式来访问属性：
# #
# # getattr(obj, name[, default]) : 访问对象的属性。
# # hasattr(obj,name) : 检查是否存在一个属性。
# # setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# # delattr(obj, name) : 删除属性。
# # hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
# # getattr(emp1, 'age')    # 返回 'age' 属性的值
# # setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
# # delattr(emp1, 'age')    # 删除属性 'age'
#
#
# # Python内置类属性
# # __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# # __doc__ :类的文档字符串
# # __name__: 类名
# # __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# # __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组
#
#
# # print "Employee.__doc__:", Employee.__doc__
# # print "Employee.__name__:", Employee.__name__
# print "Employee.__module__:", Employee.__module__
# # print "Employee.__bases__:", Employee.__bases__
# # print "Employee.__dict__:", Employee.__dict__
# # 执行以上代码输出结果如下：
# #
# # Employee.__doc__: 所有员工的基类
# # Employee.__name__: Employee
# # Employee.__module__: __main__
# # Employee.__bases__: ()
# # Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}
#
# # 类的继承
# # 面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
# #
# # 通过继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
# #
# # 继承语法
# #
# # class 派生类名(基类名)
# #     ...
# # 在python中继承中的一些特点：
# #
# # 1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
# # 2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
# # 3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# # 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
# #
# # 语法：
# #
# # 派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
# #
# # class SubClassName (ParentClass1[, ParentClass2, ...]):
#
#
#
