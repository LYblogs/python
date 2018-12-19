"""__author__ = 余婷"""

"""
匿名函数还是函数，除了声明的语法以外，函数其他的语法匿名函数都支持

1.匿名函数的声明
a.语法:
函数名 = lambda 参数列表:返回值

b.说明:
函数名 - 变量名
lambda - 关键字
参数列表 - 和普通函数的参数列表的作用和要求一样
返回值 - 相当于普通函数retrun关键字后面的表达式

注意：匿名函数中冒号后面的语句属于函数体。在声明的时候不会执行

匿名函数的调用和普通函数一模一样
"""


# 用匿名函数求两个数的和
def my_sum(num1, num2=0):
    return num1 + num2

print(my_sum(10, 20))
print(my_sum(num1=1, num2=2))

my_sum1 = lambda num1, num2=0: num1+num2
print(my_sum1(100, 200))
print(my_sum1(num1=11, num2=22))


# 练习：写一个匿名函数，求两个数的最大值
my_max = lambda x, y: max(x, y)

print(my_max(100, 200))


# 补充：python中的三目运算符
"""
a.
C中的三目运算符： 条件语句?值1:值2 - 条件语句为True,整个表达式的结果是值1，否则是值2
int x = 10, y = 20;
max = x>y?x:y;

b.
python中的三目运算符：值1 if 条件语句 else 值2  - 条件语句为True,整个表达式的结果是值1，否则是值2
x = 10
y = 20
max1 = x if x > y else y
"""
x = 100
y = 20
max1 = x if x > y else y
print(max1)


my_max2 = lambda num1, num2: num1 if num1 > num2 else num2
print(my_max2(20, 89))
print(my_max2(200, 89))


# 练习：写一个匿名函数，获取字典中指定的key对应的值
get_value = lambda dict1, key: dict1.get(key)
print(get_value({'a': 100, 'b': 200}, 'a'))


#
#
# def func1(item: dict):
#     return item['age']
#
#
# list1.sort(key=func1)
#
#
list1 = [
    {'name': '张三', 'age': 20},
    {'name': '李四', 'age': 10},
    {'name': '王五', 'age': 30}
]
list1.sort(key=lambda item: item['age'])
print()
print(list1)

def key(item):
    return item["age"]

print(key({'name': '张三', 'age': 20}))



