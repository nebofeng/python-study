def func1():
    #pass#啥都不敢 直接过
    print('hello world')
    #return 不写的话 是默认返回了None
def func():
    print('我要在函数内部生成一个函数')
    global func1    #局部作用域里的函数对象也是可以global
    def func1():
        print('我是函数内部生成好的func1')
func()
func1()
#python 里面一切皆对象
