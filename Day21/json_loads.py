#__author: ZhengNengjin
#__date: 2018/10/2

import json

f = open('json_text', 'r')

data = f.read()
data = json.loads(data)


print(data['name'])



