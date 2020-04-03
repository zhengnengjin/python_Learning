#__author: ZhengNengjin
#__date: 2018/9/19
a = set([1,2,3,4,5,])
b = set([4,5,6,7,8])
print(a.intersection(b)) # a和b的交集
print(a.union(b))   #a和b的联合
print(a.difference(b))  #a与b的差集
print(b.difference(a))  #b与a的差集
print(a.symmetric_difference(b))    #a和b的差集和
print(a-b)
print(b-a)
print(a^b)  #a和b的差集和