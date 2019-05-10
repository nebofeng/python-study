myfunc = lambda x,y:x+y
res = myfunc(1,2)
print(res)
myfunc1 = lambda x,y=1:x+y
res1 = myfunc1(2)
print(res1)
mylist = [lambda x:x**2,lambda x:x**3,lambda x:x**4]
res2 = mylist[0](2)
print(res2)
print('----------------')
for var in mylist:
    print(var(2))
print('----------------')
#跳转表
#func   #函数对象
#func() #函数调用
def func():
    print('func')
def func1():
    print('func1')
def func2():
    print('func2')
mylist1 = [func,func1,func2]
#给别人看起来不直观
mylist1[0]()
