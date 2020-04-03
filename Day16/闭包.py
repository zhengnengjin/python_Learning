#__author: ZhengNengjin
#__date: 2018/9/22

def outer():
	x = 10
	def inner():#条件一：inner就是内部函数
		print(x)  #条件二：外部环境的一个变量
		
	return inner #结论：内部函数inner是一个闭包

f = outer()
f()