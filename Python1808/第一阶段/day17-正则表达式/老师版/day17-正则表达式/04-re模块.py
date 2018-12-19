"""__author__ = 余婷"""
import re

# 1.compile(了解)
"""
compile(正则表达式) - 将正则表达式转换成正则表达式对象
转换成对象后可以通过对象调用对象方法
"""
re_str = '\d{3}'
re_obj = re.compile(re_str)

# 调用模块中的函数
print(re.fullmatch(re_str, '234'))
# 调用对象方法
print(re_obj.fullmatch('234'))

# 2.match和fullmatch
"""
a. fullmatch(正则表达式, 字符串) - 完全匹配，从字符串开头匹配到字符串结束
b. match(正则表达式, 字符串) - 不完全匹配，只匹配字符串开头

匹配成功返回匹配对象，匹配失败返回None
"""
re_str = r'\d([A-Z]{2})'
result1 = re.fullmatch(re_str, '2HK')
print(result1)

result2 = re.match(re_str, '8KLsjdddd==')
print(result2)

# 匹配对象
"""
1.span - 匹配到的内容的范围，(开始下标, 结束下标), 结束下标取不到
匹配对象.span()  - 获取整个正则表达式匹配到的范围
匹配对象.span(n) - 获取正则表达式中第n个分组匹配到的范围(前提是有分组)
"""
print(result2.span())
print(result2.span(1))

"""
2.start和end - 获取匹配结果的开始下标和结束下标
匹配对象.start()/匹配对象.end() - 获取整个正则表达式匹配到的开始下标/结束下标
匹配对象.start(n)/匹配对象.end(n) - 获取正则表达式中第n个分组匹配到的开始/结束下标
"""
print(result2.start(), result2.end())
print(result2.start(1), result2.end(1))

"""
3.group - 获取匹配到的内容
匹配对象.group() - 获取整个正则表达式匹配到的内容
匹配对象.group(n) - 获取正则表达式中第n个分组匹配到的内容
"""
print(result2.group())
print(result2.group(1))

"""
4. string - 获取用来匹配的原字符串
匹配对象.string
"""
print(result2.string)

# 3.search
"""
search(正则表达式, 字符串) - 匹配字符串中第一个满足正则表达式的子串，如果匹配成功返回匹配对象否则返回None            
"""
str1 = 'abc123hks362shjjk990kll'
result = re.search(r'\d{3}[a-z]{2}', str1)
print(result)

# 4.split
"""
split(正则表达式, 字符串) - 在字符串中按照满足正则表达式条件的子串对字符串进行切割, 返回一个列表
"""
str1 = 'ab+c7hdjd8jss-sk9sjj78s9kk*k'
result = re.split(r'\d+|[+*-]+', str1)
print(result)

# 5.sub
"""
sub(正则表达式, 新子串, 字符串) - 用新子串替换字符串中满足正则表达式的子串，返回一个替换后的字符串
"""
str1 = '你丫是傻    叉吗? 我操你大爷的. F u c k you.'
result = re.sub(r'[丫操艹]|F\s*u\s*c\s*k|傻\s*叉', '*', str1)
print(result)

# 6.findall
"""
findall(正则表达式, 字符串) - 在字符串中获取满足正则表达式的所有的字符，返回一个列表，列表元素是字符串

注意：如果这个正则表达式中有一个分组，结果是列表中只那个分组匹配到的结果
     如果这个正则表达式中分组的个数大于1，结果是一个列表，列表中的元素是元祖，元祖中是每个分组匹配到的内容
"""
str1 = 'haja37jjkd89sdhs909nnna238==='
result = re.findall(r'[a-zA-Z]{2,}(\d+)([a-z]+?)', str1)
print(result)

# 7.finditer
"""
finditer(正则表达式, 字符串) - 获取字符串中满足正则表达式的内容，返回的是一个迭代器，迭代器中的元素是匹配对象
"""
result = re.finditer(r'[a-zA-Z]{2,}(\d+)([a-z]+?)', str1)
print(result)
print(next(result))
print(next(result))


# 思考：写一个自己finditer
def yt_finditer(pattern, string):
    re1 = re.search(pattern, string)
    while re1:
        yield re1
        string = string[re1.end():]
        re1 = re.search(pattern, string)


print('============')
result = yt_finditer(r'[a-zA-Z]{2,}(\d+)([a-z]+?)', str1)
print(next(result))
print(next(result))



