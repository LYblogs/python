"""__author__ = 余婷"""

"""
python中的分之结构只有if语句，没有switch
"""
num = 11
print('%d是偶数' % (num))

# 1. if语句
"""
a.语法:
if 条件语句:
    代码段

b.说明：
if - 关键字
条件语句 - 任何有结果的表达式(不管结果是什么类型)
: - 固定
代码段 - 和if保持一个缩进的一条或者多条语句。

c.执行过程:
先判断条件语句的结果是否是True，如果是True就执行冒号后面的代码段。否则就不执行代码段
注意：如果条件语句的结果不是布尔，会先将结果转换成布尔再判断
"""
# 1.1 if后面可以写哪些语句
if 10:
    print('条件是语句是10')

if 'abc':
    print('条件是语句是abc')

if True:
    print('条件是语句是True')

if 100 > 20:
    print('条件是语句是100 > 20')

if 'AHSG'.isupper():
    print('全是大写!')

# 注意：赋值语句不能写在if的后面
# if num = 10:
#     print('赋值语句')
num = 11
if num & 1 == 0:
    print('%d是偶数' % (num))
    print('==========')        # 和if保持一个缩进的语句是在条件成立的时候才执行
    print('^^^^^^')

print('~~~~~~~~~~~')    # 在if外面的语句不管if条件是否成立都会执行

# 练习：随机产生一个年龄值，如果年龄大于等于18就打印'成年',不管年龄是多少，都把年龄值打印出来
import random
age = random.randint(0, 100)
print('年龄:',age)
if age >= 18:
    print('成年')


# 2.if-else
"""
a.语法：
if 条按语句:
    代码段1
else:
    代码段2
    
b.执行过程:
先判断条件语句是否为True，为True就执行代码段1；否则执行代码段2
"""
# 随机产生一个整数，如果是奇数打印'XXX是奇数'，否则打印'XXX是偶数'
num = random.randint(0, 20)
if num & 1 == 1:
    print('%d是奇数' % num)
else:
    print('%d是偶数' % num)
    print('!!!!!!!')


# if - elif - else
"""
a.语法:
if 条件语句1:
    代码段1
elif 条件语句2:
    代码段2
elif 条件语句3:
    代码段3
...
else:
    代码段n

b.执行过程:
先判断条件语句1是否为True，为True就执行代码段1；
否则，就判断条件语句2是否为True,为True,就执行代码段2
否则，就判断条件语句3是否为True，为True,就执行代码段3
依次类推，如果前面的条件都为False，就执行else后面的代码段n

注意：1.后面的条件判断前提是前面的条件不成立
     2.这儿的elif根据情况可以有多个，else也可以省略
"""
# 根据成绩对成绩进行分段: 小于60分打印不及格，60~70及格，71~89良好,90及90以上优秀
score = 60
if score < 60:
    print('不及格')
elif score <= 70:
    print('及格')
elif score < 90:
    print('良好')
elif score <= 100:
    print('优秀')
else:
    print('超出范围')


# 4.if嵌套
"""
可以在if，elif，else后面的代码段中，都可以再写其他的if语句
"""
# 如果一个数字是偶数就打印'偶数'，否则打印'奇数'。如果偶数还能被4整型，再打印'4的倍数'
num = 1
if num % 2 == 0:
    print('偶数')
    if num % 4 == 0:
        print('4的倍数')
    else:
        print('不是4的倍数')
else:
    print('奇数')
    if num % 5 == 0:
        print('5的倍数')


# 练习：输入一个字符串，判断是否的第一个字符是否是字母，如果是打印'以字母开头'。
#      如果这个字母是大写的，再打印'大写字母'。例如：'abc123' -> 打印'以字母开头'
#      'Abc123' -> 打印'以字母开头'和'大写字母'  '12hsj' -> 什么都不打印
# str1 = input('请输入一个字符串:')
str1 = 'Ahjdd'
# 方法一：
# 字符串.isalpha() -> 是否是字母
if str1[0].isalpha():
    print('以字母开头')
    # 字符串.isupper() -> 是否是大写字母
    if str1[0].isupper():
        print('大写字母')

# 方法二：
if 'a'<=str1[0]<='z' or 'A'<=str1[0]<='Z':
    print('以字母开头')
    if 'A'<=str1[0]<='Z':
        print('大写字母')


char = chr(random.randint(97, 122))
print('随机字符:',char)
