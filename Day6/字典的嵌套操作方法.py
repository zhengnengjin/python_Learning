#author:ZhengNengjin
#date: 2018/9/2

字典的嵌套
ABC={
	'abcdef':{'ab':[123],
	          'cd':[456],
	          'ef':[789]
	},
	'ghijkl':{'gh':[321],
	          'ij':[654]
	},
	'mnopqr':{'mn':[213],
	          'op':[546],
	          'qr':[879]
	}
}
print(ABC)

av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog['欧美']["www.youporn.com"][1]='高清午马'


#嵌套字典的修改
# ABC['abcdef']['ab'][0]='2333'
# print(ABC)


#字典的排序
# dic={3:555,1:666,2:777}
# print(dic)
# print(sorted(dic))  #本身默认按键排序
# print(sorted(dic.keys()))
# print(sorted(dic.values())) #按值排序
# print(sorted(dic.items()))  #默认按键排序


#（重要）字典的遍历
dic1={'name':'znj','age':22,'hobby':'jtt'}
# for i in dic1:
# 	print(i,dic1[i])    #输出i和i所对应的值，最快速，最高校的方法，推荐使用
#
for i,v in dic1.items():
	print(i,v)          #输出items里面的所有值。有个把字典转换为列表的过程，速度慢

	
#5 其他操作以及涉及到的方法


# dic={5:'555',2:'666',4:'444'}
# # dic.has_keys(5)
# print(5 in dic)
# print(sorted(dic.items()))
# dic5={'name': 'alex', 'age': 18}


# for i in dic5:
#     print(i,dic5[i])
#
# for i,v in dic5.items():
#     print(i,v)