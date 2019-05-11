#eval
def jia(x,y):
	return (x+y)
def jian(x,y):
	return (x-y)
def cheng(x,y):
	return (x*y)
def chu(x,y):
	return (x/y)
func_dict = {'+':jia,'-':jian,'*':cheng,'/':chu}
#字典的value是函数
result = 0
while True:
	num1 = int(input('请输入你的第一个数字:'))
	#input 接受到的是什么数据类型？
	num2 = int(input('请输入你的第二个数字:'))
	oper = input('请输入你要做的计算操作:')
	if oper not in func_dict:
		#判断的是key值
		print('你输入的这个操作符不正确')
		continue
		#continue 可以跳过后面的语句
	# 代码 笔记 视频 课堂有 百度云也有 
	# 心里依靠别人
	result = func_dict[oper](num1,num2)
	print('结果是:',result)