import re
#1. * (匹配0次或者多次)
"""
a* - a出现0次或多次
\d*  - 任意数字出现0次或者多次，"","1","1212"...都可以匹配
[abc]* - a、b或c出现0次或者多次
注意：在[]外面的*的前面需要一个字符，或者一个匹配字符的符号
"""
print(re.fullmatch(r"a*b","aaab"))
print(re.fullmatch(r"[abc]*","aaab"))
print(re.fullmatch(r".*","sdasda32&_12%#@$说到底"))

#2. + （匹配1次或者多次）
"""
a+ -a至少出现一次
"""

# 3.? (匹配0次或者一次)
"""
a? - a出现0次或者一次，"","a"可以匹配

"""

#写一个正则表达式，匹配一个整数（正负都可以），例如：123,10，+100，-123
re_str =r"[+-]?[1-9]\d*"
result =re.fullmatch(re_str,"+1")
print(result)


# 4 {}
"""
{N} - 匹配N次，a{3} - 匹配a出现三次,"aaa"
{M,N} - 匹配M-N次，M<N,a{3,5}，匹配"aaa","aaaa","aaaaa"
{,N} - 最多匹配N次（0~N）例如：a{，3} ，"","a","aa","aaa"
{M,} - 最少匹配M次（M~*）例如：a{3,},"aaa","aaaa"...

"""

#练习：输入密码，要求检测密码输入是否合格（密码由字母和数字组成，数字不开头，6~12位）
# 输入正确就是正确，错误就提示错误
re_str =r"[a-zA-Z][a-zA-Z\d]{5,11}"
password =input("请输入密码：")
result =re.fullmatch(re_str,password)
if not result:
    print("密码格式错误")
else:
    print("输入正确")
