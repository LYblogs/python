"""
1.continue 是一个关键字，只能卸载循环体中

功能：当循环执行过程遇到continue，会结束当次循环，直接进入下次循环的判断。
        （直接进入下次循环的判断：for循环就是用变量取下一个值；while循环就是直接判断条件语句是否为True）

2.break
break是一个关键字，只能写在循环体中
功能：当循环过程中遇到break，整个循环直接结束。


3.else

while 条件语句：
    循环体
else：
    代码段


for 变量 in 序列 ：
    循环体
else：
    代码段

执行过程:
else结果不会影响原循环的执行过程。当循环自然结束的时候，就会执行else后面的代码段。
循环因为遇到break而结束的时候，不会执行else后面的代码段。
"""
for x in range(10):
    print(x)
else:
    print("for循环结束了")