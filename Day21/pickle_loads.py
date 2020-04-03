#__author: ZhengNengjin
#__date: 2018/10/2

import pickle

def foo():
	print('ok')

f = open('pickle_text', 'rb')

data = f.read()
data = pickle.loads(data)

data()


