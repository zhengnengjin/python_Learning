#__author: ZhengNengjin
#__date: 2018/9/2

menu = {
	"福建省":{
		"福州市":{"仓山区","台江区","晋安区","马尾区"},
		"厦门市":{"思明区","海安区","湖里区","集美区","同安区"},
		"泉州市":{"鲤城区","丰泽区","洛江区","泉港区"},
		"南平市":{"延平区","建阳区"},
		"三明市":{"梅列区","三元区"}
	},
	"安徽省":{
		"合肥市":{"蜀山区","庐阳区","包河区","瑶海区","政务区"},
		"铜陵市":{"铜官区","义安区","郊区","野区"},
		"安庆市":{"太湖县","潜山县","怀宁县","宿松县","岳西县"},
		"六安市":{"舒城县","金寨县","霍山县","霍邱县"}
	},
	"浙江省":{
		"杭州市":{"上城区","下城区","西湖区","萧山区","余杭区"},
		"宁波市":{"海曙区","江东区","江北区","镇海区","北仑区"},
		"温州市":{"鹿城区","龙湾区","瓯海区","洞头区"}
	}
}
back_flag = False
exit_flag = False
while not back_flag and not exit_flag :
	for key in menu :
		print(key)
	choice = input("1>>>:").strip()
	if choice == 'Q':
		exit_flag = True
	if choice in menu:
		while not back_flag and not exit_flag:
			for key2 in menu[choice]:
				print(key2)
			choice2 = input("2>>>:").strip()
			if choice2 == 'B':
				back_flag = True
			if choice2 == 'Q':
				exit_flag = True
			if choice2 in menu[choice] :
				while not back_flag and not exit_flag:
					for key3 in menu[choice][choice2]:
						print(key3)
					choice3 = input("3>>>:").strip()
					
					print("last level !")
					if choice3 == 'B':
						back_flag = True
					if choice3 == 'Q':
						exit_flag = True
						break
				else:
					back_flag = False
		else:
			back_flag = False

