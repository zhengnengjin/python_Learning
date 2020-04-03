#__author: ZhengNengjin
#__date: 2018/10/8

class BaseRequest():
	# pass
	def __init__(self):
		print('BaseRequest.init')                      #第三步

class RequestHandler(BaseRequest):
	def __init__(self):
		print('RequestHandler.init')                    #第二步
		BaseRequest.__init__(self)              #执行它父类的init
		
	def serve_forever(self):
		#self,是obj
		print('RequestHandler.serve_forever')            #第五步
		
	def process_request(self):
		print('RequestHandler.process_request')
		
class Minx:
	def  process_request(self):
		print('minx.process_request')                    #第六步
		
class Son(Minx, RequestHandler):
	pass

obj = Son()  #执行init                                   # 第一步
obj.serve_forever()                                      #第四步
