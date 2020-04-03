#author:ZhengNengjin
#date: 2018/8/29

#编写一个登陆窗口，输入正确的用户名密码即可登入，登陆三次错误则程序退出。

_user="ZhengNengjin"
_passwd="15103442"

passed_authentication = False #假，不成立。（flag=标志位）

for i in range(3):
	
	username = input("Username:")
	password = input("Password:")
	
	if username == _user and password == _passwd:
		print("Welcome %s login..."%_user)
		passed_authentication = True #（真，成立）。
		break
	else:
		print("滚！")
if not passed_authentication: #只有在True的情况下，条件成立。
	print("要不要脸")

# _user = "ZhengNengjin"
# _passwd = "15103442"
#
# for i in range(3):
#
# 	username = input("Username:")
# 	password = input("Password:")
#
# 	if username == _user and password == _passwd:
# 		print("Welcome %s login..." % _user)
# 		break
# 	else:
# 		print("滚！")
# else: （如果不用flag标志位，直接加一个else，即可，只要上面的for循环正常执行，中间没有被打断，就会执行else语句）
# 	print("要不要脸")
