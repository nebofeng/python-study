myfile = open(r'C:\Users\Administrator\Desktop\1.txt','w')#默认的打开权限就是r

strlist = ('abc\n','123\n','---\n')

myfile.writelines(strlist)


#myfile.close()
#进程结束，打开的文件自动关闭
#python中的功能实现 有一些是通过C语言
#还有一些python自己实现的
