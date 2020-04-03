#author:ZhengNengjin
#date: 2018/8/29

_user = "ZhengNengjin"
_passwd = "15103442"

counter = 0

while counter < 3:
	username = input("Username:")
	password = input("Password:")

	if username == _user and password == _passwd:
		print("Welcome %s login..." % _user)
		break
	else:
		print("滚！")
	counter += 1
	if counter == 3:
		keep_going_choice = input("还想玩么？[y/n]")
		if keep_going_choice =="y":
			counter = 0
else: #（如果不用flag标志位，直要上面的for循环正常执行，中间没有被打断，就会执行else语句）
	print("要不要脸")