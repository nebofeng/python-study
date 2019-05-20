'''

引用与拷贝
浅拷贝的方式:
浅拷贝 不会拷贝数据中的子对象
import  copy
切片，copy()

深拷贝：
深拷贝 会拷贝数据中的子对象
import  copy
copy.deepcopy()

'''


mylist=[1,2,3]


mylist1=mylist[:]
mylist1[0]=3
print(mylist,mylist1)