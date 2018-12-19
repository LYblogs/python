"""__author__ = 余婷"""
"""
a.迭代器: 容器，可以同时存储多个数据，取的时候只能一个一个的取，并且取过的数据在容器中就不存在了


b.生成器: 就是迭代器, 数据是通过调用函数，获取yield后面的值而产生的。数据会在获取的时候去产生

调用一个带yield关键的函数，就是创建一个生成器。
"""
# 1.什么是生成式
"""
格式1： - 结果是一个生产器(迭代器)
(表达式 for 变量 in 序列) --> 展开：
                          def func():
                            for 变量 in 序列:
                                yield 表达式
   
注意：表达式的结果就是每次循环生成器产生的数据  
     这儿的for循环可以控制生成器产生数据的个数，和产生的值                 
"""
gen1 = (x for x in range(4))
print(gen1)   # <generator object <genexpr> at 0x1007a5200>
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))


gen2 = (x*10 for x in range(4))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

"""
格式2：
(表达式 for 变量 in 序列 if 条件语句)  --> 展开：
                                        def func1():
                                            for 变量 in 序列:
                                                if 条件语句:
                                                    yield 表达式
"""
gen3 = (x for x in range(10) if x % 2)
print(next(gen3))   # 1
print(next(gen3))   # 3
print(next(gen3))   # 5

re = list(x for x in range(10) if x % 2 == 0)
print(re)

# 练习:交换字典的键值对:{'a':1, 'b':2, 'c':3} --> {1:'a', 2:'b', 3:'c'}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = dict((value, key) for key, value in dict1.items())
print(dict2)




