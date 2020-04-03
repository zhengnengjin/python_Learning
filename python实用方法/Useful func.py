##############一些实用的python方法################

# 1检查重复元素
# def all_unique(lst):
#     return len(lst) == len(set(lst))
#
# # 2检测两个字符串是否互为变位词（即互相颠倒字符顺序）
# from collections import Counter
#
# def anagram(first, second):
#     return Counter(first) == Counter(second)
#
# # 3检查对象的内存使用情况。
# import sys
# variable = '50ee'
# # print(sys.getsizeof(variable))
#
# # 4重复打印字符串N次
# def more_print(n):
#     s ="Programming"
#     return s * n
#
# # 6.使用 title() 方法将字符串内的每个词进行首字母大写。
# s = "programming is awesome"
# # print(s.title()) # Programming Is Awesome
#
# # 7.分块使用 range() 将列表分块为指定大小的较小列表。
# from math import ceil
# def chunk(lst, size):
#     return list(map(lambda x: lst[x * size:x * size + size], list(range(0, ceil(len(lst) / size)))))
# # print(chunk([1,2,3,4,5],2)) # [[1,2],[3,4],5]
#
# # 8.使用 fliter() 删除列表中的错误值（如：False, None, 0 和“”）
# def compact(lst):
#     return list(filter(bool, lst))
# compact([0, 1, False, 2, '', 3, 'a', s, 34]) # [ 1, 2, 3,  a ,  s , 34 ]


# 10.链式比较以下代码可以在一行中用各种操作符进行多次比较。
# a = 3
# print( 2 < a < 8) # True
# print(1 == a < 2) # False

# 11.逗号分隔  以下代码段可将字符串列表转换为单个字符串，列表中的每个元素用逗号分隔。
# hobbies = ["basketball", "football", "swimming"]
# print("My hobbies are: " + ", ".join(hobbies)) # My hobbies are: basketball, football, swimming

# # 13.首字母恢复小写  以下方法可用于将给定字符串的第一个字母转换为小写。
# def decapitalize(string):
#     return string[:1].lower() + string[1:]
# decapitalize('FooBar') #  fooBar
# decapitalize('FooBar') #  fooBar

# # 14.平面化 使用递归来展开潜在的深度列表。
# def spread(arg):
#     ret = []
#     for i in arg:
#         if isinstance(i, list):
#             ret.extend(i)
#         else:
#             ret.append(i)
#     return ret
# def deep_flatten(lst):
#     result = []
#     result.extend(
#         spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
#     return result
# deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

# 15.差异该方法只保留第一个迭代器中的值，从而发现两个迭代器之间的差异。
def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
difference([1,2,3], [1,2,4]) # [3]

# # 16.寻找差异下面的方法在将给定的函数应用于两个列表的每个元素后，返回两个列表之间的差值。def difference_by(a, b, fn):
#     b = set(map(fn, b))
#     return [item for item in a if fn(item) not in b]
# from math import floor
# difference_by([2.1, 1.2], [2.3, 3.4],floor) # [1.2]
# difference_by([{  x : 2 }, {  x : 1 }], [{  x : 1 }], lambda v : v[ x ]) # [ { x: 2 } ]
#
# # 17.链式函数调用以下方法可在一行中调用多个函数。
# def add(a, b):
#     return a + bdef subtract(a, b):
#     return a - ba, b = 4, 5
#     print((subtract if a > b else add)(a, b)) # 9
#
# # 18.检查重复值以下方法使用 set() 方法仅包含唯一元素的事实来检查列表是否具有重复值。
# def has_duplicates(lst):
#     return len(lst) != len(set(lst))
#
# x = [1,2,3,4,5,5]
# y = [1,2,3,4,5]
# has_duplicates(x) # True
# has_duplicates(y) # False\
#
# # 19.合并两个词典以下方法可用于合并两个词典。
# def merge_two_dicts(a, b):
#     c = a.copy()   # make a copy of a
#     c.update(b)    # modify keys and values of a with the ones from b
#     return c
# a = {  x : 1,  y : 2}
# b = {  y : 3,  z : 4}
# print(merge_two_dicts(a, b)) # { y : 3,  x : 1,  z : 4}
# # 在Python 3.5及更高版本中，你还可以执行以下操作：
# def merge_dictionaries(a, b)
#    return {**a, **b}
# a = {  x : 1,  y : 2}
# b = {  y : 3,  z : 4}
# print(merge_dictionaries(a, b)) # { y : 3,  x : 1,  z : 4}
#
# # 20.将两个列表转换成一个词典以下方法可将两个列表转换成一个词典。
# def to_dictionary(keys, values):
#     return dict(zip(keys, values))
#
# keys = ["a", "b", "c"]
# values = [2, 3, 4]
# print(to_dictionary(keys, values)) # { a : 2,  c : 4,  b : 3}
#
# # 21.使用枚举以下方法将字典作为输入，然后仅返回该字典中的键。list = ["a", "b", "c", "d"]
# for index, element in enumerate(list):
#     print("Value", element, "Index ", index, )
# # ( Value ,  a ,  Index  , 0)
# # ( Value ,  b ,  Index  , 1)
# #( Value ,  c ,  Index  , 2)
# # ( Value ,  d ,  Index  , 3)
# # 22.计算所需时间以下代码段可用于计算执行特定代码所需的时间。import time
# start_time = time.time()
# a = 1
# b = 2
# c = a + b
# print(c) #3
# end_time = time.time()
# total_time = end_time - start_time
# print("Time: ", total_time)
# # ( Time:  , 1.1205673217773438e-05)
#
# # 23.Try else 指令你可以将 else 子句作为 try/except 块的一部分，如果没有抛出异常，则执行该子句。
# try:
#     2*3
# except TypeError:
#     print("An exception was raised")
# else:
#     print("Thank God, no exceptions were raised.")
# #Thank God, no exceptions were raised.
#
# # 24.查找最常见元素以下方法返回列表中出现的最常见元素。
# def most_frequent(list):
#     return max(set(list), key = list.count)
#
# list = [1,2,1,2,3,2,1,4,2]
# most_frequent(list)
#
# # 25.回文以下方法可检查给定的字符串是否为回文结构。该方法首先将字符串转换为小写，然后从中删除非字母数字字符。最后，它会将新的字符串与反转版本进行比较。
# from re import sub
# def palindrome(string):
#     s = sub( [W_] ,   , string.lower())
#     return s == s[::-1]
# palindrome( taco cat ) # True
#
# # 26.没有 if-else 语句的简单计算器以下代码段将展示如何编写一个不使用 if-else 条件的简单计算器。import operator
# action = {
#     "+": operator.add,
#     "-": operator.sub,
#     "/": operator.truediv,
#     "*": operator.mul,
#     "**": pow
# }
# print(action[ - ](50, 25)) # 25
#
# # 27.元素顺序打乱以下算法通过实现 Fisher-Yates算法 在新列表中进行排序来将列表中的元素顺序随机打乱。
# from copy import deepcopy
# from random import randint
# def shuffle(lst):
#     temp_lst = deepcopy(lst)
#     m = len(temp_lst)
#     while (m):
#         m -= 1
#         i = randint(0, m)
#         temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
#     return temp_lst
#
# foo = [1,2,3]
# shuffle(foo) # [2,3,1] , foo = [1,2,3]
#
# # 28.列表扁平化以下方法可使列表扁平化，类似于JavaScript中的[].concat(…arr)。
# def spread(arg):
#     ret = []
#     for i in arg:
#         if isinstance(i, list):
#             ret.extend(i)
#         else:
#             ret.append(i)
#     return ret
# spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]
#
# # 29.变量交换以下是交换两个变量的快速方法，而且无需使用额外的变量。
# def swap(a, b):
#   return b, a
# a, b = -1, 14
# swap(a, b) # (14, -1)
#
# # 30.获取缺失键的默认值以下代码段显示了如何在字典中没有包含要查找的键的情况下获得默认值。
# d = { a : 1,  b : 2}
# print(d.get( c , 3)) # 3



