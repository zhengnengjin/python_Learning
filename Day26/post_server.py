#__author: ZhengNengjin
#__date: 2018/10/16

import socket,os

# family type
sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8088)  # IP地址和端口
sk.bind(address)  # sk 的bind方法 后面跟元组，绑定ip地址和端口
sk.listen(3)
print("服务端启动...")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
	
	conn, address = sk.accept()  # 阻塞，直到客户端来链接
	
	while True:
		data = conn.recv(1024)
		cmd, filename,filesize = str(data, 'utf8').split('|')
		path = os.path.join(BASE_DIR, '文件上传', filename)
		filesize = int(filesize)

		f = open(path, 'ab')
		has_recv =0
		while has_recv != filesize:
			data = conn.recv(1024)
			f.write(data)
			has_recv += len(data)
		f.close()
sk.close()
