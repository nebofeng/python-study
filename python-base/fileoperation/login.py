#登录
user_file = open(r'C:\Users\Administrator\Desktop\文件操作续集\user_info.txt')
islogin = 0 #标志位
while True:
	if islogin == 0:
		account = input('请输入你要登录的帐号：')
		user_file.seek(0,0)
		for user in user_file:
			if user.split(':')[0] == account:
				passwd = input('请输入你要登录的密码：')
				#做密码核对的功能
				if user.split(':')[1].strip() == passwd:
					print('登录成功')
					islogin = 1
					break
				else:
					passwd_index = 1
					while passwd_index < 3:
						print('密码检查失败,请重新输入,你还剩余的次数为:',3-passwd_index)
						passwd = input('请输入你要登录的密码：')
						if user.split(':')[1].strip() == passwd:
							print('登录成功')
							islogin = 1
							break
						passwd_index+=1
					break
		else:
			print('没有这个用户,您需要注册一下')
	else:
		break
user_file.close()


