#coding=utf-8
#import 模块名.函数名

#from import  从模块中导入一个指定的部分到当前命名空间中。
# 要导入模块 fib 的 fibonacci 函数，使用如下语句：
#    from fib import fibonacci

# from xx import *  把一个模块的所有内容全部导入到当前的命名空间。也是可行的。


#搜索路径 ：

# 1. 当前目录 2. 不在当前目录，搜索shell变量PYTHONPATH下的每个目录 3. 都找不到 默认路径 unix 一般为 /usr/local/lib/python/。
#模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

#命名空间和作用域

#函数内默认是局部变量，需要用global修饰 。才能被认为是全局变量 。


#dir() 函数
# 导入内置math模块
#dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。返回的列表容纳了在一个模块里定义的所有模块，变量和函数
import math

content = dir(math)

print content;

#输出的  特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。


# globals() 和 locals() 函数
# 根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
#
# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
#
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
#
# 两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。




# reload() 函数
# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
#
# 因此，如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块。语法如下：
#
# reload(module_name)
# 在这里，module_name要直接放模块的名字，而不是一个字符串形式。比如想重载 hello 模块，如下：
#
# reload(hello)



