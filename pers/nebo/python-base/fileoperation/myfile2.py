myfile = open(r'C:\Users\Administrator\Desktop\1.txt')#默认的打开权限就是r

strlist = myfile.readlines()
#读到了一个列表
#print(strlist)
#print('----------------')
#print(strlist[1][:6:2])
for var in strlist:
	var = var[:-1]#前提是你确定你的换行符就是单个字符 
	#\r\n
	print(var)

myfile.close()

