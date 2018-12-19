"""__author__ = 余婷"""
"""
1.文件操作和异常捕获
2.面向对象
a.类的声明
class 类名(父类列表):
    类的方法
    类的属性
    
b.创建对象
变量名 = 类名()

c.类中的方法： 对象方法、类方法、静态方法
d.类中的属性： 类的字段，对象属性
e.对象属性的增删改查：两套
f.私有化，getter和setter
g.继承
python中所有的类都是直接或者间接继承objct
继承子类会继承父类所有的属性和方法(私有的也可以继承)
添加对象属性：需要在子类的init方法中调用父类的init方法，来继承父类的对象属性

运算符重载：在类中实现相应的魔法方法让类的对象能够支持相应的运算符
__gt__ (>)   __lt__  (<)


3.pygame(了解)   
"""


class Person:
    def __init__(self):
        self.__name = '张三'


class Student(Person):
    def __init__(self):
        super().__init__()
        self.age = 10


stu1 = Student()
print(stu1.__dict__)

