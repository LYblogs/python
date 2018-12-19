"""__author__ = 余婷"""

# 1.while循环
"""
a.语法：
while 条件语句:
    循环体
    
b.说明:
while - 关键字
条件语句 - 有结果的表达式(除了赋值语句，一般的表达式都行)
: - 固定写法
循环体 - 和while保持一个缩进的一条或者多条语句（会被重复执行）

(重点！)c.执行过程：
先判断条件语句是否为True,为True就执行循环体;
执行完循环体再判断条件语句是否为True, 为True又执行循环体;
执行完循环体再判断条件语句是否为True, 为True又执行循环体;
...
以此类推，知道判断条件语句的结果为False,整个循环就结果
"""
# 1,2,3,4,...100
num = 1
while num <= 100:
    print(num)
    num += 1
print('==:',num)

# 1*2*3...*10
num = 1
sum1 = 1
while num <= 10:
    sum1 *= num
    num += 1
print(sum1)

# 练习：使用while循环，获取字符串：'abc123'中的每个字符
str1 = 'abc123'
index = 0
while index < len(str1):
    print(str1[index])
    index += 1

# 2.for循环和while循环的选择
"""
python中，for循环能做到的while循环都能做到；但是while循环能做的，for循环不一定能做到

使用for循环:
a. 获取序列中的元素(值)
b. 循环次数确定

while循环:
a. 死循环
b. 循环次数不确定
"""
# 练习：程序可以不断的进行输入，知道输入的值为0为止
"""
请输入: 12
请输入: a
请输入: 
"""
value = input('请输入:')
while value != '0':
    value = input('请输入:')

print('结束!')

