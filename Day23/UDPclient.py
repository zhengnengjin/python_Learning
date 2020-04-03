from socket import *
host = 'localhost'
port = 8888
buff = 1024
addr = (host, port)
uc = socket(AF_INET, SOCK_DGRAM)
while True:
	data = input(">>>")
	if not data:
		break
	uc.sendto(bytes(data,'utf8'), addr)
	data, addr = uc.recvfrom(buff)
	if not data:
		break
	print(data)
uc.close()