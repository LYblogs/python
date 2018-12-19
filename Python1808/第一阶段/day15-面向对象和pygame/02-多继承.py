"""
多继承：让一个类同时继承多个类
两个类的字段都可以继承
两个类的方法都可以继承
但是对象属性只能继承前面的那个类中的对象属性

注意：实际开发，一般不使用多继承

"""
class Animal:
    info1="跑"
    def __init__(self,name="aaa",age=5,color="黑"):
        self.name =name
        self.age =age
        self.color =color
    def show_info(self):
        print("名字：%s   年龄：%d   颜色：%s"%(self.name,self.age,self.color))
class Fly:
    info="fei"
    def __init__(self,distance=0,speed=0):
        self.distance =distance
        self.speed =speed
    @staticmethod
    def show():
        print("会飞")

class Bird(Animal,Fly):
    pass
print(Bird.info,Bird.info1)
b1 =Bird()
print(b1.name)

"""
2.多态
类的特点：封装、继承、多态

封装：可以对多条数据（功能）和多个功能（方法）进行封装
继承：可以让一个类可以拥有另外一个类的属性和方法
多态：有继承就有多态（一个事物的多种形态）
"""