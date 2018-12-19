"""__author__ = 余婷"""

# 1.类的字段
"""
a.直接声明在类里面，函数的外面的变量就是类的字段
b.类的字段需要通过类来使用： 类.字段  - (不管是在类里面还是类的外面都一样)

不会因为对象不同而不一样的数据就声明成类的字段
"""


class Person:
    # 声明了一个字段number
    number = 61

    def show_number(self):
        print('人类的数量：%d' % Person.number)


print(Person.number)
Person().show_number()

# 2.内置类属性
"""
内置属性就是声明类的时候，类中已经声明好的属性(包含类的字段和对象的属性)
"""


class Dog:
    """说明文档:狗类"""
    # 类的字段
    type = '犬科'

    # 对象属性
    def __init__(self, name='', age=0, color=''):
        self.name = name
        self.age = age
        self.color = color

    # 对象方法
    def eat(self, food):
        print('%s在吃%s' % (self.name, food))

    # 类方法
    @classmethod
    def shout(cls):
        print('汪汪汪~~~~')

    # 静态方法
    @staticmethod
    def bite():
        print('狗咬人！！！')


dog1 = Dog('小黑', 3, '黑色')

# a.__name__
"""
类.__name__  - 获取类的名字(字符串)
"""
class_name = Person.__name__
print(class_name, type(class_name))

# with open(Person.__name__+'.json', 'w') as f:
#     pass

# b.__class__
"""
对象.__class__  - 获取对象对应的类(结果是一个类，原来类能做的事情它都可以做)
"""
aa = dog1.__class__

d1 = Dog()
d2 = aa()
print(d1, d2)

print(Dog.type)
print(aa.type)

print(dog1.__class__.__name__)   # 获取对象对应的类的名字

# c.__dict__
"""
(了解)类.__dict__   - 获取当前类的所有的类的字段及其对对应的值
(重点)对象.__dict__ - 将当前对象所有的对象属性及其值转换成字典,key是属性名,value是属性的值
"""
print(Dog.__dict__)
print(dog1.__dict__)

# d.__base__
"""
类.__bases__ - 获取当前类的父类(以元祖的形式返回，元祖中的元素就是类的父类)
"""
print(Dog.__bases__)

# e.__module__
"""
类.__module__  - 获取当前类所在的模块的模块名
"""
print(Dog.__module__)
print(int.__module__)

# f.__doc__
"""
类.__doc__  - 获取类的说明文档
"""
print(Dog.__doc__)
print(int.__doc__)






