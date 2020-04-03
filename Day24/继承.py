#__author: ZhengNengjin
#__date: 2018/10/8

class F:
	def f1(self):
		print('F.f1')
		
	def f2(self):
		print('F.f2')
		
		
class S(F):
	def s1(self):
		print('S.s1')
		
	def s2(self):
		super(S, self).f2()  #执行父类中的f2方法之一（推荐）
		print('S,s2')
		F.f2(self)          #执行父类中的f2方法之一
		
obj = S()
# obj.s1() #s1中的self是形参，此时代指obj
obj.s2() #self用于指调用方法的调用者

"""
1、继承
class 父类
	pass
class 子类
	pass
	
2、重写
防止执行父类中的方法

3、self永远是执行该方法的调用者

4、super（子类，self）.父类中的方法
	父类名.父类中的方法（self,...）
	
5、python中支持多继承
a、左侧优先
b、一条道走到黑
c、同一个根时，根最后执行
"""