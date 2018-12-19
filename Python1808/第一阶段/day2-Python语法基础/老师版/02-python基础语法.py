"""__author__ = 余婷"""

# 1.注释
# 注释是程序中专门用来注释说明的文字。不会参与程序编译和执行。对程序的功能没有任何影响
# 单行注释:在说明性文字前加#
"""
使用三个单引号或者三个双引号括起来，来设置多行注释
但是一般使用三个双引号
"""

# 2.标识符
# 标识符就是专门用来命名的。给变量命名、函数命名、类命名等
"""
要求：
python中的标识符要求是由数字、字母和下划线组成，并且数字不能开头

注意，在python3.x，标识符中可以包含非ASCII码字符（非ASCII码包含中文、日语、韩语、拉丁等）。
     但是，在实际开发的时候不要用
"""
num = 100
num2 = 100
__ = 100
# 12abc = 100  # SyntaxError: invalid syntax
你好 = 100
# n-m = 100  # SyntaxError: can't assign to operator

# 3.行与缩进
# python中对代码里面的所有有严格要求。同一级代码前面的缩进(空格/tab)的个数必须一致
# 行的规范：要求声明函数和类的前后需要有两个空行
#  print('hello world')  # IndentationError

if 100 > 10:
    print('大于')


# 4.分段(行)显示
# 一句代码很长，需要多行来显示的时候，可以在需要换行的位置加\
# 注意：加\的时候不能将一个数据，一个变量名给拆开
num = 2837487 + 34398748 + 384798578 +\
      37847578 + 347895789 + 457279 + \
      345234757 + 3549087 + 3457078

# 如果代码是列表、元祖、字典、集合的字面量，可以直接换行，不用加\
list1 = [
    12,
    23,
    4543,
    'ahgshgd',
    'sjhfjkh'
]

# 5.一行显示多条语句
"""
一行显示一条语句的时候，后面不用加分号。但是如果希望在一行显示多条语句，那么多条语句之间必须加分号
"""
print('aaa');print('bbb')

# 6.关键字(保留字)
"""
python中已经定义好的有特殊的功能或者特殊的意义的一些标识符，就是python的关键字。
命名的时候不能使用关键字

'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
"""
import keyword   # 导入keyword模块
print(keyword.kwlist)  # 打印python中所有的关键字

# and = 100  # SyntaxError: invalid syntax

# 7.print函数和input函数
"""
(掌握)
print(内容) - 在控制台中打印内容(内容必须是python数据)
print(内容1, 内容2, ..., 内容n) - 在一行打印多个内容，在控制台显示的时候多个内容之间用空格隔开

默认情况下，一个print中的内容占一行（以换行结束）。一个print中的多个内容用空格隔开
(了解)
print(内容,内容1，...,内容n, end='换行标志')
print(内容,内容1，...,内容n, sep='分割标志')
"""
print('打印1')
print(100)
print('abc', 'bcd', 200)

print('打印1', end='==')
print(100)
print('abc', 'bcd', 200, sep='@')
print('abc', 'bcd', 200, sep='')

"""
input() - 从控制台输入一串内容，以回车结束。并且将内容返回(以字符串的形式返回)
input('提示信息')

注意：程序执行到input的时候，程序会停下来，直到输入完成为止
"""
print(input('请输入:'))