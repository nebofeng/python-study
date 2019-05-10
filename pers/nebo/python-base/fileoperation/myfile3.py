myfile = open(r'C:\Users\Administrator\Desktop\1.txt')#默认的打开权限就是r

mystr = myfile.readline()
print(mystr)
mystr1 = myfile.readline()
print(myfile.tell())
print(mystr1)
mystr2 = myfile.readline()
print(mystr2)
mystr3 = myfile.readline()
print(mystr3)
mystr4 = myfile.readline()
print(mystr4)
myfile.close()
#\n在文本中写出来和实际在ascii码中的是不一样的
