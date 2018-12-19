"""__author__ = 余婷"""
"""
1.类方法和静态方法
对象方法：
a.直接声明在类中
b.自带self参数
c.使用对象调用

类方法：
a.声明@classmethod后面
b.自带cls参数
c.使用类调用

静态方法：
a.声明@staticmethod后面
b.没有自带的参数
c.使用类调用


2.私有化
加__


3.getter和setter
a.属性名加_
b.@property后面声明函数，函数名属性名，没有其他参数，需要返回值
c.对象.属性(不带_)

a.属性名加_
b.@getter名.setter后面声明函数，函数名属性名，有一个参数，不需要返回值
c.对象.属性(不带_) = 值

4.继承
class 子类(父类):
    内的内容
    
继承就是让子类直接拥有父类的属性和方法

5.添加方法和属性

"""
class A:
    def __init__(self):
        self.a = 0
        self.b = ''


class B(A):
    def __init__(self):
        super().__init__()
        self.c = 10


b = B()



