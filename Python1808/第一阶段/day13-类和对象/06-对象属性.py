"""
1.什么是对象属性
a.声明在__init__方法中
b.self.属性名 = 值
c.通过对象来使用： 对象.属性
d.不同的对象，对象属性的值可能会不一样


语法：
self.属性名 = 值

说明：
这个属性就是对象属性
"""
#情况一：使用的对象属性创建的时候都使用一个固定的默认值
class Person:
    def __init__(self):
        #这儿的name和age就是Person类的对象属性
        self.name =""
        self.age =10

#创建对象
p1 =Person()
#使用对象属性
p1.name ="滴滴滴"
print(p1.name)
#情况二.

class Person():
    def __init__(self,name):
        self.name =name
        self.age = 10

p2 = Person("曾宇")
p3 =Person("是帅逼")
print(p2.name,p3.name)
#修改对象属性的值
p2.name = "龙少爷"
print(p2.name,p3.name)


"""
2.什么样的属性应该声明成对象属性
如果属性的值会因为对象不同而不一样，这样的属性就一个声明成对象的属性
反之就声明成类的字段。

"""

#练习：声明一个矩形类

class JuXing:
    def __init__(self,long,wide):
        self.chang =long
        self.kuan = wide
    #一个对象方法需不需要除了self以外的其他参数，看实现这个函数的功能
    # 需不需要出了对象属性以外的其他数据
    def area(self):
        #self = p1
        return self.chang*p1.kuan

p1 =JuXing(20,10)
print("面积：",p1.area())

#练习：声明一个point类，拥有属性x坐标和y坐标，拥有的功能是求两点之间的距离
class Point:
    def __init__(self,x,y):
        self.x_coor =x
        self.y_coor =y
    def distance(self,x1,y1):
        return ((self.x_coor-x1)**2+(self.y_coor-y1)**2)**0.5

r1 =Point(10,20)
print("距离：",r1.distance(10,30))

#最佳方法：
class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5

r1 =Point(10,0)
r2 =Point(0,0)
print(r1.distance(r2))
