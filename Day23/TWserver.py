#__author: ZhengNengjin
#__date: 2018/10/25
from nntplib import NNTP
n = NNTP('your.nntp.server')
rsp, ct, fst, lst, grp = n.group('comp,lang.python')
rsp, anum, mid, data = n.article('110457')
for eachLine in data:
	print(eachLine)
n.quit()