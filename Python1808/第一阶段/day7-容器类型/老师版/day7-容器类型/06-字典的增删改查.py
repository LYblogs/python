"""__author__ = 余婷"""

# 1.查(获取字典的值)
"""
a.获取单个值
字典[key] - 获取字典中key对应的值 (注意：如果key不存在，会报错:KeyError)

字典.get(key) - 获取字典中key对应的值 (如果key不存在，不会报错，并且会返回一个默认值None)

None是python中的关键字，表示一个特殊值，(没有、空的意思)
"""
dog1 = {'name': '旺财', 'age': 3, 'color': '黄色', 'type': '土狗'}
print(dog1['name'])
print(dog1['color'])
# print(dog1['sex'])   # KeyError: 'sex'

print(dog1.get('age'))
print(dog1.get('type'))
print(dog1.get('sex'))

"""
b.遍历
"""
# 直接遍历字典拿到的是字典中所有的key
for key in dog1:
    print(key, dog1[key])

# 同时获取key和value（看着方便但是性能差，内存消耗多）
print(dog1.items())
for key, value in dog1.items():
    print(key, value)

# 2.增(添加键值对)
"""
字典[key] = 值  - 当key不存的时候，就是在字典中添加键值对
"""
dict1 = {'a': 100}
dict1['b'] = 200
print(dict1)

"""
字典1.update(序列)  -  将序列中的元素转换成键值对，然后再添加到字典1中

注意:在这儿的序列要求是能够转换成字典的序列。序列中的元素是只有两个元素的小序列
"""
dict1 = {'a': 100, 'b': 200}
# 当key值有重名的时候，会用序列中键值对对应的值，更新原字典的key对应的值
dict1.update({'aa': 10, 'bb': 20, 'a': 'abc'})
print(dict1)

dict1.update([[1, 2], ['a', 2], [2, 'b']])
print(dict1)

dict1.update([('aaa', 100), [12, 200]])
print(dict1)

# 3.改(修改key对应的值)
"""
字典[key] = 值  - 当key存在的时候，就是修改key对应的值
"""
dict1 = {'a': 10, 'b': 20}
dict1['a'] = 100
print(dict1)

# 4.删(删除键值对)
"""
a. del 字典[key]  - 删除字典中key对应的键值对
"""
person = {'name': '张三', 'age': 30, 'sex': '男'}
del person['sex']
print(person)

"""
b.字典.pop(key)  - 取出字典中key对应的值（删除整个键值对）
"""
person = {'name': '张三', 'age': 30, 'sex': '男'}
age = person.pop('age')
print(person, age)

person = {'name': '张三', 'age': 30, 'sex': '男'}
# 删除最后一个键值对(取出最后一个键值对, 以元祖的形式返回) - 无意义
value = person.popitem()
print(person, value)


