#__author: ZhengNengjin
#__date: 2018/9/21

'''reduce (func(x), str )
reduce: 将序列中的两个值x， y传入前面的函数中使用，再将新值与第三个值传入函数中使用，以此类推。'''

from functools import reduce
# def add(x,y):
# 	return x+y
# print(reduce(add, range(1,101)))


'''filter (function函数名字, sequence序列)
遍历序列中的每一个函数作为参数传进去'''

# str=['a','b','c','d']
# def func(s):
# 	if s != 'a':  #等于：过滤掉，不等于，返回
# 		return s
#
# ret = filter(func, str)  #ret是一个迭代器 ，迭代器是一个容器，装着你的内容
# print(list (ret))
# print(ret)



'''map (function, sequence)
把序列里的每一个遍历结果做一个处理，加一个字符串返回'''

# str = ['a', 'b', 'c']
# def fun(s):
# 	return s +'znj'
#
# ret = map(fun,str)
# print(list(ret))



'''lambda: 匿名函数，后面跟参数，有几个跟几个，然后冒号后面是代码块'''

def add(a, b):
	return a+b #普通函数

add = lambda a,b:a+b
print (add(2,3)) # lambda函数


print(list(map(lambda x, :x*x,range(1,6))))