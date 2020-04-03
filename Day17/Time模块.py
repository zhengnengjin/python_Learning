#__author: ZhengNengjin
#__date: 2018/9/27

import time

# print(help(time))

# print(time.time()) #时间戳 ***
#
# time.sleep(3)
#
# print(time.clock()) #计算CPU执行的时间

# print(time.gmtime()) #结构化时间
#
print(time.localtime())#本地时间

struct_time = time.localtime()

print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time)) #字符串时间******

# print(time.strptime('2018-09-28 19:00:00','%Y-%m-%d %H:%M:%S'))
#
# a = time.strptime('2018-09-28 19:00:00','%Y-%m-%d %H:%M:%S')
# print(a.tm_year)
# print(a.tm_mday)
# print(a.tm_wday)
# print(a.tm_mon)

# print(time.ctime(9999999999)) #输入数字，秒钟转化为1970.8.00开始的时间
#
# print(time.mktime(time.localtime())) #将时间转化为秒钟

import datetime
print(datetime.datetime.now())









