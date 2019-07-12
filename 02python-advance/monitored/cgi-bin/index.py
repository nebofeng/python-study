#!F:\soft\python27\python
#coding:utf-8


html = """
<html>
	<head>
		<title>
			it's worked	
		</title>
	</head>
	<body>
		<h2>
			it's worked
		</h2>
                <img src="/img/1.jpg">		
	</body>
</html>
"""
print("Content-type:text/html") #告诉cgi回应的类型
print() #告诉客户端头部结束
print(html)
