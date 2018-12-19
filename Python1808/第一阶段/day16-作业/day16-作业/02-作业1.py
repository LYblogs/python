"""__author__ = 余婷"""


# 1.声明⼀个电脑类: 属性:品牌、颜⾊、内存⼤小 方法:打游戏、写代码、看视频
# a.创建电脑类的对象，然后通过对象点的⽅方式获取、修改、添加和删除它的属性
# b.通过attr相关⽅方法去获取、修改、添加和删除它的属性
class Color(object):
    white = (255, 255, 255)
    black = (0, 0, 0)

    def __init__(self, r, g, b):
        self.__red = r
        self.__green = g
        self.__blue = b


class Computer(object):
    """电脑类"""
    def __init__(self, brand='', color=None, memory=0):
        self.brand = brand
        self.color = color
        self.memory = memory

    def play_game(self, game_name):
        print('玩%s' % game_name)

    def Coding(self):
        print('写代码')

    def watch_videos(self):
        print('看视频')


cp1 = Computer('外星人', Color.black, 16)

# 查
print(cp1.brand)
print(getattr(cp1, 'brand', '联想'))

# 增、改
cp1.brand = '苹果'    # 修改
cp1.name = '小黑'  # 增加
setattr(cp1, 'brand', '三星')
setattr(cp1, 'age', 3)

# 删
del cp1.color
delattr(cp1, 'name')


# 2.声明⼀个人的类和狗的类:
# 狗的属性:名字、颜⾊、年龄
# 狗的⽅法:叫唤
# 人的属性:名字、年龄、狗
# 人的⽅方法:遛狗
# a.创建⼈的对象⼩明，让他拥有⼀一条狗大黄，然后让小明去遛大黄

class Dog(object):
    def __init__(self, name='', color=None, age=0):
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print('%s在嗷嗷叫~' % self.name)


class Person(object):
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        self.dog = None

    def took_the_dog(self):
        if self.dog:
            print('%s牵着%s在草地上玩儿' % (self.name, self.dog.name))

        else:
            print('没有🐶，遛自己吧！')


p1 = Person('小明', 18)
p1.dog = Dog('大黄', '黄色', 2)
p1.took_the_dog()


# 4.创建⼀一个学⽣生类:
# 属性:姓名，年龄，学号
# 方法:答到，展示学生信息
# 创建⼀一个班级类:
# 属性:学⽣，班级名
# 方法:添加学生，删除学生，点名, 求班上学生的平均年龄
from random import randint


class Student(object):
    def __init__(self, name, age=0, study_id=''):
        self.name = name
        self.age = age
        self.study_id = study_id
        # 是否在上课
        self.is_in_class = bool(randint(0, 1))

    def reply(self):
        print('%s，到！' % self.name)

    def show_info(self):
        print('名字:%s，年龄:%d，学号:%s' % (self.name, self.age, self.study_id))


class Class(object):
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.__creat_id = (self.name+str(x).rjust(3, '0') for x in range(1, 101))

    def add_student(self):
        # 输入信息
        name = input('姓名:')
        age = int(input('年龄:'))
        study_id = next(self.__creat_id)
        # 创建学生对象
        stu1 = Student(name, age, study_id)
        self.students.append(stu1)

    def del_student(self):
        """按姓名删除学生"""
        is_exist = False
        del_name = input('请输入要删除的学生的名字:')
        for stu in self.students[:]:
            if del_name == stu.name:
                # 有这个学生
                is_exist = True
                stu.show_info()
                is_del = input('是否删除(Y/N)?:')
                if is_del == 'Y':
                    self.students.remove(stu)
                    print('删除成功')

        if not is_exist:
            print('这个学生不存在！！！')

    def naming(self):
        """点名"""
        for stu in self.students:
            print(stu.name)
            if stu.is_in_class:
                stu.reply()

    def average_age(self):
        """ 平均年龄 """
        sum1 = 0
        for stu in self.students:
            sum1 += stu.age
        return sum1 / len(self.students)

    def show_student_info(self):
        """显示所有学生信息"""
        for stu in self.students:
            stu.show_info()


# 创建班级对象
class1 = Class('py1808')

# 添加5个学生
for _ in range(3):
    class1.add_student()

# 显示班级所有学生的信息
class1.show_student_info()

# 删除学生
class1.del_student()


# 显示班级所有学生的信息
class1.show_student_info()

#
# 添加1个学生
class1.add_student()
# 显示班级所有学生的信息
class1.show_student_info()
print('平均年龄:%.2f' % class1.average_age())
