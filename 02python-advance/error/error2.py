class Myerror(Exception):
	pass

a = 1
b = 2
if a != b:
	raise Myerror('your args is not equal')