#__author: ZhengNengjin
#__date: 2018/10/8

class Province:
	
	#静态字段，属于类
	country = 'China'
	
	def __init__(self, name):
		#普通字段，属于对象
		self.name = name
		
	# def show(self):
	# 	print(self.name) 	#普通方法
	
print(Province.country)
# print(Province.name)

fujian = Province('福建')
anhui = Province('安徽')
print(fujian.name)
print(anhui.name)
'''
类成员：
#字段
 -普通字段，保存在对象中，执行只能通过对象访问
 -静态字段，保存在类中，执行可以通过对象也可以通过类访问
 

 #方法
 
 
 '''