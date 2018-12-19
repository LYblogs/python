"""
#####1.查（获取字典的值）
a.获取单个值
字典[key] - 获取字典中key对应的值（如果key不存在，会报错 # KeyError:）
字典.get（key） - 获取字典中key对应的值 （如果key不存在，不会报错，会返回值None）

None是python中的关键字，表示一个特殊值（没有、空的意思）
"""
dog1 ={"name":"旺财","age":3,"color":"绿色"}
print(dog1["name"])

print(dog1.get(""))

"""
b.遍历

"""
#直接遍历字典，拿到的是key值
for x in dog1:
    print(x)
for key,value in dog1.items():
    print(key,value)


#2.增（添加键值对）
"""
字典[key] = 值 - 当key不存在的时候，就是在字典中添加键值对


"""
dog1 ={"name":"旺财","age":3,"color":"绿色"}
dog1["价格"] = 2000
print(dog1)

"""
字典1.updatr(序列) - 将序列中的元素转换成键值对，然后再添加到字典1中

注意：在这儿的序列要求是能够转换成字典的序列。序列中的元素只有两个元素小序列

"""
dog1.update({"aa":10})
print(dog1)
#当key值有重名的时候，会用序列中键值对对应的值，更新原字典对应的值

#3.改（修改key对应的值）
"""
字典[key] = 值 -  当key存在的时候，就是修改key对应的值

"""
dict1 = {"a":10,"b":20}
dict1["a"] = 99
print(dict1)

#4.删（删除键值对）
"""
a.del 字典[key] - 删除字典中key对应的键值对
b.字典.pop（key） - 取出key对应的值（删除整个键值对）
"""
del dict1["a"]
print(dict1)
dog1 ={"name":"旺财","age":3,"color":"绿色"}
print(dog1.pop("age"))
print(dog1)
#删除最后一个键值对（取出最后一个键值对，以元组的形式返回）
dog1 ={"name":"旺财","age":3,"color":"绿色"}
value  = dog1.popitem()
print(dog1,value)