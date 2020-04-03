#__author: ZhengNengjin
#__date: 2018/9/19

# python中的作用域分4种情况：
# L：local，局部作用域，即函数中定义的变量；
# E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
# G：globa，全局变量，就是模块级别定义的变量；
# B：built-in，系统固定模块里面的变量，比如int, bytearray等。 搜索变量的优先级顺序依次是：
# 作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。

# if True:
# 	x = 3
# print(x)

count = 10
def outer():
	global count #全局变量使用global关键字
	print(count)
	count = 100
	return count
	
outer()

# 小结
#变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
#只有模块、类、及函数才能引入新作用域；
#对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
#内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，嵌套作用域变量要使用nonlocal关键字。
# nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。
