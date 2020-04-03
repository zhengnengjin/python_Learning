#author:ZhengNengjin
#date: 2018/8/29

#输入名字、年龄、工作、工资等属性，输出格式化的列表。
name=input("Name:")
age=int(input("Age:"))
job=input("Job:")
salary=input("Salary:")

if salary.isdigit(): #长得像不像数字，比如200d,'200'
	salary = int(salary)
else:
	exit("Salary must input ditgit !")
massage='''
-------- info of %s --------
Name: %s
Age : %s
Job : %s
Salary: %s
You will be retired in %s years
-------- end --------
''' % (name, name, age, job, salary, 65-age)

'''占位符%，%s s=string，%d d=digit 整数，%f f=float 浮点数，约等于小数'''

print(massage)
