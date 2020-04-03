#__author: ZhengNengjin
#__date: 2018/9/19

def print_info(*args, **kwargs) :
	print(args)    # *args 是把未命名的存储为元组
 	# print(kwargs)  # **kwargs是把已命名的键值对作为字典存储
	
	
	#关于不定长参数位置：“args放左边，kwargs放右边”
	#如果有默认参数放最左边
	
	for i in kwargs:
		
		print('%s : %s' %(i,kwargs[i]) )
		
print_info('zhengnengjin', 22, sex = 'male', job = 'student',hobby = 'jtt')
