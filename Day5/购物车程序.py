#author:ZhengNengjin
#date: 2018/8/29

product_lists = [
	('iphone6s',5800),
	('mac book',9000),
	('coffee',30),
	('python book',80),
	('bycle',1500),
]

saving = input('Please input your money:')
shopping_car = []
if saving.isdigit():
	saving =int(saving)
	while True:  # 打印商品内容
		for i,v in enumerate (product_lists,1):
			print(i,'<<<',v)  # 引导用户选择商品
		choice = input("请输入你要购买的东西的序号:[买完请输入q]：")  #验证输入是否合法
		
		if choice.isdigit():
			choice = int(choice)
			if choice > 0 and choice < len(product_lists): #将用户选择商品通过choice取出来
				p_item = product_lists[choice-1]  #如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
				if p_item[1] < saving:
					saving -= p_item[1]
					shopping_car.append(p_item)
				else:
					print('余额不足，您还剩%s'%saving)
				print(p_item)
			else:
				print('编码不存在')
		elif choice == 'q':
			print('----------您已购买以下商品----------') #循环遍历购物车里的商品，购物车存放的是已买商品
			for i in shopping_car:
				print(i)
			print('您还剩%s元'%saving)
			break
		else:
			print('退出')