#__author: ZhengNengjin
#__date: 2018/10/2

import json

dic = {'name':'alex', 'age':'22', 'hobby':'jtt'}

f = open('json_text', 'w')

data = json.dump(dic,f)


f.close()

f = open('json_text', 'r')

data = json.load(f)  # data = f.read()
					# data = json.loads(data)




print(data['name'])


