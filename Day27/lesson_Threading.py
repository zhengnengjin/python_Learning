#__author: ZhengNengjin
#__date: 2018/10/27

import time
import threading

# beg = time.time()
# def foo(n):
# 	print('foo%s'%n)
# 	time.sleep(1)
# 	print('end foo')
#
# def bar(n):
# 	print('bar%s'%n)
# 	time.sleep(3)
# 	print('end bar')
#
# print('hello')
# t1.join()
# t2.join()
# end = time.time()
# print(end - beg)

sta = time.time()
def add(n):
	sum = 0
	for i in range(n):
		sum +=i
	print(sum)
		
# add(30000000)
# add(50000000)

t1 = threading.Thread(target=add,args=(30000000,))
t2 = threading.Thread(target=add,args=(50000000,))
t1.start()# 可以放在任何位置
t2.start()
t1.join()
t2.join()

end = time.time()
print(end - sta)

