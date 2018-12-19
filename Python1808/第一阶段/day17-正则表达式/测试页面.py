import re
# 7 ^(检测字符串开头)
"""
在match和fullmatch中没有意义, search、findall等中有意义
"""
# 匹配一个字符串前面三个字符是'The'，后面两个任意字符
re_str = r'^The..'
result = re.fullmatch(re_str, 'The2;')
result1 =re.findall(re_str,"The12aae")
print(result)
print(result1)

# 8 $(检测字符串结尾)
"""
在match和fullmatch中没有意义, search、findall等中有意义
"""
# 匹配一个字符串，只有三位，分别是'The',并且e后面是字符串结尾
re_str = r'The$'
result = re.fullmatch(re_str, 'The')
print(result)
result1 =re.findall(re_str,"The")
print(result1)