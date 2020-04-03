#__author: ZhengNengjin
#__date: 2018/9/30

s = 'hello world'

# print(s.find('llo'))
# ret = s.replace('ll','xx')
# print(ret)
# print(s.split('l'))
# string提供的方法是完全匹配

引入正则：模糊匹配
import re
'''元字符'''
# . 通配符
ret1 = re.findall('w...d','hellowsssd world') # . 能代替任何一个字符，除了换行符，只能代替一个字符
print(ret1)

# ^ 从前面开始匹配
ret2 = re.findall('^z.j','znj jtt zxj')  # ^ 从前面开始寻找，找到一个匹配的，
print(ret2)

# $ 从结尾开始匹配
ret3 = re.findall('z.j$','zxj jtt znj') # $ 从后面开始寻找，找到一个匹配的，
print(ret3)

# * 重复匹配 [0,+∞] 贪婪匹配
ret4 = re.findall('ab*','abkjhaabdbabbbb') # * 匹配一次或多次匹配a后面没有或无限个b，b前面没有或无限个a
print(ret4)

# + 重复匹配[1,+∞] 贪婪匹配
ret5 = re.findall('a+b','aaaabhghabfb') #匹配a后面一个或无限个b，b前面一个或无限个a
print(ret5)

# ? 重复匹配[0,1] 贪婪匹配
ret6 = re.findall('a?b','aaaabhghabfb')# 匹配a后面0或多个b，b前面0或多个a
print(ret6)

# {} 贪婪匹配，{n}匹配一个字符n次，{n，m}匹配一个字符n到m次
ret7 = re.findall('a{1,3}b','aaaab') #{}中可以是数字也可以是范围，满足多少个a才能匹配
print(ret7)

# * + ？ 都是贪婪匹配，后面加？使其变成惰性匹配

'''结论： *等价于（0，正无穷）， +等价于（1，正无穷），？等价于（0，1）'''

#[]字符集：取消元字符的特殊功能 除了 - ^ \ 还有特殊功能
ret8 = re.findall('[a-z]','adx')
print(ret8)
ret9 = re.findall('[w,,]','awdx.,')
print(ret9)
#
ret10 = re.findall('[1-9a-zA-Z]','asdfg123')
print(ret10)

^ 放在[]里面：取反
ret11 = re.findall('[^  4,5]','iu12ds5s34')
print(ret11)

''' \ 反斜杠后边跟元字符去除特殊功能,比如\.
反斜杠后边跟普通字符实现特殊功能,比如\d'''

\d  匹配任何十进制数；它相当于类 [0-9]。
\D 匹配任何非数字字符；它相当于类 [^0-9]。
\s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
\S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
\w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
\b  匹配一个特殊字符边界，比如空格 ，&，＃等

ret12 = re.findall('\d{11}','znj17775300181jtt15956504740')
print(ret12)
ret13 = re.findall('\sasd','fak asd')
print(ret13)
ret14 = re.findall(r'I\b','hello,I am a LIST')
print(ret14)

ret15 = re.search('sb','fdfabdfsbfdfsb')
print(ret15);print(ret15.group())

ret16 = re.findall(r'\\','abc\de') # r的意思是，说是原生字符串
print(ret16)
ret16 = re.findall('\\\\','abc\de') # 原本两个\ ，python解释器每个\需要两个\所以是四个、
print(ret16)

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))

ret = re.split('[j,s]','sdjksal')
print(ret)

ret = re.sub('znj','jtt','znjlovejtt')
print(ret)

obj = re.compile('\.com'    )
ret = obj.findall('www.baidu.com')
print(ret)

ret = re.findall('www.(?:\w+).com','www.baidu.com')
print(ret)
# 加上？：取消（）的优先级

# 元字符 | 或的意思






















