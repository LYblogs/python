
"""
python中的分之语结构只有if语句，没有switch

1.if语句
语法：
    if 条件语句：
        代码段
说明：
    if - 关键字
    条件语句 - 任何有结果的表达式（不管结果是什么类型）
    ： - 固定写法
    代码段 - 需要和if语句保持一个tab缩进的一条或多条语句。
执行过程 ：
先判断条件语句的结果是否是True，如果是则执行代码段，否则就不执行。

注意：如果条件语句的结果不是布尔，会先将结果转换成布尔再判断。
      赋值语句不能写在if的后面。
"""
"""num = int(input())
if num % 2 == 0:
    print("%d是偶数"%(num))
    print("11111")  #和if保持缩进是在if成立的时候才执行
print("11111")  #和if没有保持缩进的是不管if条件是否成立都会执行
"""
#练习：随机产生一个年龄值，如果年龄大于18就打印"成年"
import random
age = random.randint(0,150)
if age >= 18:
    print("%d岁已经成年"%(age))
else:
    print("%d岁是未成年"%(age))
print("年龄是：%d"%(age))

"""
2.if-else
语法：
    if 条件语句:
        代码段1
    else：
        代码段2

执行过程：
先判断条件语句是否为True，如何是执行代码段1，否则执行代码段2.
随机产生一个整数，如果是奇数打印"xxx是奇数"，否则打印"xxx是偶数"

"""
import random
num = random.randint(0,999)
if  num & 1:
    print("%d是奇数"%(num))
else:
    print("%d是偶数" % (num))

"""
3.if - elif - else
语法：
if  条件语句1：
    代码段1
elif  条件语句2：
    代码段2
elif    条件语句3：
    代码段3
....
else：
    代码段4
    
执行过程：
先判断条件语句1是否为True，为True则执行代码段1；否则判断条件语句2
是否为True，为True则执行代码段2，以此类推，一直执行到语句为True或者
执行else后面的代码段

注意：后面的条件判断前提是前面的条件不成立
      这儿的elif可以有多个，else也可以省略
"""
#练习：如果成绩小于60是不及格，60-70及格，71~89良好，大于90优秀。
# num = int(input("请输入您的成绩："))
# if  num <60:
#     print("不及格")
# elif num<=70:
#     print("及格")
# elif  num <= 89:
#     print("良好")
# else:
#     print("优秀")

"""
4.if嵌套
可以在if，elif，else后面的代码段中，都可以写其他的if语句
练习：如果一个数字是偶数就打印"偶数"，否则打印奇数。如果偶数还能被4整除，再打印能被4整除

"""
# num = int(input())
# if  num & 1 :
#     print("是奇数")
# else:
#     print("是偶数")
#     if num % 4 == 0:
#         print("是4的倍数")
#     else:
#         print("不是4的倍数")

# 练习：输入一个字符串，判断字符串的第一个字符是否是字符，如果是，打印“以字母开头”
# 如果这个字母是大写的，再打印大写字母
# 方法1.
str1 = input("请输入一个字符串：")
if  "a"<=str1[0]<="z" or "A"<=str1[0]<="Z":
    print("以字母开头")
    if "A"<=str1[0]<="Z":
        print("大写字母")
    else:
        print("小写字母")
else:
    print("不是以字母开头")

# 方法2.
str1 = input("请输入一个字符串：")
if  str1[0].isalpha():
    print("以字母开头")
    if str1[0].isupper():
        print("大写字母")
    else:
        print("小写字母")
else:
    print("不是以字母开头")