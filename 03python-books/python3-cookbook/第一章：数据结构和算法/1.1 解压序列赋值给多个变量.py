#赋值给多个变量
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(date)
#如果参数不对应会报错

#可以使用占位符，只获取自己需要的变量
_, shares, price, _ = data
print(shares)