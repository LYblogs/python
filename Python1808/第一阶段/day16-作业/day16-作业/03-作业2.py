"""__author__ = 余婷"""


# 0.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
# 方法：
# a. 获取学生的姓名：getname()
# b. 获取学生的年龄：getage()
# c. 返回3门科目中最高的分数。get_course()

class Grade(object):
    def __init__(self, chinese: int, math: int, english: int):
        self.chinese = chinese
        self.math = math
        self.english = english

    def get_best_grade(self):
        """求最高分"""
        all_score = self.__dict__.values()
        return max(all_score)


class Student(object):
    def __init__(self, name, age, grage=Grade(0, 0, 0)):
        self.name = name
        self.age = age
        self.grade = grage

    def getname(self):
        return self.name

    def getage(self):
        return self.age

    def get_course(self):
        return self.grade.get_best_grade()


stu1 = Student('小明', 18, Grade(chinese=70, math=90, english=50))
print(stu1.get_course())


# 1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，并通过不同的构造方法创建实例。
# 至少要求 汽车能够加速 减速 停车。
# 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
class Auto(object):

    def __init__(self, color='白色', weight=0):
        self.tyre = 4
        self.color = color
        self.weight = weight
        self.speed = 0

    def add_speed(self, speed: int):
        if self.speed + speed >= 240:
            print('您已超速!')
            self.speed = 240
            return
        self.speed += speed

    def sub_speed(self, speed: int):
        if self.speed - speed < 0:
            self.speed = 0
            return
        self.speed -= speed

    def stop(self):
        self.speed = 0


class CarAuto(Auto):
    def __init__(self, color='', weight=0, air_conditioning='', cd=''):
        super().__init__(color, weight)
        self.air_conditioning = air_conditioning
        self.cd = cd

    def add_speed(self, speed: int):
        if self.speed + speed >= 260:
            print('您已超速!')
            self.speed = 260
            return
        self.speed += speed

    def sub_speed(self, speed: int):
        if self.speed - speed < 0:
            print('已经熄火！')
            self.speed = 0
            return
        self.speed -= speed


# 3.创建一个Person类，添加一个类字段用来统计Perosn类创建的对象的个数
class Person(object):
    count = 0

    def __init__(self, name=''):
        self.name = name
        Person.count += 1


p1 = Person('小明')
p2 = Person('小hua')
print(Person.count)

p3 = Person('小明')
p4 = Person('小hua')
print(Person.count)
