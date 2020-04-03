#author:ZhengNengjin
#date: 2018/9/2

# string 操作
print('Hello'*2)    #重复输出字符串
print('HelloWorld!'[2:])    #通过索引获取字符串中字符，和列表的切片操作是相同的
print('Hello'in 'HelloWorld!')  #关键字 in ，成员运算符，如果字符串中包含指定的字符返回True
print('%s is a handssome boy'%'znj')    #格式字符串
print('Hello'+'World'+'!')    #字符串拼接
a='abc'
b='def'
c=''.join([a,b])
print(c)    # + 的效率低，用join。将多个字符串通过‘’拼接起来。（重要）


# string的内置方法
st='hello\tworld'
print(st.count('l'))        #统计元素个数
print(st.capitalize())      #首字母大写
print(c.center(30,'*'))     #补充相应个数的字符并居中
print(st.encode())          #编码，暂时不讲
print(st.endswith('ld'))    #判断是否以某个内容结尾，是的话输出True
print(st.startswith('he'))  #判断是否以某个内容开头，是的话输出True（比较重要)
print(st.expandtabs(tabsize=10))
# st='hello kitty {name} is {age}'
# print(st.expandtabs(tabsize=20))
# print(st.find('t'))        #  查找到第一个元素，并将索引值返回
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print(st.format_map({'name':'alex','age':22}))
# print(st.index('t'))
# print('asd'.isalnum())
# print('12632178'.isdecimal())
# print('1269999.uuuu'.isnumeric())
# print('abc'.isidentifier())
# print('Abc'.islower())
# print('ABC'.isupper())
# print('  e'.isspace())
# print('My title'.istitle())
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('My tLtle'.swapcase())
# print('My tLtle'.ljust(50,'*'))
# print('My tLtle'.rjust(50,'*'))
# print('\tMy tLtle\n'.strip())
# print('\tMy tLtle\n'.lstrip())
# print('\tMy tLtle\n'.rstrip())
# print('ok')
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.rfind('t'))
# print('My title title'.split('i',1)) 分割字符串，
# print('My title title'.title())

#摘一些重要的字符串方法
#1 print(st.count('l'))
# print(st.center(50,'#'))   #  居中
# print(st.startswith('he')) #  判断是否以某个内容开头
# print(st.find('t'))
# print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# print('My tLtle'.lower())
# print('My tLtle'.upper())
# print('\tMy tLtle\n'.strip())
# print('My title title'.replace('itle','lesson',1))
# print('My title title'.split('i',1))


