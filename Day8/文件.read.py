#__author: ZhengNengjin
#__date: 2018/9/5

import time
f=open('静夜思','r',encoding='utf8')
for i in f.readlines():
	time.sleep(0.1)
	print(i.strip())


f.close()

# f=open('静夜思','r',encoding='utf8')
# for i in f:   #这是for内部将f对象做成了一个迭代器，迭代器就是需要的时候用一个 取一个
# 	print(i.strip())  #读取文件的最优方式，



