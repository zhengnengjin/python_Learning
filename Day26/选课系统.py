#__author: ZhengNengjin
#__date: 2018/10/12
'''
class Teacher:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.salary = 100
		
class Course:
	def __init__(self, name, cost, teacher):
		self.name = name
		self.teacher = teacher
		self.cost = cost
	def class_up(self):
		self.teacher.salary += self.cost
		
t1 = Teacher('alex', 30)
t2 = Teacher('alvin', 30)
c1 = Course('linux', 1000, t1)
c2 = Course('Python', 500, t2)
print(c1.name)
print(c1.teacher.age)
print(c1.teacher.name)
print(c1.teacher.salary)
c1.class_up()
print(c1.teacher.salary)
'''

'''
角色：学校、学员、课程、讲师
要求：
1、创建北京、上海2所学校
2、创建linux、python、go、3个课程，linux/python在北京，go在上海
3、课程包含 周期、价格、通过学校创建课程
4、通过学校创建班级、班级关联课程、讲师
5、创建学员时，选择学校，关联班级
6、提供两个角色接口、
6.1学员视图，可以注册，交学费，选择班级、
6.2讲师试图，讲师可以管理自己的班级，上课时选择班级，查看班级学员，修改所管理的学员成绩
6.3管理试图，创建讲师，创建班级，创建课程
7上面的操作产生的数据都通过pickle序列化保存到文件里
'''

class School:
	
	def beijin(self):
	
	
	def shanghai(self):



































