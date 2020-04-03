#__author: ZhengNengjin
#__date: 2018/9/25

#生成器就是一个可迭代对象（Tterable）
'''生成器一共有两种创建方式'''
#1、（x*2 for x in range（10））()用括号!
#2、yiled

#next方法
# def fib(max):
# 	n, before, after, = 0, 0, 1
# 	while n < max:
# 		#print(before)
# 		yield ( before)
# 		before, after, = after, before+after
# 		n = n +1
#
# g = fib(8)#生成器地址
# print(g)
# print(next(g))# g.__next__()-
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#################################

# send方法
def bar():
	print('ok1')
	count = yield 1
	print(count)
	yield 2

b = bar() #<generator object bar at 0x0000024F4CD08390>
print(b)
b.send(None)#next(b) 第一次send前如果没有next，只能传一个send（None）和next一样的
ret = b.send('eeee')
print(ret)
# iter()



