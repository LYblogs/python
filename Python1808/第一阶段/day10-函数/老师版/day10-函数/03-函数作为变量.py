"""__author__ = 余婷"""

"""
python中，声明函数其实就是声明一个类型是function的变量。函数名就是变量名

函数名作为变量除了可以用来调用函数获取返回值以外，普通变量能做的它都能做
"""
# 声明类型是int类型的变量a
a = 10
print(type(a))

# 声明类型是dict类型的变量b
b = {'a': 12, 'b': 200}
print(type(b))
print(b['a'])

# 声明类型是function类型的变量c
c = lambda x: x*x
print(type(c))
c(10)


# # 声明类型是function类型的变量d
def d(x):
    def e():
        print('abc')
    e()
    return x*x


print(type(d))
d(10)

# 1.让一个变量给另外一个变量赋值
# 声明一个列表变量list1
list1 = [1, 2, 3]
# 使用列表变量list1给list2赋值
list2 = list1
# 将list2当成列表来用
print(list2[0])


# 声明一个函数变量func11
def func11():
    print('我是函数')

#  使用函数变量func11给ff赋值
ff = func11
# 将ff当成函数来用
ff()

# 2.将变量作为列表的元素或者字典的值
# 声明列表变量list1
list1 = [100, 200, 300]
# 将列表变量list1作为列表list2的元素
list2 = [list1, 100]
print(list2[0][0])


# 声明一个函数变量func2
def func2():
    print('我是函数2')
# 将函数变量func2作为列表list2的元素
list2 = [func2, 100]
print(list2[0]())


# 3.作为函数的参数
"""
将函数1作为实参，传递给函数2；这儿的函数2就是一个高阶函数(实参高阶函数)
"""
def test(x):
    # x = func3
    print('test:', x)
    if not isinstance(x, int):
        x()

# 声明一个int类型的变量a
a = 10
# 将变量a作为test的实参
test(a)

# 声明一个fucntion类型的变量func3
def func3():
    print('我是函数3')
test(func3)


# 3.1 sort函数
"""
def sort(key=None, reverse=False)

key - 确定排序的时候以什么值为标准来排序(默认情况下，以列表的元素的大小为标准来排序);
      需要传一个函数，函数需要一个参数和一个返回值。这儿的参数是列表的元素
reverse - 是否降序排序, 需要传一个bool值
"""
# list2.sort(reverse=True)


"""
[1, 34, 20, 89, 8]  -> [1, 8, 20, 34, 89]
index = 0   [1, 34, 20, 89, 8]
index = 1   [1, 8, 34 ,89, 20]
index = 2   [1, 8, 20, 89, 34]
...
"""

def yt_sort(list1, key=None):
    # list1 = my_list2; key = get_age
    if key == None:
        # 直接对列表元素进行排序
        for index in range(len(list1)):
            for index2 in range(index+1, len(list1)):
                current = list1[index]
                behind = list1[index2]
                if behind < current:
                    list1[index], list1[index2] = list1[index2], list1[index]
    else:
        for index in range(len(list1)):
            for index2 in range(index+1, len(list1)):
                current = key(list1[index])
                behind = key(list1[index2])
                if behind < current:
                    list1[index], list1[index2] = list1[index2], list1[index]


my_list = [1, 34, 20, 89, 8]
yt_sort(my_list)
# my_list.sort()
print(my_list)

my_list2 = [
    {'name': '张三', 'age': 18},
    {'name': '李四', 'age': 30},
    {'name': '王五', 'age': 10}
]
# my_list2.sort() # TypeError: '<' not supported between instances of 'dict' and 'dict'
# yt_sort(my_list2) # TypeError: '<' not supported between instances of 'dict' and 'dict'


def get_age(x):
    return x['age']


yt_sort(my_list2, get_age)
print(my_list2)


my_list2 = [
    {'name': '张三', 'age': 18, 'score': 90},
    {'name': '李四', 'age': 30, 'score': 80},
    {'name': '王五', 'age': 10, 'score': 89}
]

# 取最大年龄对应的字典
max_age = max(my_list2, key=lambda x: x['age'])
print(max_age)

# 取最大成绩对应的字典
max_score = max(my_list2, key=lambda x: x['score'])
print(max_score)


# 练习：要求将按列表中元祖的第二个元素，获取最大值。
my_list3 = [('z', 10), ('b', 30), ('c', 20)]
print(max(my_list3, key=lambda item: item[1]))

# 4.变量作为函数的返回值
"""
返回值是函数的函数，也叫高阶函数(返回值高阶函数)
"""


def test2(n):
    sum1 = 1
    for x in range(1, n+1):
        sum1 *= x
    return sum1


re = test2(5) + 10
print(re)


def get_operation(char):
    # char = '+'
    """
    根据不同的符号返回不同的功能(函数功能的描述)
    :param char: 运算符符号
    :return: 不同运算符对应的功能的函数
    """
    if char == '+':
        # 求和的功能
        def sum(*args, **kwargs):
            # args = (10,20,30)
            """求多个数的和"""
            sum1 = 0
            for item1 in args:
                sum1 += item1
            for key in kwargs:
                sum1 += kwargs[key]
            print('yt')
            return sum1

        return sum
    elif char == '*':
        def mul(*args, **kwargs):
            sum1 = 1
            for item1 in args:
                sum1 *= item1
            for key in kwargs:
                sum1 *= kwargs[key]
            return sum1

        return mul
    elif char == '-':
        def diff(*args):
            """求多个数的差"""
            # (10, 20, 30)
            sum1 = args[0]
            for index in range(1, len(args)):
                sum1 -= args[index]
            return sum1

        return diff
    else:
        print('暂时不支持这个运算符')
        return None


# re是一个函数
re = get_operation('+')
# re(10, 20, 30) - 调用函数获取返回值
print(re(10, 20, 30))  # 60  = 10+20+30

# get_operation('*')  - 这个整体是一个函数
# get_operation('*')(1, 2, 3)  - 调用求乘积的那个函数，并且获取返回值
re = get_operation('*')(1, 2, 3)
print(re)


# 10 - 20 - 30
print(get_operation('-')(100, 20, 30))



