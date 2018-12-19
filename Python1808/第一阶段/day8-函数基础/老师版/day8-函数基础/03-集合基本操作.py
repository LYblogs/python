"""__author__ = 余婷"""

# 1.什么是集合(set)
"""
a.集合是python内置的一个容器类的数据类型，是可变、无序的

b.字面量 - 使用{}括起来，里面有多个元素，多个元素之间用逗号隔开
{1, 2, 3}

c.元素 - 不是键值对; 必须是不可变的，而是还是唯一的

"""
set1 = {1, 'hello', True, (1, 3)}
# set2 = {1, 'hello', True, [1, 3]}  # TypeError, 集合中的元素不可变

set3 = {1, 'hello', True, (1, 3), 1}
print(set3)

set4 = {}   # {} - 是空的字典，不是空的集合
print(type(set4))

set4 = set()  # 创建一个空的集合
print(type(set4), set4)

# 2.集合的增删改查
"""
a.查(获取集合元素) 
不能直接获取集合中单独的某个元素，只能遍历
"""
set3 = set('hello,world')
print(set3)
for item in set3:
    print(item)

"""
b.增(添加元素)
集合.add(元素) - 将指定的元素添加到集合中
集合.update(序列) - 将序列中的元素添加到集合
"""
set3.add(100)
print(set3)

set3.update([10, 20])
print(set3)

"""
c.删(删除元素)
集合.remove(元素) - 删除集合中指定的元素
"""
set3 = {100, 'w', 'h', 'e', ',', 'd', 'o', 'l', 'r'}
set3.remove(100)
print(set3)

"""
d.改 - 集合不能修改元素的值
"""

# in/not in, max, min, len, set
"""
set(序列) - 将序列转换成集合
"""
print(2 in {1, 2, 3})   # True
print({1, 2} in {1, 2, 3})   # False

