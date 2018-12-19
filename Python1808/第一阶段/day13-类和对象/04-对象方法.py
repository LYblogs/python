"""
1.什么是对象方法
直接声明在类里面，并且自带一个self的参数的函数

2.对象方法的调用 - 通过对象调用对象方法
对象.对象方法（）

3.self（当前对象）
通过对象调用对象方法的时候，对象方法中的第一个参数self不用传参；
系统会自动将当前对象传给self
哪个对象调用的，self就指向谁。

注意：当前类的对象能做的时候，self都能做，必须是通过对象调用才有用
"""

# 声明Person类
class Person:
    """人类"""
    #声明了一个对象方法sleep
    def sleep(self):
        print("睡觉")
        self.run()
    def run(self):
        print("跑")
#创建一个Person类的对象i
i =Person()
i.sleep()
