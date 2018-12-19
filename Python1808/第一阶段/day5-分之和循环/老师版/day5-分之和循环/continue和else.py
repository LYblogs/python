"""__author__ = 余婷"""

# 1.continue
"""
continue是一个关键字，只能写在循环体中

功能：当循环执行过程中遇到continue,会结束当次循环，直接进入下次循环的判断。
    （直接进入下次循环的判断:for循环就是用变量取下一个值；while循环就是直接判断条件语句是否为True）
    
"""
sum1 = 0
for x in range(100):
    if x % 2 == 0:
        continue
    sum1 += x

print(sum1)
# 结果： 求1+3+5+...+99


# 2.break
"""
break是一个关键字,只能写在循环体中

功能：当循环过程中遇到可break，整个循环直接结束
"""

"""
num = 1
sum1 = 0

1+0 >= 10  False  sum1 = 1  num = 2
1+2 >= 10  False  sum1 = 3  num = 3
3+3 >= 10  False  sum1 = 6  num = 4
6+4 >= 10  True   break
"""
num = 1
sum1 = 0
while True:
    if sum1+num >= 10:
        break
    sum1 += num
    num += 1

print(sum1)


for x in range(1000):
    print(x)
    break

# 3.else
"""
a.语法:
while 条件语句:
    循环
else:
    代码段
    
for 变量 in 序列:
    循环体
else:
    代码段
    
b.执行过程:
else结构不会影响原循环的执行过程。当循环自然死亡的时候，就会执行else后边的代码段。
循环因为遇到break而结束的时候不会执行else后边的代码段
"""

for x in range(10):
    print(x)
    if x == 3:
        break
else:
    print('for循环结束了')