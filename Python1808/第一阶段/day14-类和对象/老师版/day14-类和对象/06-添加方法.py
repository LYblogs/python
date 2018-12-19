"""__author__ = 余婷"""
"""
子类除了拥有从父类继承下来的属性和方法，还拥有属于自己的属性和方法

1.在子类中添加方法
a.添加一个新的方法
直接在子类中声明其他的方法; 
添加后子类可以调用自己的方法也可以调用父类的方法，但是父类不能调用子类的方法

b.重写父类的方法: 重新实现父类的方法
完全重写 - 覆盖父类的功能  - 直接在子类中重新实现父类的方法
部分重写 - 保留父类的功能，添加新的功能 - 在子类中实现父类方法的时候通过super()去调用父类的方法，
                                    再添加新的功能
注意：a.可以子类的方法中通过super()去调用父类的方法    
super(类, 对象) - 获取对象中父类的部分(要求对象是这个指定的类的对象)  
b.静态方法中不能使用super()

                         


c.类中方法的调用过程
通过对象或者类调用方法的时候，先看当前类中是否声明过这个方法，如果声明过就直接调用当前类对应的方法;
如果当前类中没有声明过，会去找父类中有没有声明过这个方法，声明过就调用父类的方法;
如果父类中也没有声明过，就去找父类的父类...以此类推，直到object中也没有声明过，程序才会崩溃
"""


class Person:
    # 类的字段
    num = 61

    # 对象属性
    def __init__(self):
        self.name = '张三'
        self.age = 0
        self.sex = '男'

    def fun1(self):
        print('Person的对象方法')

    # 方法
    def show_message(self):
        print('%s,你好吗？' % self.name)

    @staticmethod
    def info():
        print('我是人类')


class Student(Person):

    def study(self):
        print('%s在学生' % self.name)

    @classmethod
    def message(cls):
        super().info()
        print('我是学生!')

    # 完全重写
    @staticmethod
    def info():
        print('我是学生！！！')

    # 保留父类的功能
    def show_message(self):
        super().show_message()
        print('我去上学~')
        super().fun1()




# Student.info()