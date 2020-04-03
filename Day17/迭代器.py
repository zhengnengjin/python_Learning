#__author: ZhengNengjin
#__date: 2018/9/26
'''for循环内部迭代过程'''
# g = fib(6)
# while True:
#   try:
# 		x = next(g)
# 		print('g:', x)
# 	except StopIteration as e:
# 		print('Generator return value:',e.value)
# 		break
#
# 输出：
# g:1
# g:1
# g:2
# g:3
# g:5
# g:8
# Generator return value:done


'''
迭代器
满足迭代器协议:
1内部有next方法
2内部有iter()方法
'''
#生成器都是迭代器，迭代器不一定是生成器
#list, tuple, dict. string : Iterable(可迭代对象)

from collections import Iterator, Iterable
'''Iterable：可迭代对象，Iterator：迭代器，'''
print(isinstance(2,list))   # isinstance 用来判断前面的参数是不是那个类型

l = [1, 2, 3, 4, 5]
d = iter(l)
print(d)
'''l：是一个可迭代对象但不是迭代器，d是迭代器也是可迭代对象'''
print(isinstance(l,list))
print(isinstance(l,Iterable))
print(isinstance(l,Iterator))
print(isinstance(d,Iterator))