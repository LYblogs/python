"""
1.clear
字典.clear() - 清空字典（删除字典中所有的键值对）
"""
dict1 = {"a":10,"b":20,"c":30}
dict1.clear()
print(dict1)  # {}
# 2.copy
"""
字典.copy（） - 复制字典中的所有的键值对，产生一个新的字典

"""
dict1 = {"a":10,"b":20,"c":30}
dict2 =dict1.copy() #浅拷贝   会产生新的地址
dict2 =dict1 #直接赋地址

# 3.fromkeys()
"""
dict.fromkeys(序列，值) - 一序列中的元素作为key，值作为所有key对应的默认值，创造一个字典。

"""
dict3 = dict.fromkeys("eqwe",100)
print(dict3)  #{'e': 100, 'q': 100, 'w': 100}

# 4.get
"""
字典.get(key) - 获取key对应的值，如果key不存在，返回None
字典.get（key，值）-获取key对应的值，如果key不存在，返回对应的值
"""

# 5.keys，values，items
"""
字典.keys() - 获取字典所有的key （返回序列，序列中的元素就是字典的key）
字典.values（） - 获取字典所有的值 （返回序列，序列中的元素就是字典的值）
字典.items （） - 获取字典所有的键值对（返回序列，序列中的元素是元组，元组的元素有两个，分别就是字典的key和value）

"""
dict1 = {"a":12,"b":20,"c":30}
keys = dict1.keys()  #返回值是序列，不是列表
for i  in keys:
    print(i)
print(keys)  #dict_keys(['a', 'b', 'c'])



