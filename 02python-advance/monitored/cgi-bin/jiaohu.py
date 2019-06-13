#!F:\soft\python27\python
#coding:utf-8

import cgi

html = """
<html>
	<head>
		<title>
			cgi 	
		</title>
	</head>
	<body>
		<form action="" method="POST">
			<input type="text" name="name">
			<input type="text" name="age">
                        <input type="submit" value="submit">
		</form>
		<h3>
                    %s is %s years old 
                </h3>
	</body>
</html>
"""
#action 代表提交的位置，空为自己
#method 代表提交的的方式
#FieldStorage 负责接收cgi请求的参数
print("Content-type:text/html;Charset:utf8")
print()
request_data = cgi.FieldStorage()
try:
    name = request_data['name'].value
    data = request_data['age'].value
except:
    data = ""
    name = ""
print(html%(name,data))
