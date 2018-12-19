class Dog:
    def __init__(self,name,color,type):
        self.name =name
        self.color= color
        self.type = type

dog1 =Dog("旺财","黄色","二哈")

#1.查（获取对象属性的值）
"""
a.对象.属性名 -属性不存在时会报错
b.getattr(对象,属性名,默认值) -给了默认值之后，如果属性不存在的时候会返回默认值

"""
print(dog1.name)
# print(dog1.name1) #AttributeError: 'Dog' object has no attribute 'name1'
print(getattr(dog1,"name"))
# print(getattr(dog1,"nam1",None)) #None

try:
    print(dog1.name1)
except AttributeError:
    print(None) #None

#2.增、改
"""
a.对象.属性 = 值 （属性存在时是修改，属性不存在时是添加）
b.setattr(对象，属性名，值)

"""
class Dog:
    def __init__(self,name,color,type):
        self.name =name
        self.color= color
        self.type = type

dog1 =Dog("旺财","黄色","二哈")
dog1.aaa =20
print(dog1.aaa) #20 添加
dog1.name ="才才"
print(dog1.name) #才才  修改

#3.删
"""
del 对象.属性 - 将指定对象的指定属性删除

delattr(对象，属性名)

"""
# delattr(dog1,"name")
# # del dog1.name
# print(dog1.name) #AttributeError: 'Dog' object has no attribute 'name'

# 注意：对象属性的增删改查，都是针对指定的那一个对象，不会影响其他对象。

# 4.__slots__ 魔法
"""
是用来约束当前这个类有哪些对象属性

"""
class Student:
    #Student类的对象只能有name，id，age属性
    __slots__ =("name","id","age")
    def __init__(self,name,age):
        self.name=name
        self.id ="001"
        self.age=age

stu1 =Student("小明",18)
stu1.name = "小花"