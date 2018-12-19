import random

"""
1.字符串.capitalize() - 将字符串第一个字符转换成大写
"""
str1 = "gje  jeje jj"
str2 = str1.capitalize()
print(str2)
"""
# 2.字符串.conter（width，fillchar）- 居中
    字符串.ljust（width，fillchar）-左对齐
    字符串.rjust（width，fillchar）-右对齐
"""

num = random.randint(0, 20)
str3 = "python1808"
nwe_num = str(num).rjust(3, "0")
print(str3 + nwe_num)
