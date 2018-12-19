# 0.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
# 方法： a. 获取学生的姓名：getname()
# b. 获取学生的年龄：getage()
# c. 返回3门科目中最高的分数。get_course()
# class Student:
#     def __init__(self,name,age,*args):
#         self.name =name
#         self.age =age
#         self.score =args
#     def get_name(self):
#         return "名字是：%s"%self.name
#     def get_age(self):
#         return "年龄为：%s"%self.age
#     def get_course(self):
#         return "最高成绩为：%d" % max(self.score)
#
# s1 =Student("小明",20,80,100,98)
# print(s1.get_name())
# print(s1.get_age())
# print(s1.get_course())

# 1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，
# 并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。
# 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
# class Auto:
#     def __init__(self,tire,color,weight,speed):
#         self.tire =tire
#         self.color =color
#         self.weight =weight
#         self.speed =speed
#     def speed_up(self):
#         return "汽车加速，速度为：%dkm/h"%(self.speed +3)
#     def speed_down(self):
#         return "汽车减速，速度为：%dkm/h" % (self.speed - 3)
#     def  speed_stop(self):
#         return "汽车的速度为：0km/h,汽车停车"
# class CarAuto(Auto):
#     def __init__(self,tire,color,weight,speed,air,CD):
#         super().__init__(tire,color,weight,speed)
#         self.air =air
#         self.cd =CD
#     def speed_up(self):
#         return "小汽车的速度为：%dkm/h"%(self.speed +5)
#     def speed_down(self):
#         return "小汽车的速度为：%dkm/h" % (self.speed - 5)
# a1 =Auto(8,"黄色","500kg",50)
# print(a1.speed_up())
# print(a1.speed_down())
# print(a1.speed_stop())
# c1 =CarAuto(4,"白色","200kg",80,"美的","蓝莲花")
# print(c1.speed_up())
# print(c1.speed_down())

# 2.创建一个名为User 的类，其中包含属性firstname 和lastname ，
# 还有用户简介通常会存储的其他几个属性。在类User 中定义一个名 为describeuser() 的方法，
# 它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候。
# 管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承User类。
# 添加一个名为privileges 的属性，
# 用于存储一个由字符串(如"can add post"、"can delete post"、"can ban user"等)组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。

# class User:
#     def __init__(self,firstname,lastname,id,password):
#         self.first_name =firstname
#         self.last_name =lastname
#         self.password =password
#         self.id =id
#     def describeuser(self):
#         return ("""姓名：%s
# 密码：%s
# id: %s""")%(self.last_name+self.first_name,self.password,self.id)
#     def greetuser(self):
#         return "%s您好，欢迎使用"%(self.last_name+self.first_name)
#
# class Admin(User):
#     def __init__(self,firstname,lastname,id,password,privileges:list):
#         super().__init__(firstname,lastname,id,password)
#         self.privileges =privileges
#     def show_privileges(self):
#         for i in self.privileges:
#             print("管理员%s"%i)
#
# u1 =User("毅","李","小❀","aaaa1234")
# print(u1.describeuser())
# print(u1.greetuser())
# a1 =Admin("毅","李","小❀","aaaa1234",["can add post","can delete post","can ban user"])
# a1.show_privileges()


# 3.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
# class Person:
#     num =0
#     def __init__(self):
#         Person.num+=1
# p1=Person()
# p2=Person()
# p3=Person()
# print(Person.num)


# (尝试)5.写一个类，其功能是：1.解析指定的歌词文件的内容 2.按时间显示歌词
# 提示：歌词文件的内容一般是按下面的格式进行存储的。
# 歌词前面对应的是时间，在对应的时间点可以显示对应的歌词
# class Song:
#     def pars_song(self):
