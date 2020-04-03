#__author: ZhengNengjin
#__date: 2018/10/14

import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8888)
sk.connect(address)

print("客户端启动:")

while True:
	inp = input(">>>")  # *  输入数据
	if inp == 'exit':
		break
	sk.sendall(bytes(inp, 'utf8'))  # *发送数据
	result_len = int(str(sk.recv(1024),'utf8'))
	sk.sendall(bytes('111','utf8')) #对应前面的解决粘包问题
	print(result_len)
	data = bytes()
	while len(data)!= result_len:
		recv = sk.recv(1024)  # **收数据
		data+=recv

	print(str(data, 'gbk'))  # **打印数据

sk.close()
print(sk)










