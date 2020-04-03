#__author: ZhengNengjin
#__date: 2018/9/21

'''1,1,2,3,5,8,13,21,34,55,89...'''
# def fibo(n):
# 	before = 0
# 	after = 1
# 	for i in range(n-1):
# 		ret = before + after
# 		before = after
# 		after = ret
#
# 	return ret

# print(fibo(8))
# **************递归*********************
def fibo_new(n):  # n可以为零，数列有［0］

	if n <=1:
		return n
	return (fibo_new(n - 1) + fibo_new(n - 2))

print(fibo_new(8))

print(fibo_new(3))  # maximum recursion depth exceeded in comparison