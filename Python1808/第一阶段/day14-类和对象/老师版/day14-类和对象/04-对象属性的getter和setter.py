"""__author__ = 余婷"""
"""
1.getter和setter
如果希望在获取对象属性之前要做点儿别的事情，就给这个属性添加getter；
如果希望在给对象属性赋值之前做点儿别的事情，就给这个属性添加setter

2.给对象属性添加getter
a.属性命名的时候，属性名前加_; 例如：self._age = 0
b.声明一个函数，函数的名字是属性名(不要下划线),不需要额外参数,有返回值；并且函数前使用@property修饰。
  这个函数的返回值就是获取属性的结果
例如：
@property
def age(self):
    return  年龄相关值
  
c.当需要获取属性的时候通过对象.不带下划线的属性；例如：对象.age


3.给对象属性添加setter
想要给对象属性添加setter，必须先给它添加getter
a.属性命名的时候，属性名前加_; 例如：self._age = 0
b.声明一个函数，函数的名字是属性名(不要下划线)，需要一个额外的参数,不用返回值;
  并且函数前使用@getter名.setter修饰
例如:
@age.setter
def age(self, value):
    self._age = value
    
c.当需要给属性赋值的时候，通过对象.不带下划线的属性来赋值；例如: 对象.age = 100

"""


class Person:
    def __init__(self, name='小红'):
        self.name = name
        self._age = 60
        self.sex = '男'

    # 这儿的age函数就是属性_age的getter方法
    @property
    def age(self):
        if self._age < 1:
            return '婴儿'
        elif self._age < 18:
            return '未成年'
        elif self._age < 50:
            return '中年'
        else:
            return '老年'

    # 这儿的age函数就是属性_age的setter
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print('年龄必须是整数!!!!')
            raise ValueError

        if not (0 <= value <= 100):
            print('年龄超出范围!!!!')
            raise ValueError

        self._age = value


p1 = Person()
# print(p1.age)  # 希望取到的不是年龄值，而是年龄对应的阶段
# p1.age = '12'    # 存 0
# p1.age = '100'   # 150

# 这儿实质是在调用_age的getter方法
print(p1.age)

# 这儿实质是在调用_age的setter方法: p1.age(80)
p1.age = 80


# 练习：声明一个时间类，有一个属性是以秒的形式保存时间
# 不断的输入时间，以'XX:XX'的形式输入。输入多少个时间就保存多少个时间对象。知道输入end为止

class Time:
    def __init__(self):
        self._second= 0

    @property
    def second(self):
        return self._second

    # '01:11 - 71'
    @second.setter
    def second(self, value: str):
        times = value.split(':')
        self._second = int(times[0])*60 + int(times[1])

    """
    补充：打印自己声明的类的对象的时候，默认打印的是：<模块名.类名 object at 对象地址>
    如果不希望以默认的方式去打印对象，可以实现__repr__魔法方法。打印对象的时候就会打印这个方法的返回值
    
    这个函数的返回值必须是字符串
    """
    def __repr__(self):
        return '时间:'+ str(self.second)


"""
10:20   -> time.秒 = 620
1:20   ->  time.秒 = 80
"""
# times = []
# while True:
#     value = input('时间:')
#     if value == 'end':
#         break
#     # 创建对象，并且将输入的内容赋给时间
#     t = Time()
#     t.second = value
#     times.append(t)
#
# print(times)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __repr__(self):
    #     return '[' + self.__class__.__module__+'.'+\
    #            self.__class__.__name__+' object at '+ hex(id(self))+']'
    def __repr__(self):
        # return 'name:%s, age:%d' % (self.name, self.age)
        return str(self.__dict__)[1:-1]


stu1 = Student('小明', 29)   # >>__main__.Student object at 0x1077a9550<<
stu2 = Student('小🌺', 18)   # name:小🌺, age:18
print(stu1, stu2)




