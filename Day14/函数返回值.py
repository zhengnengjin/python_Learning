#__author: ZhengNengjin
#__date: 2018/9/19

def add(*args):
	Sum = 0
	for i in args:
		Sum += i
	print(Sum)
	return Sum
	
add(1,2,5,8)

#注意点：1函数里如果没有reture，会默认返回一个None
		#2如果return多个对象，python会帮我们把多个对象封装成一个元组返回一个对象

