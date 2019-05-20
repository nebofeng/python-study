class Myerror(Exception):
	pass
try:
	a = 1
	b = 2
	if a != b:
		raise Myerror('your args is not equal')
		#抛出异常
except Myerror as error:
	print('a == b',error)
try:
	a = 1
	b = 2
	if a != b:
		raise IndexError
		#抛出系统已经定义好的
except IndexError:
	print('********')