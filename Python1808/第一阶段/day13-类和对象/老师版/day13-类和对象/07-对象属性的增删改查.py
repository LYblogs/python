"""__author__ = 余婷"""


class Dog:
    def __init__(self, name, color, type=None):
        self.name = name
        self.color = color
        self.type = type


dog1 = Dog('旺财', '黄色', '二哈')
dog2 = Dog('才才', '黑色', '土狗')

# 1.查(获取对象属性的值)
"""
获取指定对象指定属性的值
a.对象.属性  - 属性不存在的时候会报错
b.getattr(对象, 属性名, 默认值) - 属性不存在的时候，如果设置了默认值，程序不崩溃，而是返回默认值
"""
print(dog1.name)
# print(dog1.name1)  # AttributeError: 'Dog' object has no attribute 'name1'

print(getattr(dog1, 'color'))
print(getattr(dog1, 'name1', None))

# 2.增、改
"""
a.对象.属性 = 值   
b.setattr(对象, 属性名, 值)

注意：属性存在的时候，对应的功能是修改属性的值。当属性不存在的时候是添加属性
"""
dog1.name = '大黄'    # 修改
print(dog1.name)

dog1.sex = '公'    # 添加
print(dog1.sex)

setattr(dog1, 'name', '热狗')  # 修改
print(dog1.name)

setattr(dog1, 'name2', '肉狗')  # 添加
print(dog1.name2)

# 3.删除
"""
a. del 对象.属性 
b. delattr(对象, 属性名)
"""
del dog1.name
# print(dog1.name)    # AttributeError: 'Dog' object has no attribute 'name'

delattr(dog1, 'color')
# print(dog1.color)  # AttributeError: 'Dog' object has no attribute 'color'

"""
注意： 对象属性的增删改查，都是针对指定的那一个对象，不会影响其他对象
"""

# 4.__slots__魔法
"""
__slots__是用来约束当前这个类有哪些对象属性
"""


class Student:
    # Student类的对象只能有name,study_id,age和sex属性
    __slots__ = ('name', 'study_id', 'age', 'sex')

    def __init__(self, name, age):
        self.name = name
        self.study_id = '001'
        self.age = age
        # self.sex = ''


stu1 = Student('夏明', 18)
# stu1.neme = '小明'
stu1.sex = '男'
