"""__author__ = 余婷"""

"""
1.变量的作用域
变量在程序中能够使用的范围

2.全局变量
a.声明在函数或者类的外部的变量都是全局变量
b.全局变量是从声明开始到整个py文件结束，任何位置都可以使用(作用域：从声明开始到文件结束)

3.局部变量
a.声明在函数或者类的里面的变量都是局部变量
b.局部变量是从声明开始到函数结束，任何位置都可以使用(作用域：从声明开始到函数结束)
"""
# ===========1.全局变量===========
# 全局变量
a = 10

# x和y是全局变量
for x in range(10):
    y = 20
    print(x)

print(x, y)

if True:
    # b是全局变量
    b = 20

print(b)


def func1():
    print('函数中:', a)
    print('函数中', x, y)


func1()


# ============2.局部变量=============
# num1, num2, aa, xx都是局部变量
def func2(num1, num2):
    print(num1, num2)
    aa = 11
    print(aa)
    for xx in range(5):
        print(xx)
    print(xx)


func2(10, 20)
# print(num1)  # NameError: name 'num1' is not defined
# print(aa)  # NameError: name 'aa' is not defined

# ============3.global的使用==========
"""
global关键字只能在函数中使用,作用是在函数中声明一个全局变量

语法:
global 变量名
变量名 = 值

"""
# 声明一个全局变量a1
a1 = 100


def test1():
    # 声明一个局部变量a1
    # a1 = 200
    # print(a1)

    global a1
    a1 = 200
    print(a1)

    # 在函数中声明全局变量b1
    global b1
    b1 = 300


test1()
print(a1, b1)


# =============4.nonlocal的使用==============
"""
nonlocal关键字只能在函数中使用
当需要在局部的局部中修改局部变量的值，就使用nonlocal

语法：
nonlocal 变量名
变量名 = 值
"""


def func1():
    # 声明一个局部变量a2
    a2 = 'abc'

    # python中函数可以声明函数
    def func11():
        nonlocal a2
        a2 = 'python'
        print('func11-a2:', a2)
        # a3的作用域在func11中
        a3 = 111
    func11()
    print('func1-a2:', a2)


func1()


# 思考？
# funtions = []
# for x in range(5):
#     def func1(a):
#         return a*x
#     funtions.append(func1)
#
# t1 = funtions[0]
# t2 = funtions[2]
# print(t1(2))
# print(t2(2))



