#__author: ZhengNengjin
#__date: 2018/10/8
class Foo:
	def bar(self):
		print('bar')
		
	@staticmethod
	def sta():
		print('123')
		
	@staticmethod
	def stat(x, y):
		print(x, y)
		
	@classmethod
	def classmd(cls):
		print(cls)
		print('classmd')
		
Foo.sta()
Foo.stat(1,2)

Foo.classmd()

obj = Foo()
obj.bar()

'''
方法
 -普通方法，保存在类中，由对象来调用，self=>对象
 -静态方法，保存在类中，由类直接调用
 -  类方法，保存在类中，由类直接调用，cls=>当前类
 
 ###应用场景：
 如果对象中需要保存一些值，执行某功能时，
 需要使用对象的值 -> 普通方法
 不需要任何对象中的值 -> 静态方法'''