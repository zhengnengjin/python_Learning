#__author: ZhengNengjin
#__date: 2018/9/21

def f(n):
	return  n * n

def foo(a, b, func):
	
	ret = func(a) +func(b)
	return  ret

print(foo(1,2,f))