# encoding: utf-8
# module builtins
# from (built-in)
# by generator 1.145
"""
python中，声明函数其实就是声明一个类型是function的变量。函数名就是变量名

函数作为变量，除了可以用来调用函数获取返回值，普通变量能做的，它都能做
"""

#声明类型是int类型的变量
a=10
#声明类型是dict类型的变量
b = {"a":12,"b":200}
#声明类型是function类型的变量
c = lambda x:x*x
#声明类型是function类型的变量d
def d(x):
    return x*x

print(type(d)) #<class 'function'>

# 普通变量能做的：
# 1.让一个变量给另一个变量赋值
# 声明一个列表变量list1
list1 =[1,2,3,4]
# 使用列表变量list1给list2赋值
list2 = list1
#将list2当做列表来用
print(list2[2]) #3

#声明一个类型为function的变量func11
def func11():
    print("我是函数")
#用函数变量func11给ff赋值
ff = func11
#将ff当做函数来用
ff() #我是函数

#2.将变量作为列表的元素或者是字典的值
# ```python
list1 =[1,2,3,4]
list2 =[list1,100]

# 声明函数变量func2
def func2():
    print("我是函数2")

list2 = [func2,100]
print(list2[0]())
# ```
# 3.作为函数的参数
"""
将函数1作为实参，传递给函数2；这儿的函数2就是一个高阶函数（实参高阶函数）

"""
#```python
def test(x):
    print(x)
# 声明一个int类型的变量a
a = 10
#将变量a作为实参传递给变量test
test(a)

# 声明一个function类型的变量
def func3():
    print("我是函数3")
    return "我是函数test"
test(func3())
#```

#4.sort函数
"""
def sort (key = None ,reverse =False)
key - 确定排序的时候以什么值为标准来排序（默认情况下，以列表的元素的大小为标准来排序）；
        需要传一个函数，函数需要一个参数和一个返回值。这儿的参数是列表的元素
reverse - 是否降序排序，需要传一个布尔值
"""
list1 =[1,2,3,4]
list1.sort()

#取最大年龄对应的列表
print(max([["a",10],["b",200],["c",30]],key=lambda item:item[1]))


#4.将变量作为函数的返回值
def test2(n):
    sum1 = 1
    for x in range(1,n+1):
        sum1*=x
    return  sum1

re = test2(5)+1
# print(re)

def get_operation(char):
    """
    根据不同的符号返回不同的功能（函数功能描述）
    :param char: 运算符符号
    :return: 一个运算符对应的相应的函数
    """
    if char =="+":
        def sum(*args,**kwargs):
            """
            求多个数的和
            :param args:
            :param kwargs:
            :return:
            """
            sum1=0
            for item1 in args:
                sum1+=item1
            for  key in kwargs:
                sum1+=kwargs[key]
            return sum1


        return sum
    elif char =="*":
        def mul(*args,**kwargs):
            sum1=1
            for items in args:
                sum1*=items
            for  key in  kwargs:
                sum1*=kwargs[key]
            return sum1
        return mul
    elif char == "-":
        def poor(*args,**kwargs):
            poor1 =args[0]
            for item in args:
                poor1-=item
            for key in kwargs:
                poor1 -= kwargs[key]
            return poor1
        return poor
    else:
        def x(*args,**kwargs):
            return "输入不规范"
        return "输入不规范"
re = get_operation("*")

print(get_operation("-")(1,6,7,a=1,b=2))
