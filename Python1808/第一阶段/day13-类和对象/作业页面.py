# # 1.声明一个电脑类: 属性:品牌、颜色、内存大小 方法:打游戏、写代码、看视频
# #
# # a.创建电脑类的对象，然后通过对象点的方式获取、修改、添加和删除它的属性
# #
# # b.通过attr相关方法去获取、修改、添加和删除它的属性
#
# class Computer:
#     def __init__(self,brand,color,memory_size):
#         self.brand =brand
#         self.color =color
#         self.memory_size =memory_size
#     def play_game(self):
#         print("打游戏")
#     def write_code(self):
#         print("写代码")
#     def see_video(self):
#         print("看视频")
#
#
# c1 =Computer("华硕","黑色","4GB")
# #获取
# print(c1.brand)
# print(getattr(c1,"brand"))
# print(c1.color)
# print(getattr(c1,"color"))
# print(c1.memory_size)
# print(getattr(c1,"memory_size"))
# #修改
# c1.brand ="外星人"
# setattr(c1,"brand","苹果")
# c1.color = "粉色"
# setattr(c1,"color","白色")
# c1.memory_size = "16GB"
# setattr(c1,"memory_size","32GB")
# print(c1.brand)
# print(c1.color)
# print(c1.memory_size)
# #增加
# c1.price = 32000
# setattr(c1,"price",20000)
# print(c1.price)
# #删除
# del c1.color
# delattr(c1,"price")
# # print(c1.price) AttributeError: 'Computer' object has no attribute 'price'
# # print(c1.color) #AttributeError: 'Computer' object has no attribute 'color'

# # 2.声明一个人的类和狗的类:
# #
# # 狗的属性:名字、颜色、年龄
# #
# # 狗的方法:叫唤
# #
# # 人的属性:名字、年龄、狗
# #
# # 人的方法:遛狗
# #
# # a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄
#
# class People:
#     def __init__(self,name,age,dog):
#         self.name =name
#         self.age =age
#         self.dog =dog
#     def walk_dog(self):
#         print("%s遛%s"%(p1.name,dog1.name))
# class  Dog:
#     def __init__(self,name,color,age):
#         self.name =name
#         self.color =color
#         self.age =age
#     def call1(self):
#         print("叫唤")
#
# dog1 =Dog("大黄","黄色",3)
# p1 =People("小明",18,dog1)
# p1.walk_dog()

# 3.声明一个圆类:

# class Round:
#     π=3.14
#     def __init__(self,r):
#         self.r =r
#     def area(self):
#         return Round.π*(self.r**2)
#     def perimeter(self):
#         return Round.π*self.r*2
# r1 =Round(3)
# print(r1.area())
# 4.创建一个学生类:
#
# 属性:姓名，年龄，学号
#
# 方法:答到，展示学生信息
#
# 创建一个班级类:
#
# 属性:学生，班级名
#
# 方法:添加学生，删除学生，点名, 求班上学生的平均年龄
# import json
# import Filemanager1
# class Student:
#     def __init__(self,name,age,id):
#         self.name =name
#         self.age = age
#         self.id =id
#
#     def  answe_to(self):
#         print("%s到！"%self.name)
#
#     def student_information(self):
#         dict_information =self.__dict__
#         for i in  dict_information:
#             print(i,":",dict_information[i],end="  ")
#         print()
#         return dict_information
# class  Class:
#     class_name = "python1808"
#     def __init__(self,student):
#         self.information =student
#     #添加学生
#     def add_student(self): #self =c1
#         if  not Filemanager1.read_json_file("./files/python1808.json"):
#             add_student1=[]
#             add_student1.append(self.information) #student
#             Filemanager1.write_json_file("./files/python1808.json",add_student1)
#         else:
#             count = Filemanager1.read_json_file("./files/python1808.json")
#             count.append(self.information)
#             Filemanager1.write_json_file("./files/python1808.json", count)
#         print("添加成功！")
#
# # s1 =Student("ly","18","15454")
# # countent =Student.student_information(s1)
# # c1 =Class(countent)
# # c1.add_student()
#     #删除学生
#     def del_student(self):
#         Filemanager1.read_json_file("./files/python1808.json")
#         if self.information not in Filemanager1.read_json_file("./files/python1808.json"):
#             print("删除失败，查无此人")
#         else:
#             count1 =Filemanager1.read_json_file("./files/python1808.json")
#             count1.remove(self.information)
#             Filemanager1.write_json_file("./files/python1808.json",count1)
#             print("删除成功！")
# # s1 =Student("ly","18","15454")
# # countent =Student.student_information(s1)
# # c1 =Class(countent)
# #  c1.del_student()
#     #点名
#     def call_name(self):
#         Filemanager1.read_json_file("./files/python1808.json")
#         for i in Filemanager1.read_json_file("./files/python1808.json"):
#             if self.information["name"]==i["name"]:
#                 Student.answe_to(self.information["name"])
#             else:
#                 continue
#         else:
#             print("查无此人")
# s1 =Student("ly","18","15454")
# countent =Student.student_information(s1)
# c1 =Class(countent)
# c1.call_name()
#  4.创建一个学生类:
#
# 属性:姓名，年龄，学号
#
# 方法:答到，展示学生信息
#
# 创建一个班级类:
#
# 属性:学生，班级名
#
# 方法:添加学生，删除学生，点名, 求班上学生的平均年龄

class Student:
    def __init__(self,name,age,id):
        self.name =name
        self.age = age
        self.id =id

    def  answe_to(self):
        print("%s：到！"%self.name)

    def student_information(self):
        print("姓名：%s 年龄：%d 学号：stu_%d"%(self.name,self.age,self.id))
class  Class:
    def __init__(self,class_name):
        self.students =[] #一个Class类的对象属性
        self.name =class_name #一个Class类的对象属性
    #添加
    def add_student(self,students):
        self.students.append(students)
    #删除
    def del_student(self,students):
        self.students.remove(students)
    #点名
    def  call_name(self,student1):
        for index in range(len(self.students)):
            if student1 in self.students:
                print(student1.name)
                student1.answe_to()
                break
        else:
            print(student1.name)
            print("%s：上网去了！"%student1.name)
    #求平均年龄
    def average_scores(self):
        sum =0
        for i in self.students:
            dict1 =i.__dict__
            age1 =int(dict1["age"])
            sum+=age1
        print("%s平均年龄为%.2f"%(self.name,sum/len(self.students)))
#声明Student类的对象
s1 =Student("小明","18","17")
s2 =Student("小花","19","27")
s3 =Student("小猪","20","37")
#声明一个Class的对象
c1 =Class("python1808")
#添加
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
#删除
c1.del_student(s1)
#点名
c1.call_name(s2)
c1.call_name(s3)
c1.call_name(s1)

#求平均年龄
c1.average_scores()
