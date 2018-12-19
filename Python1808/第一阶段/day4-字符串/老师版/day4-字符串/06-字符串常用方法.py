"""__author__ = 余婷"""
"""
1.字符串.capitalize() - 将字符串第一个字符转换成大写
"""
str1 = 'hello'
new_str = str1.capitalize()
print(new_str)

"""
2.字符串对齐
字符串.center(width, fillchar) -  居中
字符串.ljust(width, fillchar) - 左对齐
字符串.rjust(width, fillchar) - 右对齐

width - 正整数，表示新的字符串的宽度
fillchar - 字符， 填充字符串
"""
str1 = '123'
new_str = str1.center(7, '/')
print(new_str) # //123//

new_str = str1.ljust(7, '/')
print(new_str)  # 123////

new_str = str1.rjust(7, '/')
print(new_str)  # ////123

"python1808001"
"python1808002"
"python1808011"

import random   # 导入随机数对应的模块
"""
random.randint(m, n) - 产生一个m~n的随机整数
"""
num = random.randint(0, 20)
print(num)
new_num = 'python1808'+ str(num).rjust(3, '0')
print(new_num)

"""
"""
str1 = '23434'
print(str1.isalpha())

str1 = '壹23万萬43幺一百'
print("git=",str1.isdigit())

print(str1.isnumeric())

"""
3.join(seq)
字符串1.join(字符串2): 将字符串1的内容插入到字符串2的每个字符之间
"""
str1 = '**'
str2 = 'abc'
print(str1.join(str2))

"""
4.
max(字符串)
min(字符串)
"""
print(max('ahajsxnzhsjdf234'))  #z
print(min('ahajsxnzhsjdf234')) #2

print('agskshabkkhabba'.replace('a', '/'))
print('agsk*shabkk*habba'.split('*'))

