#__author: ZhengNengjin
#__date: 2018/10/7

class DateBaseHelper:
	def __init__(self, ip, port, username, pwd):
		self.ip = ip
		self.port = port
		self.username = username
		self.pwd = pwd
		print(ip, port, username, pwd)
		
	def add(self, content):
		'''利用self中封装的用户名、密码等 链接数据'''
		print(content)
		'''关闭数据链接'''
		
	def delete(self, content):
		'''利用self中封装的用户名、密码等 链接数据'''
		print('content')
		
		'''关闭数据链接'''
	def update(self, content):
		'''利用self中封装的用户名、密码等 链接数据'''
		print('content')
		'''关闭数据链接'''
		
	def get(self, content):
		'''利用self中封装的用户名、密码等 链接数据'''
		print('content')
		'''关闭数据链接'''
b1 = DateBaseHelper('1.1.1.1', 3306, 'znj', 123)
b1.add('sss')