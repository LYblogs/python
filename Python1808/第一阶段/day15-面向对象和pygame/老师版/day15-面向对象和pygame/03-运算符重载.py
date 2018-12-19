"""__author__ = 余婷"""

"""
1.别的语言的函数和函数的重载
C++/java声明函数的语法:
返回值类型 函数名(参数类型1 参数名1, 参数类型2 参数名2){
    函数体
}

int func1(){
    
}
void func1(int a){

}

void func1(char a){

}
int func1(int a, int b){

    
}

上面这4个函数是不同的函数(可以同时存在)


python中的函数不支持重载
def func1():
    pass
    
def func1(a):
    pass
    
def func1(a, b)
    pass
    
最终只保留最后这一个func1,前面的会被覆盖


2.运算符重载
python中使用运算的时候，实质是在调用相应的魔法方法。（python中每个运算符都对应一个魔法方法）
运算符重载:在不同的类中实现同一个运算符对应的魔法方法，来让类的对象支持相应的运算
"""


class Student(object):
    def __init__(self, name='', score=0, age=0):
        self.name = name
        self.score = score
        self.age = age

    #  + 重载
    """
    数据1 + 数据2 -- 数据1会传给self， 数据2会传给other
    """
    def __add__(self, other):
        # self + other
        return self.score + other.score

    # - 运算
    def __sub__(self, other):
        # self - other
        return self.age - other.age

    # 注意：>和<一般情况下只需要重载一个，另外一个自动支持
    # < 运算
    def __lt__(self, other):
        return self.score < other.score

    #  > 运算
    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return '<'+(str(self.__dict__)[1:-1])+'>'


stu1 = Student('小花', 90, 16)
stu2 = Student('小明', 80, 18)
stu3 = Student('小红', 87, 23)
stu4 = Student('小🐶', 30, 15)
print(stu1 + stu2)

print(stu1 - stu2)

all_students = [stu1, stu2, stu3, stu4]
all_students.sort()


print(all_students)

print(max(all_students))



