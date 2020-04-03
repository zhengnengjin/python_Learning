#__author: ZhengNengjin
#__date: 2018/10/2

import shelve

f = shelve.open('shelve_text')

f['info'] = {"name": "alex", "age": "22"}

data = f.get('info')# data = f['info']

print(data)



#关于get的用法

d = {"name": "alex", "age": "22"}

print(d.get('name'))
print(d.get('sex'))




