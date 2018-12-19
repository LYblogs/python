"""__author__ = 余婷"""

"""
1.返回值
a.函数的返回值就是return关键字后面表达式的值，就是函数调用表达式的值。
b.python中所有的函数都有返回值，默认是None

return - 关键字；返回返回值；结束函数(当函数在执行的过程中遇到了return，函数直接结束)
         如果函数体中没有return，函数会在函数体执行完成后将None作为返回值
         
函数调用表达式 - 调用函数的语句;当函数调用完成后，函数调用表达式的结果就是函数的返回值
"""
def func1(m, n):
    print(m,n)
    # 将100作为函数func1的返回值
    return 100   # return-关键字   100 - 返回值


def func2(m, n):
    return m+n   # m+n的结果就是返回值


def func3(m, n):
    #
    return None   # None作为返回值， 在这儿结束函数。函数体后面的其他语句不会执行
    print(m, n)


def func4(m):
    if m % 2 == 0:
        return '偶数'


str1 = func4(10)   # func4(10) == '偶数'
print(str1, func4(10), len(func4(10)))
print(func4(11))


# 看一个函数的返回值，永远只看是否遇到return,遇到了就是return后面的值，遇不到就是None
def func5():
    print('hello')


func5()
print(func5())

"""
返回值的作用：就是将在函数内部产生的数据，传递到函数的外面。防止在函数调用完成后被销毁
什么时候使用返回值：如果实现函数的功能会产生新的数据，一般都会将这个数据返回
"""


def func6(n):
    sum1 = sum(range(n+1))
    # print(sum1)
    return sum1


num = func6(10)
print(num)
list1 = [num]
print(list1)

# 2.同时返回多个值
"""
python的函数支持返回多个值

return 返回值1,返回值2,返回值3...  - 实质是以元祖的形式返回
"""


# 写一个函数，求多个数的和以及平均值
def operation(*nums):
    sum1 = sum(nums)
    aver = sum1 / len(nums)
    return sum1, aver


print(operation(1, 2, 3, 4, 5))  # (15, 3.0)
x, y = operation(1, 2, 3, 4, 5, 6, 7)
print(x, y)

