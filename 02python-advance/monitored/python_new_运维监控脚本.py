#coding:gbk

#1、获取要监控的计算机的信息
    #os.system("command")
    #os.popen("command")
    #file open("/proc/file")
        #字符串要处理
            #注意特殊符号 \n
            #编码问题
                # +
                # join
                # "%s"%str
                # ("{}").format(a)
        #路径的处理
            #os.path
        #文件对象的处理
            #read
            #readline
            #readlines
        #Python基本的数据类型的转换
            #int
            #str
            #list
            #dict
            #tuple
        #监控的目标
            #cpu
            #内存
            #磁盘
            #系统的进程
        #监控的方式
            #1、采用我们之前的os,sys,file
            #2、psutil
                #1、是一个跨平台的库
                #2、可以获取到系统运行的进程和系统利用率
                #3、本身就是为了监控出现的

                #cpu
                    #User Time 执行用户进程的时间百分比
                    #System Time 执行内核进程和中断的时间百分比
                    #Wait IO 空闲时间比
                    #idle cpu处于idle状态的时间百分比
                        #cpu_times 返回cpu的完整信息
                            #percpu 默认为false
                            #percpu 为True 返回多个即列表形式
                            #cpu_times(percpu = True)返回
                        #cpu_count 返回cpu逻辑个数
                            #logical参数默认为True
                            #当logical参数为False返回的是物理个数
                #内存
                    #内存的总数(total)
                    #已经使用的内存数(used)
                    #空闲的内存数(free)
                    #缓冲使用数(buffers)
                    #缓存使用数（cache）
                    #交换分区使用数(swap)
                        #virtual_memory() 返回内存的完整信息
                #磁盘
                    #磁盘的利用率     
                    #IO信息
                        #disk_partitions() 获取磁盘的完整信息
                        #disk_usage() 获得分区的使用情况
                        #disk_io_counters() 获取磁盘总的io个数
                            #perdisk 默认为False
                            #为True 返回单个分区的io个数
                #系统的进程
                    #pids 返回系统进程pid
                    #Process 返回一个process对象，参数为进程的pid
                        #p = psutil.Process(1)
                    #p.name() 返会进程的名字
                    #p.exe() 返回进程bin文件位置
                    #p.cwd() 进程的工作目录的绝对路径
                    #p.status() 返回进程的状态
                    #p.create_time() 进程的创建时间，时间戳
                        #time.ctime()将时间戳转换为字符串时间
                    #p.uids() 返回进程的uid信息
                    #p.gids() 返回进程的gid信息
                    #p.cpu_times() 返回cup时间信息
                    #p.memory_info() 返回进程内存的利用率
                    #p.io_counters() 返回进程的io读写信息
                    
import urllib
import urllib2
test_data = {'ServiceCode':'aaaa','b':'bbbbb'}#利用字典构建传的数据的格式
test_data_urlencode = urllib.urlencode(test_data)#将构建好的数据进行编码 json
requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"
req = urllib2.Request(url = requrl,data =test_data_urlencode)#携带数据发出请求














        











                







