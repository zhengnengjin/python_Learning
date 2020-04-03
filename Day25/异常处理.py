#__author: ZhengNengjin
#__date: 2018/10/11


try:
	
	#代码块，逻辑
	list = [11,22,33]
	list[999]
	int('ddd')
except ValueError as e: #except，用于捕获异常
	print(e)
except IndexError as e:
	print(e)
except Exception as e:
	print(e)
	#上述代码块如果出错，自动执行当前块内容

 
'''主动触发异常'''
# try:
# 	#主动触发异常
# 	raise Exception('sss')
# except Exception as e:
# 	print(e)


'''
def db():
	return False

try:
	i =input(">>>")
	int(i)
	result = db()
	if not result:
		# r = open('rzjl','a')
		# r.write('clcw')
		raise Exception('clcfffw\n')
except Exception as e:
	str_error = str(e)
	print(str_error)
	r = open('rzjl', 'a')
	r.write(str_error)
'''

# '''自定义异常'''
# class ZhengNengjinError(Exception):
# 	def __init__(self, msg):
# 		self.message = msg
#
# 	def __str__(self):
# 		return self.message
#
# try:
# 	raise ZhengNengjinError('郑能锦')
# except ZhengNengjinError as e:
# 	print(e)
#
# '''assert条件，断言，用于强制用户服从，可以捕获，但是一般不捕获'''
# print(6)
# assert 1==1
# print(456)
#
	
	

	
	
	















