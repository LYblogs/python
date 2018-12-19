"""__author__ = 余婷"""

# 1.列表赋值
"""
a.直接使用一个列表变量给另一个列表变量赋值，赋的是地址。
  赋完值之后，对其中一个列表进行增删改，会影响另一个列表
b.如果赋值的时候赋的列表的切片或者拷贝,会产生新的地址，然后使用新的地址赋值。
  赋完值之后，两个列表相互之间不影响
"""
# 现象1：
list1 = [1, 2, 3]
list2 = list1
list2.append(100)
print(list1)   # [1, 2, 3, 100]
list1 = [1, 2, 3]
list2.append(200)
print(list1)

# 现象2：
list1 = [1, 2, 3]
list2 = list1[:]
list2.append(100)
print(list1)   # [1, 2, 3]

# 2.列表中的方法
"""
1.列表.count(元素) - 获取指定元素在列表中出现的次数
"""
numbers = [100, 34, 90, 89, 100, 7, 100, 18]
print(numbers.count(100))

"""
2.列表.extend(序列) - 将序列中所有的元素都添加到列表中
"""
numbers.extend(['abc', 'hello'])
print(numbers)
numbers.extend('world')
print(numbers)
numbers.extend(range(11, 15))
print(numbers)

"""
3.列表.index(元素) - 获取指定元素的下标

注意:a.如果元素有多个，只去第一个的下标
    b.如果这个元素不存在，会报错(ValueError)
"""
numbers = [3, 1, 2, 3, 4, 5, 3]
print(numbers.index(3))   # 0
# print(numbers.index(33))  # ValueError: 33 is not in list

"""
4.列表.reverse() - 反向列表(将列表元素倒序)
"""
numbers = [19, 89, 2, 8, 98, 10, 32]
numbers.reverse()
print(numbers)

"""
5.列表.sort() - 对列表进行升序排序(从小到大)
列表.sort(reverse=True) - 对列表进行降序排序(从大到小)

注意：列表的要求：a.列表的元素类型必须一样  b.元素支持比较运算符
"""
numbers = [19, 89, 2, 8, 98, 10, 32]
numbers.sort()
print(numbers)

numbers = [19, 89, 2, 8, 98, 10, 32]
numbers.sort(reverse=True)
print(numbers)

names = ['路飞', '娜美', '山治', '罗宾', '弗兰克', '乔巴', '佐罗']
names.sort()
print(names)

"""
6.列表.clear() - 清空列表
"""
names = ['路飞', '娜美', '山治', '罗宾', '弗兰克', '乔巴', '佐罗']
names.clear()
print(names)

# 注意: 清空列表尽量使用clear()
# names = ['路飞', '娜美', '山治', '罗宾', '弗兰克', '乔巴', '佐罗']
# names = []
# print(names)

"""
7.列表.copy() - 将列表中元素直接赋值一份产生一个新的列表。和列表[:]效果一样
注意: 这儿的拷贝是浅拷贝
"""
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)
print(list1 is list2)   # False
