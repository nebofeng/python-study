myfile = open(r'C:\Users\Administrator\Desktop\1.txt')#默认的打开权限就是r
#read
mystr = myfile.read(10)
myfile.seek(-1,0)#修改文件读写指针
mystr1 = myfile.read(10)
#默认read函数不加参数 是全读
print(mystr)
print(mystr1)
#\U \A \D 
myfile.close()
#mysql数据句柄 线程回收
