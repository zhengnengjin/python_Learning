#__author: ZhengNengjin
#__date: 2018/9/28
'''加密模块'''
import hashlib

m = hashlib.md5()# md5算法
print(m)

m.update('hello woeld'.encode('utf-8'))
print(m.hexdigest())
m.update('znj'.encode('utf8'))
print(m.hexdigest())

m2 = hashlib.sha1() #sha 算法
m2.update('hello world'.encode('utf8'))
print(m2.hexdigest())
