#__author: ZhengNengjin
#__date: 2018/10/8

class Foo:
	def __init__(self):
		self.name = 'a'
		# obj.name
		self.name_list = ['znj']
	
	#obj.bar()
	def bar(self):
		#self是对象
		print('bar')

	@property
	def perr(self):
		# print('123')
		del self.name_list[0]
		return 1
	
	#obj.per = 123
	@perr.setter
	def perr(self, val):
		print(val)
		
	@perr.deleter
	def perr(self):
		print('666')
	
obj = Foo()
r = obj.perr
print(r)
obj.perr = 123
del obj.perr




class Foo:
	def f1(self): #配fget
		return 123

	def f2(self, v): #配fset
		print(v)

	def f3(self): #配fdel
		print('del')



	per = property(fget=f1, fset=f2, fdel=f3, doc='asdasdsas')
	# @property    #fget = f1 等同于
	# def per(self):
	# 	return 123

obj = Foo()
ret = obj.per #配fget
print(ret)
obj.per = 123456 #配fset
del obj.per #配fdel









