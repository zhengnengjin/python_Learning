#__author: ZhengNengjin
#__date: 2018/9/22

'''装饰器函数'''
import time
def logger(flag): #展示日志记录的装饰器函数
	def show_time(func): #展示运行时间的装饰器函数
		def inner(*x, **y):  # inner是一个闭包函数
			start = time.time()
			func(*x, **y)
			end = time.time()
			print('spend %s ' % (end - start))
			if flag == 'true':
				print('日志记录')
		return inner
	return show_time
#############################################
@logger('true') # @show_time # 等价于 foo = show_time(foo)
def foo():
	print('ZhengNengjin')
	time.sleep(1)

foo() #没有参数的前面装饰器也不要参数

def add(*a,**b):
	sums = 0
	for i in a:
		sums += i
	print(sums)
	time.sleep(1)
	
add(1,2,8,5,0,4,9,0)

