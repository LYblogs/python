"""
1.添加类的字段
直接在子类中添加新的字段

2.添加对象属性
继承对象属性是通过基础父类的init方法继承下来
如果想要在保留父类继承下来的对象属性的前提下，添加新的对象属性，
需要在子类的init方法中，通过super()去调用父类的init方法
"""

class Person:
    num =61
    def __init__(self,name):
        self.name =name
        self.age =0

class Student(Person):
    number =60
    def __init__(self,name):
        super().__init__(name)
        self.study_id ="vvv"
print(Student.number,Student.num)
stu1 =Student("张三")
print(stu1.name,stu1.age,stu1.study_id)

#练习：声明一个动物类，有属性：年龄，颜色，类型。
# 要求创建动物对象的时候类型和颜色必须赋值，年龄可以赋值也可以不赋值
# 声明一个猫类，有属性：年龄、颜色、类型，爱好
# 要求创建猫对象的时候，颜色必须赋值，年龄和爱好可以赋值，也可以不赋值，类型不能赋值。
class Animal:
    def __init__(self,color,type,age=5):
        self.age =age
        self.color =color
        self.type =type

class  Cat(Animal):
    def __init__(self,color,age=0,hobby ="call"):
        super().__init__("猫科",color,age)
        self.hobby =hobby

a1 =Animal("犬科","黄色",10)
c1 =Cat("黄色")
c2 =Cat("白色",10,"aaa")