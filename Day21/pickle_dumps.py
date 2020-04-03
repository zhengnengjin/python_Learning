#__author: ZhengNengjin
#__date: 2018/10/2

import pickle

def foo():
	print('ok')
	
data = pickle.dumps(foo)

f = open('pickle_text', 'wb') # 把write改成write byte，将里面的内容写成字节的形式

f.write(data)


f.close()


















