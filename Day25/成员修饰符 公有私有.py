#__author: ZhengNengjin
#__date: 2018/10/9
'''
class Foo:
	def __init__(self, name, age):
		self.name = name
		# self.age = age
		self.__age = age
		
	def show(self):   # 只能通过内部访问私有字段
		print(self.name)
		print(self.__age)
	
obj = Foo('znj', 22)
obj.show()
'''


'''
class Foo:  #静态字段私有化
	__v = '123'
	def __init__(self):
		pass
	
	def show(self):
		return Foo.__v
	
	@staticmethod
	def stat():
		return Foo.__v
	
print(Foo().show())
print(Foo().stat())
'''


'''
class Foo:
	def __f1(self):
		return 123
	
	def f2(self):
		r = self.__f1()
		return r

obj = Foo()
print(obj.f2())
'''


'''
class F:
	def __init__(self):
		self.a = 123
		self.__b = 456
		
class S(F):
	def __init__(self, name):
		self.name = name
		self.__age = 22
		super(S, self).__init__()
		
	def show(self):
		print(self.name)
		print(self.__age)
		print(self.a)
		print(self.__b)  # 继承的也无法从外部访问私有字段
		
		
obj = S('znj')
obj.show()
'''
