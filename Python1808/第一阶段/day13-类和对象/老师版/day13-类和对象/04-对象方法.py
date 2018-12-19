"""__author__ = 余婷"""

"""
1.什么是对象方法
直接声明在类中，并且自带一个叫self的参数的函数

2.对象方法的调用 - 通过对象调用对象方法
对象.对象方法()

3.self (当前对象)
通过对象调用对象方法的时候，对象方法中的第一个参数self不用传参，
系统会自动将当前对象传给self。
哪个对象调用的，self就指向谁。

注意：当前类的对象能做的事情，self都能够做

"""


# 声明Person类
class Person:
    """人类"""

    # 声明了一个对象方法sleep
    def sleep(self, a):
        # self = p1, a = 10
        print('self:', self)
        print('睡觉!', a)
        self.run()

    def run(self):
        # self=p1
        print('跑')


#  创建Person的对象p1
p1 = Person()
print('p1:', p1)
p1.sleep(10)



