#__author: ZhengNengjin
#__date: 2018/10/9

class F:
	def __init__(self):
		print('init')
		
	def __call__(self, *args, **kwargs): # 对象后面加俩（）自动执行
		print('call')
		
	
obj = F()
obj()
print(F.__dict__)







