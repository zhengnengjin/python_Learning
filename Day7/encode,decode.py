#__author: ZhengNengjin
#__date: 2018/9/3

# Py3：str   bytes

# str: unicode

# bytes: 十六进制

a = 'hello郑能锦'
print(type(a)) # <class 'str'>

'''str>>>>>bytes : 编码'''

b = bytes(a,'utf8') #utf8规则下的bytes类型
print(b) #b'hello\xe9\x83\x91\xe8\x83\xbd\xe9\x94\xa6'

b2 = a.encode('utf8')
print(b2)#b'hello\xe9\x83\x91\xe8\x83\xbd\xe9\x94\xa6'


'''bytes>>>>>str : 解码'''

#解码的第一种方式
a = str(b2, "utf8")
print(a) #hello郑能锦

#解码的第二张方式
a2 = b2.decode("utf8")
print(a2) #hello郑能锦




'''按照什么规则编码就得按照什么规则解码'''






