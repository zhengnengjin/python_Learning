from socket import *
from time import ctime
host = ''
port = 8888
buff = 1024
ADDR = (host, port)
us = socket(AF_INET, SOCK_DGRAM)
us.bind(ADDR)

while True:
	print("waiting...")
	data, addr = us.recvfrom(buff)
	us.sendto(bytes('[%s] %s' %(ctime(), data),'utf8'),addr)
	print('...rfaft:',addr)

us.close()