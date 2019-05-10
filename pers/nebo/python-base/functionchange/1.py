a = 1
def func(num):
    num = 2#修改 赋值
    print('inside a is:',num)
def func1(num):
    num += 1#修改 加等于
    #针对与不可变数据对象 num += 1 == num = num + 1
    print('inside a is:',num)

def func2(num):
    num += 2  # 修改 加等于
    # 针对与不可变数据对象 num += 1 == num = num + 1
    print('inside a is:', num)
    return  num


print('外部的a是:',a)
func(a)
print('外部的a是:',a)

print('------------')
print('外部的a是:',a)
func1(a)
print('外部的a是:',a)

a=func2(a)
print('外部的a是:',a)
