#__author: ZhengNengjin
#__date: 2018/9/5

import time
f=open('静夜思','w',encoding='utf8') # w是write，清空之前的 内容，write新的，a是append，增加内容。
f.write("静夜思\n床前明月光\n疑是地上霜\n举头望明月\n低头思故乡\n")
f.write('zheng nengjin'.title())
print(f.fileno())
print(f.tell())
time.sleep(5)
f.close()