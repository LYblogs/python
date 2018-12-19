import re
# 1.compile
"""
compile(正则表达式) - 将正则表达式转换成正则表达式对象
"""
re_str="\d{3}"
re_obj =re.compile(re_str)
#调用模块中的函数
print(re.fullmatch(re_str,"211"))
#调用对象方法
print(re_obj.fullmatch("234"))

# 2.match和fullmatch
"""
a.fullmatch(正则表达式，字符串) - 完全匹配，从开头到字符串结束
b.match(正则表达式，字符串)- 不完全匹配，只匹配字符串开头

匹配成功就返回匹配对象，匹配失败就返回None
"""
re_str = r"\d([A-Z]{2})"
print(re.fullmatch(re_str,"1IN"))
result=re.match(re_str,"1IN56565")
print(result)

#匹配对象
"""
1.获取span值 - 匹配到的内容的范围，（开始下标，结束下标）
匹配对象.span（）获取整个正则表达式匹配到的范围
匹配对象.span（n）获取正则表达式中第n个分组匹配到的范围（前提是要有分组）
"""
print(result.span(1)) #(1, 3)

"""
2.start和end - 获取匹配结果的开始下标和结束下标
匹配对象.start()/匹配对象.end() -获取整个正则表达式的开始下标和结束下标
匹配对象.start(n)/匹配对象.end(n) - 获取正则表达式中第n个分组匹配到的开始下标和结束下标
"""
print(result.start(),result.end()) #0 3
print(result.start(1),result.end(1)) #1 3

"""
3.group - 获取匹配到的内容
匹配对象.group（） - 获取整个正则表达式匹配到的内容
匹配对象.group（n） -获取正则表达式中第n个分组匹配到的内容
"""
print(result.group()) #1IN
print(result.group(1)) #IN

"""
4.string - 获取用来匹配的原字符串
匹配对象.string
"""
print(result.string) #1IN56565


# 3.search
"""
search（正则表达式，字符串）- 匹配字符串中第一个满足正则表达式的子串，如果匹配成功，返回匹配对象，否则返回None


"""
str1 ="abc123hks362abc123"
result =re.search(r"\d{3}[a-z]{2}",str1)
print(result)

#4.spilt
"""
split(正则表达式，字符串) - 在字符串中按照满足正则表达式的子串进行切割

"""
str1 ="abds1sd5sdss8dsd4545d2dd"
result =re.split(r"\d+",str1)
print(result) #['abds', 'sd', 'sdss', 'dsd', 'd', 'dd']


#5.sub
"""
sub（正则表达式，新子串，字符串） -在字符串中用新子串替换满足正则表达式中的子串，返回新字符串 

"""
str1 ="草你麻痹的 你是sb吗"
result =re.sub(r"[草麻痹]|sb","*",str1)
print(result)

#6.findall
"""
findall(正则表达式，字符串) - 在字符串中获取满足正则表达式的所有字符，返回的是一个列表，列表元素是字符串
注意：如果正则表达式中有一个分组，结果就是列表中只取分组对应的字符串
      如果正则表达式中的分组大于1，列表中的元素是元组，每个元组的元素就是每个分组匹配到的内容
"""
str1 ="asd5eeaaaadee8787qwaadsd12aasd1212dsdse==33"
result =re.findall(r"[a-zA-Z]{2,}\d+[a-z]+?",str1)
print(result) #['asd5eeaaaadee', 'qwaadsd12aasd']
                #['asd5e', 'eaaaadee8787q', 'waadsd12a', 'asd1212d']

#7.finditer
"""
finditer（正则表达式，字符串）-获取字符串满足正则表达式的内容，返回的是一个迭代器，迭代器中的元素就是匹配到的对象

"""
result =re.finditer(r"[a-zA-Z]{2,}\d+[a-z]+?",str1)
print(next(result))
print(next(result))
#思考：写一个自己的finditer
def my_finditer(pattern,string):
    re1 =re.search(pattern,string)
    while re1:
        yield re1
        string =string[re1.end():]
        re1 =re.search(pattern,string)
result=my_finditer(r"[a-zA-Z]{2,}\d+[a-z]+?",str1)
print(next(result))
print(next(result))