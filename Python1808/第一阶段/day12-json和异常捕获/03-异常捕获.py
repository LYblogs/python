"""
1.什么是异常捕获
程序执行过程中出现错误，也叫出现异常

2.异常捕获
让本来会出现异常的位置，不出现异常，而是自己去处理异常出现的情况

3.怎么捕获异常
情况一：捕获所有的异常
语法：
try：
    需要捕获异常的代码段1
except：
    代码段2
执行过程：执行代码段1，如果代码段1中出现异常，不会崩溃，而是马上执行代码段2.
            如果代码段1没有异常，不会执行代码段2

"""
try:
    print([1,2,3][10])
except:
    print("出现异常")
print("========")

"""
情况二：捕获指定的异常
a.语法：
try:
    代码段1
except 错误类型名：
    代码段2
    
执行过程：执行代码段1，当代码段1出现指定错误类型的时候，才执行代码段2


"""
try:
    print(int("abc"))
    print([1,2,3][10]) #IndexError
except ValueError:
    print("下标越界")

"""
情况三：同时捕获多个异常，对不同的异常做出相同的反应
语法：
try:
    代码段1
except (错误类型1，错误类型2):
    代码段2
执行过程：执行代码段1，当代码段1中出现了指定的异常。不崩溃，然后执行代码段2


情况四:同时捕获多个异常，对不同的异常做出不同的反应
try:
    代码段1
except 错误类型1:
    代码段2
except 错误类型2:
    代码段3
.
.
.
"""
# w(ﾟДﾟ)w
# w(°一°)w

"""
4.try -except-finally
语法：
try:
    代码段1
except:
    代码段2
finally:
    代码段3
不管代码段1中是否出现异常，也不管异常是否捕获到，finally后面的代码都会执行（写遗书的位置）
"""
# try:
#     print([1,2,3][10])
# except KeyError:
#     print("aaa")
# finally:
#     print("bbbb")

#统计学生的成绩，到输入的结果是"end"
# 最后求输入的成绩的和
#
# while True:
#     try:
#         score = int(input("输入成绩:"))
#         break
#     except ValueError:
#         print("输入有误!请重新输入")


#封装一个函数，功能是获取指定文件中的内容（普通文本文件）
# 从封装的角度：调用者做的事情，越少越好
def huo_qu():
    while True:
        address=input("请输入文件地址：")
        try:
            with open(address,"r",encoding="utf-8") as  f:
                countent=f.read()
                print(countent)
                break
        except FileNotFoundError:
            print("文件地址错误")
huo_qu()