import copy
mylist = [1,2,3]
def func(obj):
    obj = ['a','b','c']
    print('inside a is:',obj)
def func1(obj):
    obj = copy.deepcopy(obj)
    obj = ['a','b','d']
    #我们把这个列表 深拷贝给了 obj
    print('inside a is:',obj)

func(mylist)#传参
print('外部的a修改完成后是:',mylist)
print('------------------')
mylist = [1,2,3]
func1(mylist)#传参
print('外部的a修改完成后是:',mylist)
