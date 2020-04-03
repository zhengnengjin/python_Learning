#__author: ZhengNengjin
#__date: 2018/10/15

import subprocess

import subprocess

a=subprocess.Popen("ipconfig", shell=True,stdout=subprocess.PIPE )#stdout=subprocess.pipe从子进程转到主进程
#可以用cd，config，dir等等cmd命令
print(str(a.stdout.read(),'gbk'))





