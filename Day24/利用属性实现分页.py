#__author: ZhengNengjin
#__date: 2018/10/8

class Pergination:
	def __init__(self, current_page):
		try:
			p = int(current_page)
		except Exception as e:
			p = 1
			
		self.page = int(current_page)
		
	@property
	def start(self):
		val = (self.page-1) * 10
		return val
	@property
	def end(self):
		val = self.page * 10
		return val
	
list = []
for i in range(100):
	list.append(i)
	
while True:
	p = input('请输入要查看的页码：')
	obj = Pergination(p)
	
	print(list[obj.start:obj.end])
#前面有@property obj.start就不用加（）