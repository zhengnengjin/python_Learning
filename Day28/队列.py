#__author: ZhengNengjin
#__date: 2018/12/31

import  queue

d = queue.Queue(3) #队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。


d.put('zhengnengjin',0)
d.put('jiangtingting',)
d.put('xbl') #调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为
#1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。

print(d.get())
print(d.get())
print(d.get())


import threading,time

# li=[1,2,3,4,5]

# def pri():
#     while li:
#         a=li[-1]
#         print(a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except:
#             print('----',a)
#
# t1=threading.Thread(target=pri,args=())
# t1.start()
# t2=threading.Thread(target=pri,args=())
# t2.start()








