record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
#使用* 号来匹配所有的电话number
name, email, *phone_numbers = record


#解压出的 phone_numbers 变量永远都是列表类型，不管解压的电话号码数量是多少（包括 0 个）

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing,current)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record