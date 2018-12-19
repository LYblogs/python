"""__author__ = 余婷"""

"""
类中的方法分为：对象方法, 类方法和静态方法
1.对象方法
a.直接声明在类中
b.有默认参数self
c.通过对象去调用: 对象.对象方法()

2.类方法
a.在声明前添加@classmethod
b.有默认参数cls, 调用的时候不需要给cls传参。系统会自动将调用当前类方法的类传给cls。
  cls最终指向的是一个类，类可以做的事情cls都可以做
c.通过类去调用: 类.类方法()


3.静态方法
a.在声明前添加@staticmethod
b.没有默认参数
c.通过类去调用：类.类方法() 

4.对象方法、类方法和静态的方法的选择
a.什么时候使用对象方法：
当实现函数的功能需要用到对象的属性的时候就使用对象方法

b.什么时候使用类方法：
实现函数的功能不需要对象的属性，但是需要类的时候就使用类方法

c.什么时候使用静态方法
实现函数的功能既不需要对象的属性，也不需要类的时候，就使用静态方法
"""


class Person():

    # 类的字段
    num = 61

    def __init__(self, name):
        self.name = name

    # 对象方法
    def eat(self, food):
        # print(Person.num)
        print('%s在吃%s' % (self.name, food))

    # 类方法
    @classmethod
    def destroy(cls):
        # cls = Person
        print('cls:',cls)
        print('人类破坏环境')

        # 可以用cls来创建对象
        p1 = cls('小明')
        p1.eat('面包')

        # 可以用cls使用类的字段
        print(cls.num)

        # 可以用cls调用类相关的方法

    # 静态方法
    @staticmethod
    def hit_animal():
        print('人类殴打小动物!')
        print(Person.num)


print('Person:', Person)
Person.destroy()
Person.hit_animal()


# 练习：
# 数学类，属性：pi  功能：求两个数的和,  求一个圆的面积
class Math:
    pi = 3.1415926

    @staticmethod
    def sum(num1, num2):
        return num1+num2

    @classmethod
    def circle_area(cls, r):
        return cls.pi * (r ** 2)

    # @staticmethod
    # def circle_area(r):
    #     return Math.pi * (r ** 2)


class YTMath(Math):
    pi = 3.14



print(Math.sum(10, 3.10))
print(Math.circle_area(2))

print(YTMath.circle_area(2))
