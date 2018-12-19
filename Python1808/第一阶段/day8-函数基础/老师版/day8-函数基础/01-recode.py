"""__author__ = 余婷"""
"""
1.列表(list) - 可变，有序 - []

a.获取元素 - 通过下标获取元素

b.增删改
增 - append,insert,(extend)
删 - remove,del,pop,clear
改 - 列表[下标] = 新值

c.相关运算: +, *, in/not in, len(), list(), max(), min()

2.元祖(tuple) - 不可变，有序 - ()
a.获取元素 - 通过下标获取元素
变量1, 变量2 = 元素1, 元素2
变量1, *变量2 = 元素1, 元素2, 元素3, 元素4
(元素,)

c.相关运算: +, *, in/not in, len(), tuple(), max(), min()


3.字典(dict) - 可变, 无序 - {}
a.获取元素 - 通过键获取元素

b.增删改
增 - 字典[key] = 值； 字典1.update(字典2)
删 - del 字典[key]; 字典.pop(key); clear
改 - 字典[key] = 值；字典1.update(字典2)

c.相关运算:in/not in, len(), dict(), max(), min()
max和min - 取的是字典的key的最大值和最小值
"""
print(len({'a': 10, 'b': 20}))
dict1 = dict([(1, [1, 2]), ['a', 'b'], ('aaa', 100)])
print(dict1)

dict2 = {'a': 10, 'd': 20, 'c': 30}
print(max(dict2))
print(min(dict2))





