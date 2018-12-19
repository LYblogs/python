"""__author__ = 余婷"""

"""
返回值能做的事情，函数调用表达式都可以做
"""


# 1.用函数调用表达式给变量赋值
def func1():
    return 'hello'


# str1 = 'hello'
str1 = func1()
print(str1)


# 2.通过函数调用表达式使用相应的方法
def func2():
    return [1, 2]


# print([1, 2][0])
item = func2()[0]
print(item)


item = func2().append(3)   # item获取的是append函数的返回值，append函数没有返回值
print(item)

list1 = func2()
list1.append(3)
print(list1)


# 3.将函数调用表达式作为容器的元素，函数的参数，函数的返回值
def func3():
    print('hello')
    return 100


# 作为值惨叫运算
print(func3() + 3)   # print(100 + 3)

# 作为列表元素
list2 = [func3(), 'abc']
print('list2:',list2)   # [100, 'abc']

# 作为字典的key和value
dict1 = {func3(): func3()}   # {100:100}
print(dict1)


# 作为函数的返回值
def func4(m):
    print(m)
    return func3()


# 作为函数的实参
re = func4(func3())   # func4(100)
print(re)   # 100


