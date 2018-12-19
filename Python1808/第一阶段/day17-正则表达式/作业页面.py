# 1. 写一个正则表达式判断一个字符串是否是ip地址
# 规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255
# 255.189.10.37   正确
# 256.189.89.9    错误


# try:
#     re_str =r"(((0?|1)\d?\d?\.)|(2[0-5]?[0-5]?\.)){3}(((0?|1)\d?\d?)|(2[0-5]?[0-5]?))"
#     ip =input("请输入ip地址：")
#     result =re.fullmatch(re_str,ip)
#     ip1=result.group()
#     print("输入正确")
# except AttributeError:
#     print("输入错误")
# 2. 计算一个字符串中所有的数字的和
# 例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
# import re
# re_str =r"\d+\.?\d+"
# str1 =input("请输入字符串：")
# result =re.findall(re_str,str1)
# sum =0
# for countent in result:
#     sum+=float(countent)
# print(sum)
# 3. 验证输入的内容只能是汉字
# import re
# re_str =r"[\u4e00-\u9FA5]+"
# result =re.fullmatch(re_str,"苏俄武器和")
# print(result)

# 4. 电话号码的验证
# re_str =r"(13\d|15[0-27-9]|18[2-47-8]|17\d)\d{8}"
# result =re.fullmatch(re_str,"13540869383")
# print(result)
# 5. 简单的身份证号的验证
# 51392219970428543x
import re
# # re_str =r"\d{6}(1\d{3}|(200\d|201[0-8]))(0\d|1[0-2])([1-2]\d|3[0-1])\d{3}(x|\d)"
# # print(re.fullmatch(re_str,"51392220181231543x"))
re_str =r"a*?b"
print(re.fullmatch(re_str,"aaaab"))
# 3.	能够完全匹配字符串“back”和“back-end”的正则表达式包括（ ABC）
# A. “\w{4}-\w{3}|\w{4}”	match->back,back-end    fullmatch-> back,back-end
# B. “\w{4}|\w{4}-\w{3}” match-> back, back  fullmatch-> back,back-end
# C. “\S+-\S+|\S+”
# D. “\w*\b-\b\w*|\w*”
# 4.	能够完全匹配字符串“go go”和“kitty kitty”，但不能完全匹配“go kitty”的正则表达式包括（ ）
# :\1就是重复前面第一个()/组合里面的内容
# ：\2就是重复前面第二个()/组合里面的内容
# A. “\b(\w+)\b\s+\1\b”
# B. “\w{2,5}\s*\1”
# C. “(\S+) \s+\1”
# D. “(\S{2,5})\s{1,}\1”