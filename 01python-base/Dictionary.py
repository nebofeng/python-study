#coding=utf-8

#{} 是字典 。字典可以覆盖修改。删除可以删除单个元素 del 还可以 删除整个词典 。 .clear() 方法
mydict1 = dict(([1, 'a'], [2, 'b']))
print(mydict1)

mydict2 = dict.fromkeys((1,2,3),'a')
print(mydict2)

str1 = ['import','is','if','for','else','exception']
a={key:val for key,val in enumerate(str1)}
print(a)

M = [[1,2,3],[4,5,6],[7,8,9]]#求m中3，6，9组成的列表
b=[x[2] for x in M]
print(b)