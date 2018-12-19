"""__author__ = 余婷"""
# 1. +
"""
列表1 + 列表2 - 使用两个列表中元素产生一个新的列表
"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list1 + list2)
print(list1, list2)

# 2. *
"""
列表 * n(正整数) - 将列表中的元素重复n次，产生一个新的列表
"""
print(list1*3)

# 3. in和not in
"""
元素 in 列表    判断指定的元素是否在指定的列表中
元素 not in 列表   判断指定的元素是否不在指定的列表中
"""
names = ['小明', '路飞', '小花', '余婷']
if '余婷' in names:
    print('恭喜，获奖了!')
else:
    print('很遗憾！')

print(['小明', '路飞'] in names)    # False

# 4.len
"""
len(列表) - 获取列表元素的个数
"""
names = [['小明', '路飞'], '小花', '余婷', {'a': 12, 'b': 123}, lambda x: x*2]
print(len(names))

# 5.list
"""
list(数据) - 将其他的数据转换成列表

注意: 这儿的数据，只能是序列(所有的序列都能转换成列表-将序列中的元素作为列表的元素)
"""
str1 = 'hello'
print(list(str1))

print(list(range(10, 20)))
# print(list(100))  # TypeError: 'int' object is not iterable

# 6.max和min
"""
max(列表) - 获取列表中元素的最大值
min(列表) - 获取列表中元素的最小值

注意：列表有要求：a. 列表中的元素的类型一样  b.元素对应的类型支持比较运算符
"""
print(max([1, 45, 667, 3, 78, 90]))
print(min([1, 45, 667, 3, 78, 90]))
print(max(['ab', 'sk', 'zbs', '**(3']))