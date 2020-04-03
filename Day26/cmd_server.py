# __author: ZhengNengjin
# __date: 2018/10/14

import socket, subprocess

# family type
sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8888)  # IP地址和端口
sk.bind(address)  # sk 的bind方法 后面跟元组，绑定ip地址和端口
sk.listen(3)
print("服务端启动...")

while True:
	
	conn, address = sk.accept()  # 阻塞，直到客户端来链接
	print(address)
	
	while True:
		try:
			data = conn.recv(1024)  # *收数据
		except Exception:
			print("意外中断")
			break
		if not data: break
		print(str(data, 'utf8'))  # *打印数据
		
		obj = subprocess.Popen(str(data,'utf8'), shell=True, stdout=subprocess.PIPE)
		cmd_result = obj.stdout.read()
		
		result_len = bytes(str(len(cmd_result)),'utf8')
		conn.sendall(result_len)
		# inp = input(">>>")  # ** 输入数据
		conn.recv(1021) #解决粘包问题，隔断开两个send
		
		conn.sendall(cmd_result)  # **发送数据
	
sk.close()
