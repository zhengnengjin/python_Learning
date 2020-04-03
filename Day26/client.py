#__author: ZhengNengjin
#__date: 2018/10/14

from socket import *

sk = socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)
print ("客户端启动:")

while True:
	inp = input(">>>")  # *  输入数据
	if inp == 'exit':
		break
	sk.sendall(bytes(inp, 'utf8'))  # *发送数据
	
	data = sk.recv(1024)#**收数据
	print(str(data,'utf8'))#**打印数据
	

sk.close()
print(sk)
