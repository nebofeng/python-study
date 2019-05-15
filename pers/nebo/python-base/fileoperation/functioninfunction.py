def func():
	print('hello')
	def func1():
		print('world')
	return func1()
#func    #函数对象
#func()  #函数调用
func() #-> print('hello') -> def func1 -> return func1()