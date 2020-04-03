#__author: ZhengNengjin
#__date: 2018/10/8

class Base:
	def a(self):
		print('Base.a')
		
class F0(Base):
	def a1(self):
		print('F0.a')

class F1(F0):
	def a1(self):
		print('F1.a')
		
class F2(Base):
	def a1(self):
		print('F2.a')
		
class S(F1, F2): #继承取决于先后顺序
	pass

obj = S()
obj.a()
'''
子类多继承时，顺着左边的往上找，
如果遇到共同的根（Base），先找右边的 ，没有再找Base
'''




