"""
try:
    a = int(input(">>>")) #python 3 input == python 2 raw_input
    a+0
except:
    a = None
    print("a error")
else:
    print(a)
finally:
    if a:
        print("a is number")
    else:
        print("a is not number")
"""
#raise

"""
def hello(a)
    if a.isdigit(): #判断字符串是否完全由数字组成
        print("this is number")
    else:
        print("a must be number")
a = input(">>>")
hello(a)

def hello(a):#如果a必须是一个数字，否则程序终止
    if a.isdigit(): #判断字符串是否完全由数字组成
        print("this is number")
    else:
        print("a must be number")
        raise TypeError("a must be number")
a = input(">>>")
hello(a)

class MyError(Exception):
    pass

a = 0.0
if a == 0:
    raise MyError("a be not 0")
"""
#NameError TypeError AttributeError KeyError IOError ValueError
f = open("e:\\1.txt","a")
print(f.closed)
f.close()
print(f.closed)







