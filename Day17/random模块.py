#__author: ZhengNengjin
#__date: 2018/9/28

import random
# print(random.random())
# print(random.randint(1,8))# 包括最后面的数
# print(random.randrange(1,3)) #不包括最后面的数
print(random.choice(['123',4,[5,6]]))
print(random.sample(['123',4,[5,6]],2))
print(chr(65))
#
# '''五位随机验证码'''
# def v_code():
# 	code = ''
# 	for i in range(5):
# 		add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
# 		code += str(add)
# 	print(code)
#
# v_code()





