"""
1.什么是元组
元组就是不可变的列表。（有序，不可变）
有序 - 可以通过下标获取元素
不可变 - 不支持增删改
2.元组的字面量：通过小括号将多个元素括起来，多个元素之间用逗号隔开。

"""
tuple1 = (1,2,3,"ab",True)
print(type(tuple1))
#a.tuple 只有一个元素的元组,小括号后面的元素必须加括号
tuple2 = (10,)
print(type(tuple2))
# b.去掉小括号，元素之间用括号隔开还是表示元组
tuple3 = 1,2,3,"aaa"
print(tuple3,type(tuple3))
#c.获取元组元素
tuple4 = 10,20,30
print(tuple4[0],tuple4[-3])
#可以通过变量个数和元组元素保持一致来获取元组中的每个元素
x,y,z = tuple4
print(x,y,z)
#通过在变量名前加*，获取没有*的变量获取到的元素的剩下部分。以列表形式返回

tuple5 = ("李毅",98,100,90,88,78)
name,*scores = tuple5
print(name,scores)

#（了解）
tuple6 = (1,2,3)
list1 = ["aa","bb","cc"]
print(*list1)

"""
3.获取元组元素： 和列表方法一样

4.相关运算和列表一样

5.元组相关的方法：只有列表中的count 、 index

"""
max()