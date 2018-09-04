#coding=utf-8

class Employee:
    '所有员工的基类'
    empcount=0

    def __int__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount +=1;

    def displayCount(self):
        print "Total Employee %d"  %Employee.empcount

    def displayEmployee(self):
        print "name :",self.name,",Salary: ",self.salary

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()