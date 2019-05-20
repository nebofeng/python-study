#coding=utf-8
def printme(parameters ):
    "打印传递进函数的字符串"
    print(parameters)
    return

printme("Hello Python !")

# python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
# 比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#
# 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print(b) # 结果是 2


# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print ("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print("函数外取值: ", mylist)


#参数  ： 必备参数 ， 关键字参数 ， 默认参数 ， 不定长 参数


#必备参数， 需要传递参数进去函数


# 关键字参数 。传递参数的时候 。形如 ： str=""  参数名，参数值一起传入 。
printme( parameters ="sss") #如果是多个参数。顺序可以随意
#缺省参数 （默认参数）没传递age的时候有默认值
def function(name,age=35):
    print (name,age)

    return;

# 不定长参数 加了 *的变量名字会存放所有未命名的变量参数
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;

a = 1
def func():
    a = 2
    print('函数内部的a是:',a)
func()
print('函数外部的a是:',a)


def func1():
    global  a
    a = 2
    print('函数内部的a是:',a)
func1()
print('函数外部的a是:',a)



import copy
mylist = [1,2,3]
def func3(obj):
    obj = ['a','b','c']
    print('inside a is:',obj)
def func2(obj):
    obj = copy.deepcopy(obj)
    obj = ['a','b','c']
    #我们把这个列表 深拷贝给了 obj
    print('inside a is:',obj)

func3(mylist)#传参
print('外部的a修改完成后是:',mylist)
print('------------------')
mylist = [1,2,3]
func2(mylist)#传参
print('外部的a修改完成后是:',mylist)






