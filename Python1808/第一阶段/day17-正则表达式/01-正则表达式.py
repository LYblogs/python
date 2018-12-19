import re
"""
1.什么是正则表达式
正则表达式就是一个字符匹配的工具；是由正则符号和普通字符组成，来匹配不同规律的字符串

2.python对正则表达式的支持
python中内置提供了一个re模块，用来支持正则表达式

fullmach（正则表达式，字符串） - 用正则表达式去完全匹配字符串，如果匹配成功，返回一个匹配结果；
失败，返回None

python中正则表达式的写法：将正则内容写到字符串中，一般这个字符串最前面会加一个r

"""

#1普通字符
"""
普通字符在正则表达式中，代表字符本身
"""
#匹配一个字符串，第一个字符是a，第二个字符是b，第三个字符也是最后一个字符是c
re_str = r"abc"
result=re.fullmatch(re_str,"abc") #  <re.Match object; span=(0, 3), match='abc'>
print(result)

# 2  .(匹配任意字符)
"""
在正则表达式中，.出现的位置，可以匹配一个任意字符
注意：一个.只能匹配一个字符

"""
#匹配一个字符串长度为3，并且第一个字符是a，最后一个字符为c，中间为任意字符的字符串
re_str =r"a.c"
result =re.fullmatch(re_str,"a\tc")
print(result) #<re.Match object; span=(0, 3), match='a\tc'>

#3 \w(匹配字母数字或者下划线)
"""
在正则表达式中，\w出现的位置可以匹配一个任意的字母数字、下划线(其实也可以匹配Unicode编码中除了ASCII码剩下的部分)

注意：
一个\w只能匹配一个字符
中文也可以匹配
"""
re_str  = r"\w..."
result =re.fullmatch(re_str,"1&5%") #<re.Match object; span=(0, 4), match='1&5%'>
result1 =re.fullmatch(re_str,"啊333") #<re.Match object; span=(0, 4), match='啊333'>
print(result)
print(result1)

# 4 \s （匹配空白字符）
"""
空白字符包括：空格、制表符和换行符

注意：一个\s只能匹配一个字符
"""
#匹配一个长度是4的字符串，并且字符串前两位是字母数字下划线，中间一个空白，最后是字符数字下划线的字符串。
re_str =r"\w\w\s\w"
result =re.fullmatch(re_str,"hj\n8") #<re.Match object; span=(0, 4), match='hj\n8'>
result1 =re.fullmatch(re_str,"hj\r8")
print(result1)

# 5 \d （匹配数字字符）
#匹配一个长度为5的字符串，并且字符串前三位必须是数字字符，后两位是任意字符
re_str = r"\d\d\d.."
result =re.fullmatch(re_str,"555aa")
print(result)

#6  \b(检测单词边界)
"""
注意：\b：是检测\b出现的位置是否是单词边界，不会对字符进行匹配。
        当正则表达式中出现了\b，匹配的时候先去掉\b，匹配成功后，再看\b出现的位置是否是单词边界
单词边界：单词开头，单词结尾、标点符号、空白符号等（只要能将单词区分开的符号都属于单词边界）
"""
#匹配字符串”hello world ， 并且要求w的前面是单词边界“
re_str =r"hello\b world"
result =re.fullmatch(re_str,"hello world")
print(result)

#7 ^ （检测字符串开头）
"""
在match与fullmatch中没有意义，search、findall等中有意义
"""
#匹配一个字符串长度为5，前面三个字符是the，后面两个任意字符
re_str = r"^The.."

# 8 $ （检测字符串结尾）
"""
在match与fullmatch中没有意义，search、findall等中有意义
"""
re_str =r"The$"
result =re.fullmatch(re_str,"The")
print(result)

"""
\大写字母对应的功能是\小写字母的取反
\w - 匹配数字、字母、下划线
\W - 匹配非数字、字母、下划线
\D - 匹配非数字字符
\S - 匹配非空白字符
\B - 检测非单词边界
"""

# 9  \W （匹配非数字、字母、下划线）
# 匹配一个字符串，第一个字符是数字，第二个是非数字，
# 第三个是空白字符,第四个是数字字母下划线，最后一个是a，并且要求a的前面不是单词边界
re_str =r"\d\D\s\w\Ba"
result =re.fullmatch(re_str,"1b _a")
print(result) #<re.Match object; span=(0, 5), match='1b _a'>

# 10  [字符集](匹配中括号出现的任意一个字符)
"""
1.[普通字符集](匹配中括号出现的任意一个字符)
列如：[abc] - 匹配a或者b或者c

注意：a.一个中括号只能匹配一个字符
      b.正则中有特殊功能的单个符号放在中括号中会失效，例如：. $ ^等
      c.匹配字符的组合符号在中括号中保持原来的功能；列如：\w，\d等
"""
#匹配一个长度是2的字符串，并且第一个字符为数字，第二个字符为[bcd=]里面的元素
re_str =r"\d[bcd=]"
result =re.fullmatch(re_str,"1=")
print(result)

"""
2.[字符1-字符2] - 表示字符1-字符2的范围（字符1的编码值，要小于字符2的编码）

[a-z] - 表示匹配所有的小写字母
[A-Z] - 表示匹配所有的大写字母
[a-zA-Z] - 表示匹配所有的字母
[1-7] - 匹配数字字符1到7
[\u4e00-\u9fa5] - 匹配所有中文
"""
re_str =r"[a-z]"

# 11 [^字符集] - （匹配不在字符集中的任何字符）
"""
[^abc] - 匹配除了abc以外的任意其他字符
[^a-z]  - 匹配除了小写字母外的其他任意字符
"""