#__author: ZhengNengjin
#__date: 2018/10/2

#---- json 和 pickle 只有两种方法，dumps和loads，加载过去用dumps，加载回来用loads

import json

dic = {'name':'znj', 'age':'22', 'hobby':'jtt'}

f = open('json_text', 'w')

data = json.dumps(dic)

f.write(data)


f.close()





















