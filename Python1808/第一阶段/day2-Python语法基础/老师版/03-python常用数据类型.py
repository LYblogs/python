"""__author__ = 余婷"""

# python中常用的数据类型有：整型、浮点型、布尔、字符串、列表、字典、元祖、集合、函数等....
# 1.常见数据类型的字面量(常量)
"""
整型: 100, 23, -129  -- 所有的整数
浮点型: 12.3, 45.0, -0.1123  -- 所有的小数
布尔: True, False  -- 只有两个值
字符串: 'abc', "ahjs", '348sj', "上的+-"  -- 由双引号或者单引号括起来的内容
列表: [12, 'abc', True]
元祖：(23, 89, 'asd')
字典:{'ab': 120, 18:'abc'}
"""
100
12.3
True
'348sj'
[12, 'abc', True]
(23, 89, 'asd')
{'ab': 120, 18:'abc'}

# 2.数字相关类型
"""
python中和数字相关的类型：整型、浮点型、布尔、复数(虚数)
a.整型(int):整数对应的类型，包含了所有的整数。python3.x中整数对应的类型只有一个：int
                                      python2.x中整数对应的类型有:int和long
                                      
python中的整数，除了可以用十进制表示，还可以用二进制、八进制和十六进制进行表示
"""
12
200
-100

"""
a.浮点型(float): 小数对应的类型，包含了所有小数。
支持科学计数法
"""
12.90
-12.03
2e4   # 20000.0
print(2e4)
print(3e-2)

"""
c.布尔(bool): 只有True和False， 其中True表示真,False表示假。
             True实质就是数字1，False实质是数字0
True和False都是关键字
"""
print(True, False)
print(1+True, 1+False)


"""
d.复数(complex): 所有的虚数对应的类型
数字后面加j，来表示复数的虚部。实部就是普通数字
"""
10+1j
20-9j
print((10+1j)+(20-9j))

# 3.type函数
"""
type(数据) - 获取数据对应的类型
"""
print(type(100))
print(type(10+2j))

# 4.isinstance函数
"""
isinstance(数据,类型) - 判断指定的数据是否是指定的类型，结果是布尔值
"""
isinstance(100, float)   # 判断100是否是float类型
print(isinstance(100, float))   # False
print(isinstance(100, int))     # True

# 5.类型的强制转换
"""
类型名(数据) - 将指定数据转换成指定类型
整型转成浮点型: 在整数的后面加.0    float()
浮点型转换成整型: 只保留小数点前面的整数部分    int()
其他类型转布尔: 0转换成False,其他的转换成True   bool()

注意：复数不能转换成整型和浮点型，可以转换成布尔类型（不管什么数据都可以转换成布尔）
"""
print(float(False))
print(int(False))
print(bool(10+10j))

