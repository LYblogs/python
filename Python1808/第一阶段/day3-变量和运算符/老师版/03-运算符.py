"""__author__ = 余婷"""

"""
python中的运算符：数学运算符,比较运算符,逻辑运算符,赋值运算符,位运算符
"""
# 1.数学运算符：+，-，*，/, %, //, **
"""
+: 加法运算，-:减法运算，*:乘法运算，/:除法运算， %:取余（求余数）, //:整除， **：幂运算
+,-,*,/和数学中的+，-，x,÷ 对应的功能一模一样
"""
print(10+20)
print(10-20)
print(10*20)
print(10/20)

# a.% - 取余
"""
应用1：获取一个整数的最低的一位或者几位的值  num%(10^n)
应用2：判断一个是是否能够被另外一个数整除   num1 % num2
"""
print(10 % 3)
print(10 % 2)

# 获取一个数的个数
num = 36523
print(num % 10)  # 3
print(num % 100) # 23

# b. // - 除法运算，求商，获取商的整数部分
print(5//2)   # 2
print(3.9 // 3)  # 1.0

num = 289
print(num//100)  # 取num的百位上的值

# c. ** - 幂运算
"""
x ** y - 求x的y次方
"""
print(2**10)  # 2的10次方
print(9**0.5) # 9开平方
print(8**(1/3))  # 8开3次方


# 2.比较运算符：>, <, ==, !=, >=, <=
"""
所有的比较运算符的运算结果都是布尔值
"""
# 值1 > 值2 ： 值1是否大于值2
print(100 > 10)  # True
print(10 > 100)  # False
print(10 > 10)   # False

# 值1 < 值2： 值1是否小于值2
print(100 < 10)  # False

# 值1==值2： 值1是否等于值2
print(10 == 100)    # False
print(10 == 10)     # True
num = 10
print(num == 10)  # True

# 值1!=值2: 值1是否不等于值2
print(10!=100)   # True
print(10!=10)    # False

# 3.逻辑运算符: and, or, not
"""
逻辑运算符的运算对象是布尔值，运算符结果也是布尔值
a. and(逻辑与运算):
值1 and 值2：如果值1和值2的都为True,结果才是True；只要有一个False结果就是False
True and True -> True
True and False -> False
False and True -> False
False and  False -> False
"""
# 逻辑与运算相当于生活中的'并且'；当需要多个条件同时满足，就使用and将多个条件连接在一起
grade = 90   # 成绩
score = 98   # 分数
# 例子：要求成绩大于90并且表现分大于95，才能获得奖学金
print('是否获取奖学金:',    grade > 90 and score > 95)

"""
b.or(逻辑或运算)
值1 or 值2：如果值1和值2中有一个是True，就过就是True。两个都是False，即如果才是False
True or  True  -> True
True or  False  -> True
False or  True  -> True
False or  False  -> False
"""
# 逻辑或运算，相当于生活中的'或者';当需要多个条件中至少有一个条件满足，就是用or将多个条件连接在一起
grade = 90   # 成绩
score = 98   # 分数
# 例子：要求成绩大于90或者表现分大于95，就能获得奖学金
print(grade > 90 or score > 95)

"""
c.not(逻辑非运算)
not 值：如果值是True,结果就是False;如果值是False，结果就是True

not True -> False
not False -> True
"""
# not用来对某个条件进行否定
age = 17
# 是否能够进入网吧的条件: 年龄不小于18
print('是否能进入网吧:', not age < 18)
print('是否能进入网吧:', age >= 18)



