"""__author__ = 余婷"""
"""
1.什么是迭代器(iter)
迭代器是python中的容器类的数据类型，可以同时存储多个数据。
取迭代器中的数据只能一个一个的取，而且取出来的数据，在迭代器就不存在了

2.迭代器中数据的来源
a.将其他序列转换成迭代器
b.使用生成式、生成器去产生数据
"""
# 1.将数据转换成迭代器
"""
所有的序列都可以转换成迭代器
"""
# 将字符串转换成迭代器
iter1 = iter('abcd')
print(iter1)

iter2 = iter([1, 10, 100, 1000])
print(iter2)

iter3 = iter({'name': '小明', 'age': 20})
print(iter3)

# 2.获取迭代器中的元素
"""
a.
next(迭代器) / 迭代器.__next__() - 取出迭代器中第一个元素(已经取出来的元素再也回不到迭代器中了)
"""
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
# print(next(iter1))   # 当迭代器是空的时候，使用next获取元素，会出现StopIteration异常

print(iter2.__next__())
print(next(iter2))

"""
b.通过for循环取出迭代器中每个元素
"""
for x in iter2:
    print('==:', x)

# print(next(iter2))   # 出现异常StopIteration，因为for循环已经将这个迭代器中的元素取完了
