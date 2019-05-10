def func1():
	pass
def func():
	print('this is func')
	global func1 #把一个对象声明成全局的
	def func1():
		print('hello world')
	#return func1

#myfunc = func()
func()
func1()