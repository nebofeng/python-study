myfile = open(r'C:\Users\Administrator\Desktop\1.txt')#默认的打开权限就是r

for mystr in myfile:
	print(mystr)

#文件迭代访问
#按照行来读取的