"""
1.什么是迭代器（iter）
迭代器是python中的容器类的数据类型，可以同时存储多个数据。
取迭代器中的数据只能一个一个取，而且取出来的数据，在迭代器中就不存在了。

2.迭代器中数据的来源
a.将其他序列中的数据转换成迭代器（所有序列都能转换成迭代器）
b.使用生成式、生成器去产生数据

"""
# 1.将数据转换成迭代器
#将字符串转换成迭代器
iter1 = iter("asdsad")
print(iter1) #<str_iterator>

#将列表转换成迭代器
iter2 = iter([1,2,555])
print(iter2) #<list_iterator>
#将字典转换成迭代器
iter3 =iter({"name":"小明","age":28})
print(iter3)#  <dict_keyiterator>

#2.获取迭代器中的元素
"""
next(迭代器) - 取出迭代器中第一个元素（已经取出的元素不能再回去）
迭代器.__next__() - 取出迭代器中第一个元素（已经取出的元素不能再回去）

b.通过for 循环取出迭代器中的每个元素
"""
print(next(iter("迭代器")))
iter1 = iter("asds")
print(next(iter1)) #a
print(next(iter1)) #b
print(next(iter1)) #c
print(next(iter1)) #d
# print(next(iter1))  #当迭代器是空的时候，再取就会报错：StopIteration