import time
import datetime
#=============================1.time模块===================================
"""
time模块中主要提供了很多和时间相关的函数，和一个类：struct_time 

#1.时间戳
时间戳 - 指定的时间到1970年1月1日0时0分0秒的时间差，单位是秒

a.使用时间戳的场景
1.节约时间存储成本
1543545814.62544 - 8字节
"2018/11/30 10:51:34" - 20字节+18字节 一个字符两个字节
2.方便对时间进行加密


"""
#1.获取当前时间（单位：秒）- 以时间戳的形式返回
result=time.time()
print(result)

#2.获取本地时间
"""
localtime() - 获取当前本地时间
localtime(时间戳)- 将时间戳转换成struct_time对象
"""
result =time.localtime()
print(result)
print("%s-%s-%s"%(result.tm_year,result.tm_mon,result.tm_mday))
result=time.localtime(0)
print(result)

#3.格式时间

"""
strftime(时间格式，struct_time时间对象) - 将时间对象转换成指定格式的时间字符串

时间格式 - 字符串，字符串中带有相应的时间格式，用来获取指定的时间值
%Y - 年
%m - 月
%d - 日

时间对象 - struct_time

time.strptime(字符串，时间格式) -返回时间对象
"""
time_str =time.strftime("%Y-%m-%d" , time.localtime())
print("time_str=",time_str)

time_str=time.strptime("2018-11-30","%Y-%m-%d")
print("===",time_str)

from datetime import datetime ,time ,date,timedelta
"""
datetime 模块中主要包含三个类
date（日期） - 只能对(年月日)对应的时间进行表示和操作
time（时间） - 只能对(时分秒)对应的时间进行表示和操作
datetime（日期和时间）能对(时分秒/年月日)对应的时间进行表示和操作
"""
date1=date.today()
print(date1.year,date1.month,date1.day)

time1 =datetime.now()
print(time1) #2018-11-30 12:06:50.695103

"""
date和datetime对象支持时间的加减操作:

时间对象+
时间对象-
"""
print(time1+timedelta(seconds=1000000))

#将字符串转换成datetime对象
time2=datetime.strptime("2018-12-31 23:59:10", "%Y-%m-%d %H:%M:%S")
print(time2+timedelta(seconds=50))

print(datetime.tzinfo)

