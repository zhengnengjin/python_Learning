#__author: ZhengNengjin
#__date: 2018/9/21

# def f(n):
# 	ret = 1
# 	for i in range(1,n+1):
# 		ret = ret * i
# 	return ret
#
# n = int(input("请输入一个数字："))
# f(n)
# print(f(n)) #实现阶乘的函数

#递归实现
def fact(n):
	if n==1:
		return 1
	return n * fact(n-1)


n = int(input("请输入一个数字："))
fact(n)
print(fact(n)) #递归实现阶乘的函数

'''关于递归的特性：
1调用自身函数
2有一个结束条件
凡是递归能实现的，循环都能实现
递归的效率在很多时间下很低'''


