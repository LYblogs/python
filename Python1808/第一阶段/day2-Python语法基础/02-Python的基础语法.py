# 1.注释
# 注释是程序中专门用来注释说明的文字。不会参与程序的编译与执行。
# 单行注释：在说明性文字前加#

"""
多行注释：把说明性文字用三个'或"括起来
但一般使用三个"
"""


# 2.标识符
# 标识符就是专门用来命名的。给变量命名、函数命名、类命名等
"""
要求：
Python的标识符要求是由数字、字母和下划线组成，并且数字不能开头。

注意：在Python3.x，标识符中可以包含非ASCII码字符（非ASCII码包含中文、日语、韩语等）
      但是，在实际开发的时候不要用
"""
num = 100
__ = 200
你好 = 300
print(num,__)
"""
"""
# 3.行与缩进
# Python中对代码里面的缩进有严格要求。同一行代码前面的缩进（空格/tab）的个数必须一致
# 行的规范：要求声明函数和类的前后需要两个空行


# 4.分行显示
#一句代码很长，需要多行显示的时候，可以在需要换行的位置加\
# 注意：加\的时候不能将一个数据，一个变量名拆开
# 如果代码是列表、元组、字典、集合的字面量，可以直接换行，并不用加\
list1 = [12
         ,23
         ,5454,
         'ASA']

# 5.一行显示多条语句
"""
一行显示一条语句不用加分号。但是希望一条显示多条语句
那么多条语句之间必须加分号
"""
print('aaa');print(123)

# 6.关键字（保留字）
"""
Python中已经定义好的有特殊功能或者有特殊意义的一些标识符，就是Python的关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'async'
 'await', 'break', 'class', 'continue', 'def', 'del'
 'elif', 'else', 'except', 'finally', 'for', 'from'
 'global', 'if', 'import', 'in', 'is', 'lambda'
 'nonlocal', 'not', 'or', 'pass', 'raise', 'return' 
 'try', 'while', 'with', 'yield']
"""
import  keyword # 导出keyword库
print(keyword.kwlist)# 打印所有关键字

# 7.print函数和input函数
"""
print（内容） - 在控制台中打印内容
print（内容1，内容2） - 在控制台中一行打印2个内容

默认情况下一个print的内容占一行（以换行结束）。一个print里的多个内容用空格隔开。
print（内容1，内容2，...，内容n，end =“换行标志”）
print（内容1，内容2，...，内容n，sep =“分割标志”）
"""
print('打印1')
print(100)
print('打印1',end='==')
print(100)
print('abc','bcd',100,sep='*')
print('abc','bcd',100,sep='')

'''
input（） - 从控制台输入一串内容（以回车结束）。并将内容返回

注意：程序执行到input的时候，程序会停下来，直到输入完成为止

'''
input('请输入一个整数：')
