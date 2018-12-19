"""__author__ = 余婷"""

"""
1.什么是元祖（tuple）
元祖就是不可变的列表。（有序，不可变）
有序 - 可以通过下标获取元素
不可变 - 不支持增、删、改

2.元祖的字面量: 通过小括号将多个元素括起来，多个元素之间用逗号隔开
"""
tuple1 = (1, True, 'abc', [1, 2], 1)
print(tuple1)

# a.只要一个元素的元祖: 在元素的后面必须加一个逗号
tuple2 = (10,)
print(tuple2, type(tuple2))

# b.直接将多个数据用逗号隔开，不用括号括起来。还是一个元祖值
tuple3 = 1, 2, 3, 'abc'
print(tuple3, type(tuple3))

# c.获取元祖元素
tuple4 = (10, 20)
print(tuple4[0], tuple4[-2])

# 可以通过变量个数和元祖元素个数保持一致来获取元祖中的每个元素
x, y = tuple4  # x, y = 10, 20
print(x, y)

# 通过在变量名前加*,获取没有*的变量获取到的元素的剩下的部分。以列表的形式返回
tuple5 = ('余婷', 98, 90, 99, 87, 78)
name, *scores = tuple5
print(name, scores)  # '余婷' [98, 90, 99, 87, 78]

name, number, *scores = tuple5
print(name, number)   # '余婷'  98
print(scores)  # [90, 99, 87, 78]

*list1, num = tuple5
print(list1, num)  # ['余婷', 98, 90, 99, 87]  78

num1, *list1, num2 = tuple5
print(num1, num2)   # 余婷 78
print(list1)  # [98, 90, 99, 87]

# (了解)
tuple1 = (1, 2, 3)
print(*tuple1)
list1 = ['aa', 'bb', 'cc']
# a = list1[0]
# b = list1[1]
# c = list1[2]
# *list1 == a b c
print(*list1)

"""
3.获取元祖元素和列表获取列表回去列表元素一模一样
"""
tuple1 = 1, 2, 3, 4, 5
print(tuple1[1])
print(tuple1[:3])

for item in tuple1:
    print(item)

"""
4.相关运算和列表一样
+, *, in/not in, len(), tuple(), max(), min()
"""
print((1, 2) + ('a', 'n'))
print((1, 2) * 3)
print(1 in (1, 2))
print(len((1, 2, 4)))
print(max((1, 89, 0)))
print(min((1, 89, 0)))

"""
5.元祖相关的方法： 只有列表中的count和index
"""
