#coding=utf-8
import  time
localTime=time.time()
showTime=time.localtime(localTime)
print(localTime)
# print showTime
# print time.localtime()
#
# print time.asctime(showTime)
# # 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
now_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
end_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
while(int(end_time)-int(now_time)<60):
    print("==========")
    end_time= time.strftime("%Y%m%d%H%M%S", time.localtime())