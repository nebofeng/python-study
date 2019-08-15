import xlrd
from xlutils.copy import copy
import os
# 导入xlwt模块
import xlwt
import re

# 创建一个Workbook对象，相当于创建了一个Excel文件
book = xlwt.Workbook(encoding="utf-8", style_compression=0)

'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。默认是ascii。
style_compression:表示是否压缩，不常用。
'''

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('test01', cell_overwrite_ok=True)

# 向表test中添加数据
# 合并第0行的第0列到第2列。前四个参数： 开始合并的行，结束合并的行，开始合并的列，结束合并的列
sheet.write_merge(0, 0,0,2, 'field_2')
#前两个参数：所在的行，所在的列
sheet.write(1, 31, "查询字段：条目： 时间")

book.save("filepath/filename")