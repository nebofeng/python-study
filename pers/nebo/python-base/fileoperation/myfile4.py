myfile = open(r'C:\Users\Administrator\Desktop\1.txt')#默认的打开权限就是r

strlist = myfile.readlines()

for var in strlist:
	var = var.strip()
	print(var)