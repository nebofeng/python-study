mylist = [1,2,3] #定义了一个列表
def func(obj):#传递了一个可变对象，相当于传递了一个值
    obj = ['a','b','c']#重新赋值
    print('inside a is:',obj)
def func1(obj): #原地址 传递一个可变对象，相当于传递了引用
    obj += ['a','b','c'] #拼接修改 修改了原址的值 加等于
    #后面我们会遇到的一些内置函数，直接修改可变对象本身的内置函数
    #比如 list.append() list.extend()那么是直接修改了可变对象
    print('inside a is:',obj)
    #可变数据对象使用了+= 就是修改了原址的值
func(mylist)#传参
print('外部的a修改完成后是:',mylist)
print('------------------')
mylist = [1,2,3]
func1(mylist)#传参
print('外部的a修改完成后是:',mylist)
#可变对象你如果直接修改 是修改了其本身

#入门的程序员： 语法错误 : , N -> n
#中级程序员：返回值不对，函数调用不对了 bug
#高级程序员：设计模式了 可扩展性 结合业务
#文件操作  txt 文本操作
