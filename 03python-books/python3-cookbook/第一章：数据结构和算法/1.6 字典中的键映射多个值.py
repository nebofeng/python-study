#怎样实现一个键对应多个值的字典（也叫 multidict）？

#可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。
# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。比如：

from collections import defaultdict

#允许多个重复
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(2)
d['b'].append(4)


#重复 只有一个
dset = defaultdict(set)
dset['a'].add(1)
dset['a'].add(1)
dset['b'].add(4)
print(d)
print(dset)


#需要注意的是， defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
'''
映射是指 k v 对应
https://www.cnblogs.com/colorfulday/p/10833078.html


defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值：

>>> dd['foo']
[]
>>> dd
defaultdict(<type 'list'>, {'foo': []})
>>> dd['bar'].append('quux')
>>> dd
defaultdict(<type 'list'>, {'foo': [], 'bar': ['quux']})
需要注意的是，这种形式的默认值只有在通过dict.__getitem__(key)访问的时候才有效
https://www.cnblogs.com/jidongdeatao/p/6930325.html

'''

# 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。比如：

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)



#一般来讲，创建一个多值映射字典是很简单的。但是，如果你选择自己实现的话，那么对于值的初始化可能会有点麻烦， 你可能会像下面这样来实现：

pairs=[('a',"b"),('a',"c")]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
#如果使用 defaultdict 的话代码就更加简洁了：

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)