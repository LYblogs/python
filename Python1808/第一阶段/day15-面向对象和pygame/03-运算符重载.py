"""
python中的函数不支持重载

2.运算符重载
python中使用运算的时候，实质是在调用相应的魔法方法。（python中每个运算符都对应一个魔法方法）
运算符重载：在不同的类中实现同一个运算符对应的魔法方法，来让类的对象支持相应的运算。

"""
class Student(object):
    def __init__(self,name="",score=0,age=0):
        self.name=name
        self.score=score
        self.age=age
    #加法运算符重载
    def __add__(self, other):
        #self+other
        return self.score+other.score
    #小于运算符，大于和小于一般只需要重载一个，另外一个自动支持
    def __lt__(self, other):
        return self.score<other.score
    def __repr__(self):
        return str(self.__dict__)[1:-1]
stu1=Student("小花",90,16)
stu2=Student("小明",80,18)
stu3=Student("小红",80,18)
stu4=Student("小白",80,18)
print(stu1+stu2)

all_students =[stu1,stu2,stu3,stu4]
print(all_students)
print(max(all_students))