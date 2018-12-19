"""__author__ = 余婷"""

"""
1.多继承
多继承： 让一个类同时继承多个类

注意：实际开发的时候，一般不使用多继承
"""


class Animal:
    num = 61

    def __init__(self, name='名字', age=0, color=''):
        self.name = name
        self.age = age
        self.color = color

    def show_info(self):
        print('=====')
        # print('名字:%s 年龄:%d 颜色:%s' % (self.name, self.age, self.color))


class Fly:
    info = '飞'

    def __init__(self, distance=0, speed=0):
        self.distance = distance
        self.speed = speed

    @staticmethod
    def show():
        print('会飞！')


# 让Birds同时继承Animal和Fly
class Birds(Fly, Animal):
    pass


bird1 = Birds()
# 对象属性只能继承第一个类的对象属性
print(bird1.speed)

# 两个类的字段都能继承
print(Birds.num, Birds.info)

# 两个类的方法都能继承
Birds.show()
bird1.show_info()


"""
2.多态
类的特点：封装、继承、多态

封装：可以对多条数据(属性)和多个功能(方法)进行封装
继承：可以让一个类拥有另外一个类的属性和方法
多态：有继承就有多态(一个事物的多种形态)
"""

