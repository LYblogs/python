"""__author__ = 余婷"""
"""
1.类和对象的概念
类：拥有相同属性和相同功能的对象的集合
对象: 类的实例

2.类的声明
class 类名:
    类的内容  
    
3.对象的创建
类()

4.对象方法
a.直接声明在类中，并且自带一个self参数
b.通过对象来调用: 对象.对象方法()
c.通过对象调用的时候，self不需要传参，系统会将当前对象传给self

5.构造方法和init方法
方法名和类名相同的方法就是构造方法。专门用来创建对象的
当创建对象的时候，会自动调用init方法

6.对象属性
a.声明在init方法中的
b.self.属性 = 值
c.对象.属性

7.对象属性的增删改查
对象.属性 / getattr(对象, '属性名', 默认值)
对象.属性 = 值   / setattr(对象, '属性名', 值)
del 对象.属性   / delattr(对象, '属性名')
__slots__ = ('属性名') - 约束当前类有哪些对象属性

8.类的字段
声明在类中，函数的外面的变量
"""
# def Perosn(*args, **kwargs):
#     对象 = 开辟空间创建对象
#     对象.__init__(*args, **kwargs)
#     return 对象


class Person:
    # 注意: 如果给类的__slots__赋了值，那么这个类的对象的__dict__属性就不能用了
    # __slots__ = ('name', 'age', 'sex')

    def __init__(self):
        self.name = '张三'
        self.age = 18
        self.sex = '男'


p1 = Person()
print(p1.__dict__)

p2 = Person()
p2.name = '李四'
print(p2.__dict__)