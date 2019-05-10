from time import sleep
myfile = open(r'C:\Users\Administrator\Desktop\1.txt','w')#默认的打开权限就是r
#read->r
#write->w
#binary->b
myfile.write('abcabcabcabcabcabc\n')
myfile.write('------------------\n')#
myfile.flush()
sleep(7)
#代表程序要休眠
print('休息结束')
myfile.close()
#覆盖掉
#跟着
#换行重起一行