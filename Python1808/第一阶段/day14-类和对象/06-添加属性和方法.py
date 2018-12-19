"""
1.在子类中添加方法
子类除了拥有从父类继承的属性和方法，还拥有自己的属性和方法；
a.添加一个新的方法
直接在子类中声明其他的方法；
添加后子类可以用父类，父类不能用子类的
b.重写父类的方法
完全重写 -覆盖父类的功能 - 直接在子类中重新实现父类的方法
部分从写 - 保留父类的功能 ，添加新的功能 -
在子类中实现父类的方法时通过super（）去调用父类的方法，再添加新的功能

注意：a.可以子类的方法中通过super（）去调用父类的方法
super(类，对象) - 获取对象中父类的部分（要求对象是指定的类的对象）
b.静态方法中不能用super
c.类中方法的调用过程
通过类或者对象调用方法的时候，先看当前类中声明过这个方法，如果声明过，就直接调用当前类对应的方法
如果当前类中没有声明过，会去找父类中有没有声明过这个方法，声明过就调用父类的方法；
如果父类中也没有声明过，就去找父类的父类，然后以此类推直到找到object为止，
直到object里面也没有才会报错

1.在子类中添加方法
"""
class Person:
    num =61
    def __init__(self):
        self.name ="张三"
        self.age =50
        self.sex ='男'
    def show_message(self):
        print("%s你好吗？"%self.name)
    @staticmethod
    def info():
        print("我是人类")
class Student(Person):
    def studay(self):
        print("%s在学习"%self.name)
    @classmethod
    def student_game(cls):
        print("%s在玩游戏"%cls.num)
    #完全重写
    @staticmethod
    def info():
        print("我是学生")
    #保留父类的功能
    def show_message(self):
        super().show_message()
        print("我去上学")
s1 =Student()
s1.studay() #张三在学习
s1.student_game()#61在玩游戏
Student.info() #我是学生
Person.info() #我是人类
s1.show_message() #张三你好吗？
                  #我去上学
p1 =Person()
p1.show_message() #张三你好吗？