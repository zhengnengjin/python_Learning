#__author: ZhengNengjin
#__date: 2018/10/1

import re
def format_string(string):
	string = string.replace(' ', '') #去空格，用非空格替换空格
	string = string.replace('++', '+')
	string = string.replace('--', '+')
	string = string.replace('-+', '-')
	string = string.replace('+-', '-')
	string = string.replace('*+', '*')
	string = string.replace('/+', '/')
	return string

#检查表达式合法性
def check(string):
	check_result = True
	#括号是否匹配
	if not string.count('(') == string.count(')'):
		print("表达式错误，括号未闭合!")
		check_result = False
	if re.findall('[a-z]+', string.lower()):
		print("表达式错误，包含非法字符!")
		check_result = False
	
	return check_result

def cal_mul_div(s):#(3+5*6/2-5)
	string = ''
	regular = '\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
	while re.search(regular, string):
		#获取表达式
		expression = re.search(regular,string).group()
		
		#如果是乘法
		if expression.count("*")==1:
			#获取要计算的两个数
			x,y = expression.split("*")
			#计算结果
		mul_result = str(float(x)*float(y))
		#将计算的表达式替换为计算结果值
		string = string.replace(expression,mul_result)
		#格式化一下
		string = format_string(string)
		
		#如果是除法
		if expression.count("/"):
			#获取要计算的两个数
			x,y = expression.split("/")
			#计算结果
		div_result = str(float(x)/float(y))
		#将计算的表达式替换为计算结果值
		string = string.replace(expression,div_result)
		#格式化一下
		string = format_string(string)
		
		if expression.count('*')==2:
			x,y = expression.split('**')
			pow_result = 1
			for i in range(int(y)):
				pow_result*=int(x)
			string = string.replace(expression,str(pow_result))
			string = format_string(string)
	return  string
			
	# ret1 = re.search('\d+\.?\d*[*/]\d+\.?\d*',s)
	# #0.5/3.9
	# x,y = re.split('[*/]',ret) #'0.5' '3.9'
	#
	# ret2 = float(x)/float(y)
	# str(ret2)#
	# s.replace(ret1,ret2)
	# return s

def cal_add_sub(string):# 3+15-5
	#定义正则表达式
	add_regular = '[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
	sub_regular = '[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'
	
	#开始加法
	while re.findall(add_regular, string):
		#把所有的加法都算完，获取所有加法表达式
		add_list = re.findall(add_regular, string)
		for add_str in add_list:
			#获取两个加法的数
			x, y = add_str.split('+')
			add_result = '+'+ str(float(x)+float(y))
			string = string.replace(add_str,add_result)
		string = format_string(string)
		
	#开始减法
	while re.findall(sub_regular, string):
		#把所有的加法都算完，获取所有加法表达式
		sub_list = re.findall(sub_regular, string)
		for sub_str in sub_list:
			numbers = sub_str.split('-')
			if len(numbers) == 3:
				result = 0
				for v in numbers:
					if v:
						result -= float(v)
			else:
				x, y = numbers
				result = float(x) - float(y)
			string = string.replace(sub_str, sub_result)
		string = format_string(string)
	return string

if __name__ == "__main__":
	source = input('请输入你要计算的公式：')
	
	
	if check(source):
		print("source:", source)
		print("my result is:", eval(source))
		source = format_string(source)
		print(source)
	
		while source.count("(") > 0:
			#格式化
			#去括号，得到括号的字符串，
			strs = re.search('\([^()]*\)',source).group()
			
			replace_str = cal_mul_div(strs)
			
			replace_str = cal_add_sub(replace_str)
			
			source = format_string(source.replace(strs,replace_str[1:-1]))
			
		else:
			#没有括号就到最后单一表达式
			replace_str = cal_mul_div(source)
			#乘除法
			replace_str = cal_add_sub(replace_str)
			#加减法
			source = source.replace(source,replace_str)
		# print("my result is :",source.replace('+',''))
		
	









