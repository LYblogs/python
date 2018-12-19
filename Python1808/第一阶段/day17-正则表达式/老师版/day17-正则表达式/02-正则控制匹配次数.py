"""__author__ = 余婷"""
import re

# 1 *(匹配0次或者多次)
"""
a* - a出现0次或者多次, '','a','aa', 'aaa'...都可以匹配
\d* - 任意数字出现0次或者多次， '','1','12', '3772'...都可以匹配
[abc]* - a，b或者c出现0次或者多次
[A-F]* - A到F中任意字符出现0次或者多次

注意：在[]外面的*的前面需要一个字符或者一个匹配字符的符号
"""
print(re.fullmatch(r'a*b', 'aaaaaaaaaab'))
print(re.fullmatch(r'[abc]*', 'aabc'))

# 2 +(匹配1次或者多次)
"""
a+ - a至少出现一次
\d+ - 数字至少出现一次
"""
print(re.fullmatch(r'a+b', 'ab'))

# 3 ?(匹配0次或者1次)
"""
a? - a出现0次或者1次, '', 'a'可以匹配
"""
# 写一个正则表达式匹配一个整数（正整数和负整数都可以），例如：123， 10， +100， -1234，
re_str = r'[-+]?[1-9]\d*'
print(re.fullmatch(re_str, '-12'))

# 4 {}
"""
{N} - 匹配N次,  例如： a{3}，匹配三个'a'
{M,N} - 匹配M到N次,   例如： a{3, 5}，匹配三个'a' 或者4个'a'或者5个'a'
{,N} - 最多匹配N次(0~N)   例如：a{,3}，'','a', 'aa', 'aaa' 
{M,} - 至少匹配M次   例如：a{3,} , 'aaa', 'aaaa', 'aaaaa'...
"""
print(re.fullmatch(r'a{3,}', 'aaa'))

# 练习：输入密码，要求检查密码输入是否合格(密码由字母和数字组成，数字不开头，6-12位)。给出提示
password = input('密码:')
re_str = r'[a-zA-Z][\da-zA-Z]{5,11}'
result = re.fullmatch(re_str, password)
if result:
    print('输入成功！')
else:
    print('输入有误！')
