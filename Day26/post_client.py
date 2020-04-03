#__author: ZhengNengjin
#__date: 2018/10/16

import socket,os

sk = socket.socket()
# print(sk)
address = ('127.0.0.1', 8088)
sk.connect(address)

print("客户端启动:")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
	inp = input(">>>").strip()  # *  输入数据
	
	cmd, path = inp.split('|')
	path = os.path.join(BASE_DIR, path)
	filename = os.path.basename(path)
	file_size = os.stat(path).st_size
	file_info = 'post|%s|%s'%(filename, file_size)
	sk.sendall(bytes(file_info, 'utf8'))
	
	f = open(path, 'rb')
	has_sent = 0
	while has_sent !=file_size:
		data = f.read(1024)
		sk.sendall(data)
		has_sent += len(data)
	f.close()
	print("上传成功!")
sk.close()
print(sk)

