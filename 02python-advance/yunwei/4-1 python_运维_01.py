#coding:gbk

#python 运维实战

#需求:
    #1、利用python实现自动监控服务器性能
    #2、并将监控到的数据进行处理，上传到指定web服务器上

#用到的知识点
    #python 流程控制
        #for
        #while
        #if
            #break
            #continue
            #pass
    #python 面向对象及面向过程开发
        #class
        #def
    #python 模块导入
        #import
        #配置文件
    #python os模块
        #os.system 执行系统命令,但是不返回结果
        #os.popen 执行系统命令，但是以文件的形式返回结果
        #os.listdir 返回指定目录下的文件和目录
        #os.sep 取代操作系统特定的路径分割符,用于跨平台
        #os.getcwd 获取当前的工作目录
        #os.remove 删除文件
        #os.chdir 修改执行路径
        #os.mkdir 创建目录
        #os.path.join 路径拼接
        #os.path.isfile 判断是否是文件
        #os.path.isdir 判断是否是文件夹
        #os.path.split 路径切分
        #os.path.dirname 返回指定的目录
        #os.rename 修改名称
    #python sys模块
import sys
        #sys.argv 接收外部的参数
            #返回一个列表，第一个元素是文件名
            #之后的参数来至于调用文件是外部传的参数
        #sys.path 返回系统的导入路径
        #sys.exit 退出运行
    #标准输出、输入、错误
        #sys.stdout 标准输出 输出，但是不换行
"""
for i in range(10):
    print(str(i))
for j in range(10):
    sys.stdout.write(str(j))
"""    
        #sys.stdin 标准输入
            #a = raw_input(">>>")
        #sys.err 标准错误
    #重定向



    #python cgi
        #做简单的web接收服务器
    #python socket
        #tcp
        #udp
    #python pickle 持久性，序列化
        #dump 序列化
        #load 反序列化
    #python urllib
        #发送post请求
        
    #python 捕获异常
        #try
        #except
        #Exception
        #else
        #finally
    #python 对文件的操作
        #file
    #python queue队列
        #queue
        #lifoqueue

    #linux 基础命令
        #ls 列出文件的目录
        #uname 查看内核版本
        
    






    
