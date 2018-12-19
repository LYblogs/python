# 1.类的字段
"""
a.直接声明在类里面，并且是在函数外面的变量，就是类的字段
b.类的字段需要通过类来使用 类.字段 - 不管在类里面还是类外面都一样

不会因为对象不同而不一样的数据，就声明成类的字段
"""
class Person:
    #声明一个类的字段
    number =61
    def show_number(self):
        print("人的数量%s"%Person.number)


Person.number =20
print(Person.number)

# 2.内置类属性
"""
内置属性就是声明类的时候，类中已经声明好的属性（类的字段和对象的属性）
"""
class Dog:
    """说明文档：狗类"""
    #类的字段
    type ="犬科"
    #对象属性
    def __init__(self,name ="",age=0,color=""):
        self.name =name
        self.age =age
        self.color =color
    #对象方法
    def eat(self,food):
        print("%s在吃%s"%(self.name,food))
    #类方法
    @classmethod
    def  shout(cls):
        print("汪汪汪")
    #静态方法
    @staticmethod
    def bite():
        print("狗咬人！")

dog1 =Dog("小黑",10,"黄色")
# a.__name__
"""
类.__name__ - 获取类的名字（字符串）

"""
print(Person.__name__,type(Person.__name__)) #Person <class 'str'>

# b.__class__
"""
对象.__class__ -获取对象对应的类(结果是一个类，原来类能做的事情它都能做)

"""
a =dog1.__class__
print(a.__name__) #Dog <class"str">
print(Dog.type)#犬科
print(a.type) #犬科


#c.__dict__ (返回的是字典)
"""
类.__dict__ -  获取当前类的所有的类的字段及其对应的值
(重点)对象.__dict__ - 将当前对象所有的属性及其值转换成字典，key是属性名，value是属性的值 

"""
print(dog1.__dict__)
#d.__base__（返回的是元组，元素就是父类）
"""
类.__basa__ 获取当前类的父类

"""
print(Dog.__bases__) #(<class 'object'>,)

#e.__module__
"""
类.__module__ - 获取当前类所在的模块的模块名

"""
print(Dog.__module__)  #__main__

#f.__doc__
"""
类.__doc__ - 获取类的说明文档

"""
print(Dog.__doc__) #说明文档：狗类
