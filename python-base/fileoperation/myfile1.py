myfile = open(r'C:\Users\Administrator\Desktop\1.txt','rb')#默认的打开权限就是r
#read
#mystr = myfile.read(10)
myfile.seek(-21,2)#修改文件读写指针
#文件末尾向前偏移9个
mystr1 = myfile.read(10)
print(mystr1)
#我们在读10个

