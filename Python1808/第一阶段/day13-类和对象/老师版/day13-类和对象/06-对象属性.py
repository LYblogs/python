"""__author__ = 余婷"""

"""
1.什么是对象属性
a.声明在__init__方法中
b.self.属性名 = 值
c.通过对象使用: 对象.属性

语法：
self.变量名 = 值   

说明:变量名就是属性名, 这个变量就是对象属性


2.什么样的属性应该声明称对象属性
如果属性的值会因为对象不同而不一样，那这样的属性就应该声明成对象属性。反之就声明称类的字段
"""


# 情况一：所有对象属性创建的时候都使用一个固定的默认值
class Person:
    def __init__(self):
        # 这儿的name和age就是Person类的对象属性
        self.name = '张三'
        self.age = 0


# 创建对象
p1 = Person()

# 使用对象属性
print(p1.name)
p1.name = '李四'
print(p1.name)

p2 = Person()
p2.name = '小红'
print(p2.name, p1.name)


# 情况二：创建对象的时候，决定对象属性的值
class Person:
    def __init__(self, name1, age=1):
        self.name = name1
        self.age = age


p11 = Person('小红')
p12 = Person('小花', 0)
print(p11.age, p12.age)  # 1 0
print(p11.name, p12.name)  # 小红  小花

# 修改对象属性的值
p11.name = '老王'
print(p11.name)


# 练习：声明一个矩形类
"""
属性: 长和宽
方法: 求面积和求周长
"""


class Rect:
    def __init__(self, length1, width1):
        self.length = length1
        self.width = width1

    # 一个对象方法需不需要除了self以外的其他参数，
    # 看实现这个函数的功能需不需要除了属性以外的其他数据
    def area(self):
        # self = r1
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width)*2


r1 = Rect(10, 20)
print(r1.area())

r2 = Rect(3, 4)
print(r2.area())


# 练习：声明一个Point类，拥有属性x坐标和y坐标。功能：求两个点之间的距离
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 求当前点到另外一个点的距离
    def distance(self, other):
        """
        求两个点的距离
        :param other: Point对象
        :return: 距离
        """
        # self = p1  other = p2
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5


# 创建点p1
p1 = Point(0, 0)
print(p1.x, p1.y)
# 创建点p2
p2 = Point(3, 4)

# 求p1到p2的距离
print(p1.distance(p2))
