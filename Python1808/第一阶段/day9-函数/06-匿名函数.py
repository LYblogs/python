"""
匿名函数还是函数，除了声明的语法以外，函数其他的语法匿名函数都支持
1.匿名函数的声明
a.语法
函数名 = lambda 参数列表：返回值
b.说明：
函数名 - 变量名
lambda - 关键字
参数列表 -和普通函数的参数列表的作用和要求一样
返回值 - 相当于普通函数return关键字后面的表达式

注意：匿名函数中 ： 后面的语句属于函数体
"""
#用匿名函数求两个数的和
def my_num(num1,num2):
    return num1+num2

my_sum1 = lambda num1,num2:num1+num2

print(my_sum1(10,20))

#练习：写一个匿名函数，功能是求两个数的最大值
my_max = lambda  num1,num2:max(num1,num2)

#补充：python中三目运算符
"""
C中的三目运算符：条件语句？值1：值2 - 条件语句为True，整个表达式的结果是值1，否则是值2

int x =10，y =20；
max =x>y?x:y;

b.python中的三目运算符：值1 if 条件语句 else 值2 -条件语句为True，整个表达式的结果是值1，否则是值2
"""
x = 10
y = 20
print(x if x>y else y)

# 练习：写一个匿名函数，获取字典中指定的key对应的值
my_values = lambda dict,key:dict[key]
print(my_values({"a":100,"b":200},"a"))