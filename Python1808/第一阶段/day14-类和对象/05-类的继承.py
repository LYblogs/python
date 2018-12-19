"""
1.继承
python中的类支持继承，并且支持多继承
python中默认情况是继承自object（object是python中所有类的基类）

（被继承者）（继承者）
    父类  和   子类

继承就是让子类直接拥有父类中的内容

b.可以继承哪些内容
对象属性
类的字段
对象方法
__slots__魔法不会被继承
"""
class Person:
    num =61
    def __init__(self):
        self.name ="张三"
        self.age =0
        self.sex ="男"
    def show_message(self):
        print("%s你好吗"%self.name)
    @classmethod
    def people(cls):
        print("世界有%d亿人"%cls.num)
#Student类继承Person
class Student(Person):
     pass
stu1 =Student()
print(stu1.name)
print(Student.num)
stu1.show_message()
Student.people()
