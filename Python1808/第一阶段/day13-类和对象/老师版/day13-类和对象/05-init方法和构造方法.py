"""__author__ = 余婷"""
"""
0.魔法方法
python类中，用__开头并且是__结尾的方法，就是魔法方法。
魔法方法不需要主动调用，都是自动调用的

1.__init__方法
a.是对象方法
b.不需要自己调用，会被自动调用
c.专门用来对对象进行初始化的

2.构造方法
概念：函数名和类名一样的函数，就是构造方法
当我们创建类的时候，系统会自动创建这个类的构造方法，用来创建对象。
当我们通过构造方法创建对象的时候，系统会自动调用init方法来对创建好的对象进行初始化

注意：当init方法中除了self以外如果需要别的参数，那么这些参数是通过构造方法来传的参
     只要调用了构造方法，就会产生新的对象。（想要对象，调用构造方法）
"""


class Person(object):
    def __init__(self, name, age=0):
        print('self', self)
        print('init方法', name)

"""
def Person(*args, **kwargs):
    在堆中开辟空间创建对象
    对象.__init__(*args, **kwargs)
    return 对象
"""
p0 = Person('abc', 10)

p1 = Person('abc', 10)
print('p1:', p1)


p2 = Person('123', age=20)
print('p2:', p2)
# p3 = Person()
p3 = p1


# 模拟构造方法和init方法
def __init__(a, b):
    print('自己实现', a, b)


def Person1(*args, **kwargs):
    # args = (10, 20)
    print('创建对象')
    __init__(*args, **kwargs)

    print('返回对象')


Person1(10, 20)
