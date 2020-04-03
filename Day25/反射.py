#__author: ZhengNengjin
#__date: 2018/10/11

'''
class Foo:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def show(self):
		return "%s-%s"%(self.name, self.age)

obj = Foo('ZNJ', 22)
func = getattr(obj, 'show') #获取对象里面的值
# func = getattr(obj, 'name')
print(func)
r = func()
print(r)

print(hasattr(obj, 'name')) #判断对象里面是否有那个东西
setattr(obj, 'gender', 'male') #设置一个东西
print(obj.gender)
delattr(obj, 'name') #删除一个东西

'''
import s1
'''
r1 = s1.name
print(r1)
r2 = s1.func()
print(r2)

r3 = getattr(s1, 'name')
print(r3)
r4 = getattr(s1,'func')
print(r4())

cls = getattr(s1, 'Foo')
print(cls)
'''


# inp = input('请输入要查看的URL：')
# # if inp =='f1':
# 	# s1.f1()
#
# if hasattr(s1, inp):
#
# 	func = getattr(s1, inp)
# 	print(func())
# else:
# 	print('404')


'''
class Foo:
	def __init__(self,name,age):
		self.name = name
		self.age = age
#obj = Foo()# obj对象，obj也叫Foo类的实例（创建对象的过程是实例化）
obj1 = Foo()
obj2 = Foo()
obj3 = Foo()
#单例,永远使用一份实例（对象）
'''


class Foo:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def show(self):
		print(self.name, self.age)
v = None

while True:
	if v:
		v.show()
	else:
		v = Foo('znj', 22)
		v.show()
	

# class Foo:
# 	__v = None
# 	@classmethod
# 	def get_instance(cls):
# 		if cls.__v:
# 			return cls.__v
# 		else:
# 			cls.__v = Foo()
# 			return cls.__v
# obj1 = Foo.get_instance()
# print(obj1)
# obj2 = Foo.get_instance()
# print(obj2)
# obj3 = Foo.get_instance()
# print(obj3)
# #classmethod 创建单例实例



















	
	





















