#__author: ZhengNengjin
#__date: 2018/10/11
class MyType(type):
	def __init__(self, what, bases = None, dict = None):
		super(MyType, self).__init__(what, bases, dict)

	def __call__(self, *args, **kwargs):
		obj = self.__new__(self, *args, **kwargs)

		self.__init__(obj)
		
class Foo(object):
	__mateclass__ = MyType
	def __init__(self, name):
		self.name = name
		
	def __new__(cls, *args, **kwargs):
		return object.__new__(cls, *args, **kwargs)
	
obj = Foo(44)