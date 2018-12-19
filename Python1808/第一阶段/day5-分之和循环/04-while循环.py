"""
1.while循环
语法：
while 条件语句：
    循环体

说明：
while - 关键字
条件语句 - 只要有结果的表达式（除了赋值语句，一般的表达式都行）
：- 固定写法
循环体 - 和while保持一个缩进的一条或者多条语句（会被重复执行的代码）

执行过程：
先判断条件语句是否为True，如果为True则执行循环体；
执行完循环体再判断条件语句是否为True，为True又执行循环体；
以此类推，直到判断条件语句为False，整个循环就结束
"""
num1 = 1
sum1 = 1
while num1 <=10:
    sum1 *= num1
    num1 += 1
print(sum1)

#练习：使用while循环，获取字符串"abc123"的每个字符
str1 = "abc123"
index = 0
while index <len(str1):
    print(str1[index])
    index +=1

"""
2.for循环和while的选择
python中for循环能做的while都能做到，但是while循环能做的for循环不一定能做到
for循环：
        当循环需要获取序列中元素的值
        循环次数确定的时候
while：
      循环次数不确定
      死循环
"""

#练习：程序可以不断的去输入，直到输入的值为0为止
str2 = input("请输入：")
num2 = 0
while str2 != "0" and num2 <2:
    num2 +=1
    str2 = input("请输入：")

