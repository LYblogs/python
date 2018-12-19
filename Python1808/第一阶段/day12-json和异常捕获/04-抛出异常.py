"""
抛出异常：主动让程序出现异常

语法：
raise  错误类型  - 程序执行到raise类型语句的时候直接抛出异常
注意：错误类型必须是一个类，并且这个类是exception的子类
"""
# print([1,2,3][2])
# raise IndexError

#练习：输入年龄，如果输入的年龄的范围不在0~100，程序就崩溃

age1= int(input("请输入年龄（0~100）："))
if age1 >100 or age1<0:
    raise  ValueError