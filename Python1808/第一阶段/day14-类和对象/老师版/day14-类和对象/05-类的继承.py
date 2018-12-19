"""__author__ = 余婷"""

"""
1.继承
python中的类支持继承，并且支持多继承。
python中默认情况是继承自object（object是python中所有类的基类）

a.什么是继承
一个类可以继承另外一个类，继承者我们叫子类，被继承者叫父类。继承就是让子类直接拥有父类中的内容

b.可以继承哪些内容
所有的属性和方法都可以继承
"""


class Person(object):
    num = 61

    # 注意：__slots__对应的值不会被继承
    __slots__ = ('name', 'age', 'sex')

    def __init__(self):
        self.name = '张三'
        self.age = 0
        self.sex = '男'

    def show_message(self):
        print('%s你好吗?' % self.name)


# Student类继承自Person类
class Student(Person):
    pass


# 创建学生对象
stu1 = Student()
# 对象属性可以继承
print(stu1.name, stu1.age, stu1.sex)

# 类的字段可以继承
print(Student.num)

# 对象方法可以继承
stu1.show_message()



p1 = Person()
# p1.color = '黄色'
stu1.color = '白色'
print(stu1.color)






