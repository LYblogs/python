"""__author__ = 余婷"""

# 1.clear
"""
字典.clear() - 清空字典（删除字典中所有的键值对）
"""
dict1 = {'a': 100, 'b': 200}
dict1.clear()
print(dict1)

# 2.copy
"""
字典.copy() - 复制字典中所有的键值对，产生一个新的字典
"""
dict1 = {'a': 100, 'b': 200}
dict2 = dict1.copy()   # 这儿会产生新的地址
print(dict2)
dict1['a'] = 1
print(dict2)

# 3.fromkeys
"""
dict.fromkeys(序列, 值) - 以序列中的元素作为key，值作为所有key对应的默认值，创建一个字典
"""
dict3 = dict.fromkeys('xyzp', 100)
print(dict3)   # {'x': 100, 'y': 100, 'z': 100, 'p': 100}
dict3 = dict.fromkeys(['name', 'age', 'height'], 100)
print(dict3)    # {'name': 100, 'age': 100, 'height': 100}


# 4.get
"""
字典.get(key) - 获取key对应的值，如果key不存在，返回None
字典.get(key,值) - 获取key对应的值，如果key不存在，返回指定的值
"""
dict3 = {'name': 100, 'age': 100, 'height': 100}
print(dict3.get('name'))   # 100
print(dict3.get('name', '不存在'))   # 100
print(dict3.get('name1'))       # None
print(dict3.get('name1', '不存在'))    # 不存在

# 5.keys, values, items
"""
字典.keys() - 获取字典所有的key(返回一个序列，序列中的元素就是字典的key)
字典.values() - 获取字典所有的值(返回一个序列，序列中的元素就是字典的value)
字典.items() - 获取字典所有的键值对(返回一个序列，序列中的元素是元祖，元祖中元素有两个分别是key和value)
"""
dict4 = {'x': 23, 'y': 89, 'z': 234, 'p': 100}
# 获取所有的key
keys = dict4.keys()
print(keys, type(keys))  # 返回值是序列，但是不是列表
# print(keys[0])
for item in keys:
    print(item)

# 获取所有的值
print(dict4.values())

print(dict4.items())  # dict_items([('x', 23), ('y', 89), ('z', 234), ('p', 100)])

# 6.setdefault
"""
字典.setdefault(key, value) - 给字典添加键值对(注意：如果key本来就存在，不会修改这个key的值 - 对原字典没有影响)
"""

dict4 = {'x': 23, 'y': 89, 'z': 234, 'p': 100}
dict4.setdefault('xx', 'abc')
print(dict4)    # {'x': 23, 'y': 89, 'z': 234, 'p': 100, 'xx': 'abc'}

dict4 = {'x': 23, 'y': 89, 'z': 234, 'p': 100}
dict4.setdefault('x', 'abc')
print(dict4)  # {'x': 23, 'y': 89, 'z': 234, 'p': 100}
