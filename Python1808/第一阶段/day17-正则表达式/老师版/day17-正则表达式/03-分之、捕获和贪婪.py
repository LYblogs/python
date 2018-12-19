"""__author__ = 余婷"""
import re

# 1.分之
"""
条件1 | 条件2  - 匹配条件1或者条件2
\d{2}|[a-z] - 匹配两个数字字符或者一个小写字母
a\d{2}|\w{2} - 匹配一个a后面两个数字，或者两个数字字母下划线

注意：正则中的分之也会出现短路，当条件1可以匹配，就不会再使用条件2进行匹配
"""
print(re.fullmatch(r'\d{2}|[a-z]', 'z'))
print(re.fullmatch(r'a\d{2}|\w{2}', 'sh'))

# 练习：写一个正则表达式，匹配所有的数字,包括正的、负的，整数，小数，0
# 例如：100, +100, -100, 12.5, -12.5, 0, 0.23, 0.012
"""
12, 12.34 : [+-]?[1-9]\d*[.]?\d*
0.123 : [+-]?0[.]\d+
0 : 0
"""
re_str = r'[-+]?[1-9]\d*[.]?\d*|[+-]?0[.]\d+|0'
print(re.fullmatch(re_str, '-0.02'))

# 2 () - 捕获和分组
"""
a.分组 - 将括号中的内容作为一个整体
"""
# 匹配一个字符串，前三位是'abc',后三位是三个数字或者三个大写字母
re_str1 = r'abc\d{3}|abc[A-Z]{3}'
re_str2 = r'abc(\d{3}|[A-Z]{3})'
print(re.fullmatch(re_str2, 'abc123'))

# 匹配一个字符串，以'数字小写字母'的形式出现3次
re_str = r'(\d[a-z]){3}'
print(re.fullmatch(re_str, '2s3f4h'))

"""
b.捕获
通过正则获取符合条件的子串的时候，可以在正则表达式中加括号，匹配后只获取括号里面匹配到的内容

re.findall(正则表达式，字符串) - 在字符串中去获取符合正则表达式条件的所有的子串,返回一个列表
"""
str1 = 'ahsa783+sdh*92dfjhjj78jhsda67jk'
print(re.findall(r'a(\d+)', str1))  # ['783', '67']

"""
c.重复匹配
带多个分组的正则表达式中可以分组的后面通过添加'\数字'来重复前面第几个分组中匹配到的内容

说明：\数字 - 这儿的数字代表前面第几个分组; \1代表第一个分组  \2代表第二个分组
"""
re_str = r'(\d{3})([a-z]{2})a\1{2}-\2'
print(re.fullmatch(re_str, '123efa123123-ef'))

# 3.贪婪
"""
匹配次数后加?就是贪婪匹配：*?, +?, ??, {M,N}?, {M,}? 表示尽可能少的重复
"""
re_str = 'a.+?b'
str1 = 'xxxahdjbnnkbsssammmbkkk'
print(re.findall(re_str, str1))

with open('content.txt', encoding='utf-8') as f:
    text = f.read()
    re_str = '"name":(.+?),'
    all_names = re.findall(re_str, text)
    print(all_names)

# 4.转义符号
r"""
在正则表达式中可以在有特殊意义或者特殊功能的符号前加\来取消其特殊功能
\\w  - 代表两个字符，分别是'\'和w
\+ - 代表+字符
\* - 代表*字符
\? - 代表?字符
[], (), {}表示字符的时候，前面也要加\

注意：在中括号中, \必须加\表示\本身，^在最前面加\表示^本身， -在两个字符之间加\表示-本身
"""
re_str = r'\\w-\d{3}'
print(re.fullmatch(re_str, '\w-232'))

re_str = r'a\+\(\d{2}\)'
print(re.fullmatch(re_str, 'a+(23)'))

re_str = r'[\^a1\-9]'
print(re.fullmatch(re_str, '3'))

re_str = r'(\d{2}([a-z]{3}))\1\2'
print(re.fullmatch(re_str, '12abc12abcabc'))


