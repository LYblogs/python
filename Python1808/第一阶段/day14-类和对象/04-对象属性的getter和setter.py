"""
1.getter和setter
如果希望在获取对象属性之前要做点别的事情，就给这个属性添加getter；
如果希望在给对象属性赋值之前做点别的事情，就给这个属性添加setter

2.添加getter
a.属性在命名的时候，属性名前加_（保护的） 例如：self._age =0
b.声明一个函数，函数的名字是属性名(不要下划线)，不需要额外的参数，有返回值；
并且函数前使用@property修饰，这个函数的返回值就是获取属性的结果
例如：
@property
def age(self):
    return 年龄相关值

c.当需要获取属性的时候，通过对象.一个不带下划线的属性 例如：对象.age

3.给对象属性添加setter
想要给对象属性添加setter，必须先给它添加getter
a.属性在命名的时候，属性名前加_（保护的）
b.声明一个函数，函数的名字是属性名(不要下划线)，需要一个额外的参数，不用返回值；并且函数前
使用@getter名.setter修饰
列如：
@age.setter
def age(self,value):
    self._age =value
c.当需要给属性赋值的时候，通过对象.一个不带下划线的属性  列如：对象.age =100
"""
class Person:
    def __init__(self,name ="小红"):
        self.name =name
        self._age =0
        self.sex ="男"
    #这儿的age函数就是属性_age的getter方法
    @property
    def age(self):
        if self._age<1:
            return "婴儿"
        elif self._age<10:
            return "小孩"
        elif self._age<30:
            return "青年"
        elif self._age<=100:
            return "老年"
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            print("年龄是整数")
            raise ValueError
        if not 0<=value<=100:
            print("超出范围!!")
            raise ValueError
        self._age =value
p1 =Person()
#这儿实质是在调用_age的getter方法
print(p1.age)
# print(p1.age) #希望取到的不是年龄值，而是年龄对应的阶段
# p1.age =-12 #存0
# p1.age =200 #存150
#这儿实质是在调用_age的setter方法
p1.age =98
print(p1.age)
#练习：声明一个时间类，属性：以秒的形式保存时间
#不断的输入时间：以"xx:xx"形式输入。输入多少个时间，就保存多少个时间对象。
#直到输入end为止


class Time:
    def __init__(self):
        self._second = 0
    @property
    def second(self):
        return self._second
    @second.setter
    def second(self,value:str):
        times=value.split(":")
        self._second =int(times[0])*60+int(times[1])
while True:
    value =input("时间:")
    if value =="end":
        break
    t =Time()
    t.second =value
    print(t.second)
"""
补充：打印自己声明的类的对象的时候，默认打印的是：<模块名.类名 object at 对象地址（id）>
    如果不希望以默认的方式去打印对象，可以实现__repr__魔法方法。
    打印对象的时候就会打印这个方法的返回值
    def __repr__(self):
        return"aaa"
    
"""
class Student:
    def __init__(self,name,age):
        self.name =name
        self.age =age
    def __repr__(self):
        return "name:%s,age:%d"%(self.name,self.age)
        # return "<<"+self.__class__.__module__+"."+\
        # self.__class__.__name__+"object at "+hex(id(self))+">>"

stu1 =Student("小明",29)
stu2 =Student("小花",21)
print(stu1)
