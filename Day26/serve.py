#__author: ZhengNengjin
#__date: 2018/10/14

# import socket
# #family type
# sk = socket.socket()
# print(sk)
# address = ('127.0.0.1', 8000) # IP地址和端口
# sk.bind(address) #sk 的bind方法 后面跟元组，绑定ip地址和端口
# sk.listen(2)
# print('writing...')
# conn,address = sk.accept() #阻塞，直到客户端来链接
#
# while True:
#
# 	inp = input(">>>")#** 输入数据
# 	conn.send(bytes(inp,'utf8'))#**发送数据
#
# 	data = conn.recv(1024) #*收数据
# 	print(str(data,'utf8'))#*打印数据\
# 	if not data:
# 		conn.close()
# 		conn, address = sk.accept()
# 		print(address)
# 		continue
#
#
# sk.close()


from socket import *

address = ('', 8000)  # IP地址和端口
# family type 两个参数
sk = socket()
print(sk)

sk.bind(address)  # sk 的bind方法 后面跟元组，绑定ip地址和端口
sk.listen(3)

while True:
	print('waiting for connect...')
	conn, address = sk.accept()  # 阻塞，直到客户端来链接
	print(address)
	
	while True:
		try:
			data = conn.recv(1024)  # *收数据
		except Exception :
			print("意外中断")
			break
		print(str(data, 'utf8'))  # *打印数据
		# if not data: break
		
		inp = input(">>>")  # ** 输入数据
		conn.send(bytes(inp, 'utf8'))  # **发送数据

	conn.close()


















