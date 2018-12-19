"""
迭代器：容器类型，可以存储多个数据，取的时候只能一个一个的取，并且取过之后的数据就不存在了。
生成器：就是迭代器。通过调用函数，获取yield后面的值而产生的元素。数据会在获取的时候去产生。
 调用一个带yiel

"""
#1.什么是生成式
"""
格式1：结果是一个生成器
(表达式 for  变量 in 序列) --> 展开:  
                             def  func1（）：
                               for  变量 in 序列：
                                  yield  表达式  
注意：表达式的结果就是每次循环生成器产生的数据。
这儿的for循环可以控制生成器产生数据的，和产生的值。
"""
gen1 = (10 for x in range(4))
print(next(gen1))

"""
格式2：
(表达式 for 变量 in 序列 if 条件语句)--> 展开：
                                       def func1（）
                                          for 变量 in 序列：
                                             if 条件语句：
                                                yield  表达式

"""
gen3 = (x for x in range(10)if x%2)
print(next(gen3))
print(next(gen3))
print(next(gen3))

re = list((x for x in range(10)if x% 2 ==0))
print(re)

#交换字典的键值对：{“a”：1,"b":2,"c":3}
dict1 = {"a":1,"b":2,"c":3}
dict2=dict((value,key)for key,value in dict1.items())
print(dict2)