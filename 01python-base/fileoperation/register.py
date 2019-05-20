user_file = open(r'C:\Users\Administrator\Desktop\文件操作续集\user_info.txt','a+')
#单纯只以a模式打开文件是不可读的
user_list = user_file.readlines()
#保存了文件中所有的帐号和密码
while True:
	account = input('请输入你要注册的帐号：')
	for user in user_list:
		if user.split(':')[0] == account:
			print('已经被注册,需要重新注册')
			break#只能跳出来最内层循环
	else:# 遍历完完整个 用户列表之后，如果没有break说明没有这个用户
	#只有当for循环正常执行完之后 才会执行这里
		passwd1 = input('请输入你要注册的密码：')
		passwd2 = input('请再次输入你要注册的密码：')
		if passwd1 != passwd2:
			print('密码不一致，请重新注册')
			continue
		user_info = '%s:%s\n'%(account,passwd1)
		user_file.write(user_info)
		print('注册成功了!')
		break
		#注册成功 就不需要在注册了，直接跳出了while
user_file.close()
