# 1. +
"""
列表1 + 列表2 - 使用两个列表中元素产生一个新的列表

"""
list1 = [1,2,3]
list2 = ["a","b","c"]
print(list1+list2)
print(list1,list2)


# 2. *
"""
列表* n（正整数） - 将列表中的元素重复n次，产生一个新的列表。
"""
print(list1*3)

# 3.in 和 not in
"""
元素 in  列表
元素  not  in  列表
判断指定的元素是否（在/不在）指定的列表中
"""

names = ["小明","路飞"]


# 4. len
"""
len(列表) - 获取列表元素的个数
"""

# 5.str
"""
list（数据） - 将其他的数据转换成列表
注意：这儿的数据，只能是序列（所有的序列都能转换-将序列中的元素作为列表的元素）


"""

print(list(range(10)))
print(list("曾 宇 是 憨 批"))

# 6.max和min
"""
max(列表) - 获取列表中元素的最大值
min(列表) - 获取列表中元素的最小值
注意：列表中元素的类型必须一样
      元素对应的类型支持比较运算符

"""
