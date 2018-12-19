"""__author__ = 余婷"""

"""
1.私有化
在类中，可以通过在属性名前，或者方法名前加__（注意：不能以__结尾）,那么这个属性或者方法就会变成私有的。
私有的属性和方法在类的外部不能使用
"""


class Person:
    __num = 100    # 私有的属性
    __number__ = 200   # 不是私有属性

    def __init__(self):
        self.name = '张三'
        self.__age = 18

    def __show_message(self):
        print(Person.__num)
        print('名字:', self.name, '年龄:', self.__age)

    def func1(self):
        self.__show_message()


# print(Person.__num)

p1 = Person()
print(p1.name)

# p1.__show_message()
p1.func1()

# print(p1.__age)

print(Person.__number__)


"""
2.私有化原理
python中没有真正的私有化, 不能从访问权限上控制属性和方法的使用。
只是在名字前有__但是没有以__结尾的名字前再加了'_类名',导致不能直接通过原属性和方法名进行访问
"""


class Dog:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color


dog1 = Dog('大黄', '黄色')
print(dog1.__dict__)
# print(dog1.__name, dog1.__color)
print(dog1._Dog__name)