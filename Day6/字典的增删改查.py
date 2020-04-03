# author:ZhengNengjin
# date: 2018/9/2

#字典两大特点：无序，键唯一

#创建字典
dic={'name':'znj','age':22}
print(dic)          #直接创建

dic0=dic.fromkeys(['host1','host2','host3'],'test')
print(dic0)            #fromkeys创建方法，列表里每个值作为各个键，后面的值（列表）作为每个键同统一的值。

dict #关键字创建



#字典的查找
dic1={'name':'znj', 'age':22, 'sex':'man'}
print(dic1['name'])
print(dic1.keys())
print(dic1.values())
print(dic1.items())
print(dic1.get('age'))
print(dic1.get('ages')) #没有键就是None
print('name'in dic1) # 字典里有就是Ture
print('names'in dic1) # 字典里没有就是False
print(list(dic1.keys())) #把字典里的键，查找并列为列表
print(list(dic1.values())) #把字典里的值，查找并列为列表


#字典的增加
dic2={}
dic2['name']='jtt'
dic2['age']=23
print(dic2)
a=dic2.setdefault('name','znj')
b=dic2.setdefault('ages',22)  #增加字典里面没有的键值对
print(a,b)
print(dic2)


#字典的修改
dic3={'name':'xbl','age':1}
print("the xbl is" + str(dic3['age']) + ".")
dic3['age']=2
print("the xbl is now" + str(dic3['age']) + ".")
dic3['name']='dbl'
dicc={'sex':'girl'}
dic3.update(dicc)  # update：类似于列表的extend，将新的字典扩展到旧的字典，如果重复了，就覆盖它。
print(dic3)



#字典的删除
dic4={'name':'znj','age':22,'sex':'man'}

del dic4['sex'] #方法一：del，完全删除某个键值对，不可使用它
print(dic4)

dic4.clear()  #方法二：clear，清空列表，列表还存在
print(dic4)

ret = dic4.pop('sex')  #方法三：pop，删除某个键值对并返回它，可使用这个值
print(ret)
print(dic4)

a = dic4.popitem()   #方法四：popitem，随机删除某个键值对，并以元组方式返回值...
print(a,dic4)

del dic4  #删除整个字典





