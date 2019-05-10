myfunc = lambda x : x**3
#匿名函数
print(myfunc(2))
mylist = [lambda x : x**2,lambda x : x**3,lambda x : x**4]
#跳转表
mylist[0](3)
for var in mylist:
	print(var)
	print(var(2))

def func():
	print('----------')
mylist1 = [func]
mylist1[0]()

