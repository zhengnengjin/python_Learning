#__author: ZhengNengjin
#__date: 2018/10/4

class Bar:
	def foo(self, arg):
		print(self, self.name, self.age, self.gender, arg)
		
z1 = Bar()
print(z1)
z1.name = 'znj'
z1.age = '22'
z1.gender = 'male'
z1.foo(666)

# z2 = Bar()
# z2.name = 'jtt'
# z2.age = '23'
# z2.gender = 'female'
# z2.foo(666)