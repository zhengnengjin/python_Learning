#__author: ZhengNengjin
#__date: 2018/10/12
import pickle

'''嵌套'''
class F1:
	def __init__(self):
		self.name = 'znj'
		
class F2:
	def __init__(self, a):
		self.aa = a
		
class F3:
	def __init__(self, b):
		self.bb = b
		
f1 = F1() # [name=123]
f2 = F2(f1) #[aa=[name=123]]
f3 = F3(f2)   # [bb=[aa=[name=123]]]
f3.bb.aa.name

data = pickle.dumps(F1)

f = open('test', 'wb') # 把write改成write byte，将里面的内容写成字节的形式

f.write(data)


f.close()
