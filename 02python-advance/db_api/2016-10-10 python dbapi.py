#coding:utf-8

#1、我们讲一下python对数据库的操作
    #MySQLDB
#2、我们将元类的一部分

    # 作用域和装饰器 讲完了
    # 面向对象 讲完了 补充元类
    # socket TCP UDP 讲完了 
    # DBAPI 
    # thread 多线程
        # select
        # twisted
            #我们需要用socket搭配thread select twisted写例子 
    #spider 爬虫
        #tcp/ip
        #re
        #xapth
        #beautifulsoup

        #分布式

import MySQLdb as sql
#python dbapi
    #数据库: 存储数据的仓库
        #这里的关系指的是字段

        #关系型数据库 
            #sqlserver
            #mysql
            #mariadb
            #oracle

        #NOSQL NOT ONLY SQL 非关系型数据库
            #monongo
            #redis

#本质上我们写的程序是对数据的处理

#学员管理系统
    #对学员信息的管理(存储，统计，分类)
    #对数据库当中的数据
        #增
        #删
        #改
        #查
#mysql 数据库
    #1、mysql 数据库的结构
        #1、mysql 的安装
        #2、进入数据库(mysql)
              #cmd
                #mysql -u 用户名 -p密码 -h 主机
                    #用户名：指的是登录mysql数据库的用户名
                            #1、在本地通常以root 最高权限用户登录
                            #2、mysql 默认不允许root远程登录
        #3、mysql当中
            #database 数据库
                #table 表
                    #field 字段
                        #data 数据
        
#mysql
    #数据库 school
        #student
            #id                 1
            #name               "while"
            #age                18 
            #gender             "nan"
        #teacher
            #id
            #name
            #age
            #gender

#mysql 基本命令
    #1、查看所有数据库
        #show databases;
    #2、创建数据库
        #create database dbname;
    #3、使用数据库
        #use dbname;
    #4、查看库当中的表
        #show tables;
    #5、创建数据表
        #filid int primary key auto_increment,name char(10)
        #create table table_name (
            #field_name field_type,
                #主键 primary key
                #自增长 auto_increment
            #);
    #6、对数据表里的数据进行操作
            #1、增
                #insert into table_name(field,)value(data)
            #2、删
                #delete from table_name where field = data;
            #3、改
                #update table_name set field = data where field = data;
            #4、查
                #select * from table_name;
                    # *代表所有字段，可以具体的写字段
                #desc table_name; 查看表结构

#python MySQLdb mysql 的关系
    #python 是一门脚本语言，我们用python写程序
    #mysql 是数据库，我们用数据库存数据
    #MySQLdb 是python用来操作mysql数据库的接口 它是一个三方的模块
        #pip install python-mysql
        #yum install python-mysql

    #1、安装python
        #python 交互式
    #2、安装mysqldb(2.x) pymysql(3.x)
        #import MySQLdb
    #3、安装mysql
        #mysql -u root -padmin
                    
#MySQLdb 的操作

#python 利用MySQLdb操作数据库的步骤
    #1、导入模块
import MySQLdb as sql
#as 别名
    #2、创建数据库连接对象
"""
con = sql.connect(
    host = "localhost", #host 主机，本机的主机名或者ip,指你连接的数据库的主机
    user = "root", #user 登录数据库的用户名称
    passwd="123456", #passwd 登录数据库用户名称对应的密码
    db="myexample" #你要操作的数据库的名称
    #charset = "utf-8" #编码
    #port = 3306 端口 默认3306
    )
    #3、实例化mysql游标
        #游标:是用来传递python对mysql的命令和接收mysql返回给python的数据的对象
cur = con.cursor()
    #4、利用游标执行数据库命令
cur.execute("select * from student")
    #5、接收数据库的返回
cur.fetchall() #接收所有的返回
cur.fetchone() #接收返回的1条
cur.fetchmany(number) #接收返回的指定条
    #6、关闭游标
cur.close()
    #7、提交对数据库的操作
con.commit() #提交
    #8、关闭数据库连接
con.close()
"""
"""
try:
    1+"1"
except Exception as e:
    print(e)


con = sql.connect(
    host = "localhost", 
    user = "root", 
    passwd="admin", 
    db="myexample" 
    )

cur = con.cursor()
sql = "select * from student;"
print(cur.execute(sql))#mysqldb 执行后返回该命令执行以后受影响的数据条数
response_data = cur.fetchall()
print(type(response_data[0][0]))
cur.close()
con.commit()
con.close()
"""
#1、在我们的工作当中我们使用数据库难点不在我们对数据库的操作上
    #我们使用数据库对业务逻辑进行合理的描述才是关键

    #功能 --> 需求
        #建模 --> 就是利用字段和关系对我们的需求进行正确的描述
        #1、听明白需求
        #2、按照需求把表建出来
        #3、都会数据库内的数据进行管理

#2、如果说我们只是在操作数据，我们也许遇到的第一个难点是字符串的拼接和数据结构的整理
    
#sql = "insert into %(table_name)s (%(field)s) valeu(%(values)s)"

#string = "%s is a %s,%s is %s years old"%("while","man","while",13)
#print(string)
#string = "%(name)s is a %(gender)s,%(name)s is %(age)s years old"%{"name":"while","age":13,"gender":"man"}
#print("%s%%"%100)


"""
sqls = " select * from student where name like '%%%s%%';"%'f'

con = sql.connect(
    host = "localhost", 
    user = "root", 
    passwd="admin", 
    db="myexample" 
    )

cur = con.cursor()
print(cur.execute(sqls))#mysqldb 执行后返回该命令执行以后受影响的数据条数
response_data = cur.fetchall()
print(type(response_data[0][0]))
cur.close()
con.commit()
con.close()

def find_name(name):
    sqls = " select * from student where name like '%%%s%%';"%name

    con = sql.connect(
        host = "localhost", 
        user = "root", 
        passwd="admin", 
        db="myexample" 
        )

    cur = con.cursor()
    print(cur.execute(sqls))#mysqldb 执行后返回该命令执行以后受影响的数据条数
    response_data = cur.fetchall()
    print(response_data)
    cur.close()
    con.commit()
    con.close()

find_name("i")
"""









                    






















                    
    












    






































