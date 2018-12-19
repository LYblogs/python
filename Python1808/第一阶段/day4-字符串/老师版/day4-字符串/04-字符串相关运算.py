"""__author__ = 余婷"""
"""
1. + 
字符串1 + 字符串2： 将两个字符串拼接在一起产生一个新的字符串(不会修改原字符)

注意：字符串相加，加号两边必须都是字符串
"""
str1 = 'abc'
str2 = '123'
print(str1 + str2, str1, str2)

# print(str2+10)  # TypeError: must be str, not int
print(str2+'10')  # 12310

"""
2. *
字符串 * n(正整数)：字符串的内容重复n次，产生一个新的字符串
"""
str1 = 'abc'
print(str1*3)
print('*'*10)

# 练习： 10个*跟10个%   ***..%%%..
print(('*'*10+'%'*10)*3)

"""
3.比较运算符: >，<. ==, !=, >=, <=
a. ==, != 
字符串1 == 字符串2 - 判断两个字符串是否相等
"""
print('abc' == 'abc')
print('abc' != 'abc')
print('abc' == 'cba')

"""
a. >, <, >=, <=
两个字符串比较大小：从第一个开始，找到第一对不同的字符，然后比较他们的编码值的大小
"""
print('abc' > 'ad')  # False
print('abcdZ' > 'abcde' )  # False
print('1abc' < 'ahkks')  # True

# 练习：判断一个字符是否是字母
# char = input('请输入一个字符:')
char = 'a'
print('是否是字母:', 'a' <= char <= 'z' or 'A' <= char <= 'Z')

# 练习：判断一个字符是否是中文
print('是否是中文:', '\u4e00' <= char <= '\u9fa5')
print('是否是中文:', 0x4e00 <= ord(char) <= 0x9fa5)
print('是否是中文:', '一' <= char <= '龥')


"""
4. in 和 not in
字符串1 in 字符串2：判断字符串2中是否包含字符串1，结果是布尔
字符串1 not in 字符串2：判断字符串2中是否不包含字符串1，结果是布尔
"""
print('abc' in 'abc123')  # True
print('abc' in 'ab123c')  # False
print('abc' not in 'ab123c')  # True
print('#' in 'ahs#hf#23')   # True


"""
5.len函数
len(序列) 
len(字符串) - 获取字符串中字符的个数
"""
print(len('abc123'))
print(len('abc\n123\u4edd'))  # 8
print(len('abc\n123\\u4edd')) # 13
print(len(r'abc\n123\u4edd')) # 14
print(len('abc\t1 23'))  # 8

"""
6.str
str(数据)；将数据转换成字符串

a.其他数据转换成字符串:
所有的类型的数据都可以转换成字符串。转换的时候就是在数据的值的最外面加引号

补充：系统数据类型名不能用来给变量命名
"""
str1 = str(100)
print(str1, type(str1))

"""
b.字符串转其他类型
字符串转整数: int(字符串), 只有去掉引号后剩下的部分本身就是一个整数的字符串才能转换成整型
字符串转浮点型: float(字符串),只有去掉引号后剩下的部分本身就是一个整数或者小数的字符串才能转换成浮点型
字符串转布尔: bool(字符串), 除了空串会转换成False,其他所有的字符串都会转换成True
"""
print(int('-123'))
print(float('12.89'), float('123'), float('2e3'))
print(bool('0'), bool('False'))   # True
print(bool(''))  # False

