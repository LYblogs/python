"""
1.什么是json数据
json数据就是一种数据格式，瞒住json格式的数据就是json数据。
文件中的后缀是.json，并且文件中的内容满足json格式

2.json格式
一个json中只有一个数据；并且这个数据是json支持的数据类型的数据

json支持的数据类型
数字类型 - 包含所有的数字，包括整数和浮点数，例如：100,12.5，-20.5

字符串 - 使用双引号括起来的字符集，例如："123","abc123","%$@*"

布尔 - true 和false

数组 - 相当于python中的列表，使用[]括起来，括号里面是任意json支持的数据类型
列如：["abc",true,"@@#!%%&&",100]

字典 -相当于python中的字典，使用{}括起来，括号里面是键值对；
键一般是字符串，值是json支持的任意类型的数据

特殊值 - null（相当于None），表示空

3.python有个内置的模块用来支持对json数据的处理：json
"""
import json

"""
a.将json数据转换成python数据
b.将python数据转换成json数据

"""

# 1.将json数据转换成python数据怎么转换
"""
loads(字符串) - 将json格式的数据转换成python对应的数据
字符串里面的内容必须满足json数据

json        python
数字   --   整型/浮点型
字符串 --   字符串（双引号会变成单引号）
布尔   --   布尔（true-->True , false-->False）
数组   --   列表
字典   --   字典
null   --  None
"""
#字符串
py = json.loads('"abc"')
print(py,type(py)) # 'abc' #<class 'str'>

# 数字
py1 = json.loads('100.12')
print(py1,type(py1)) #100.12  #<class 'float'>

# 布尔
py2 = json.loads('false')
print(py2) #False

#数组
py3 = json.loads('["abc",100,true]')
print(py3) #['abc', 100, True]

with open("data.json","r",encoding="utf-8")as f:
    count = f.read()
data_dict = json.loads(count)
# print(data_dict['data'][2]["age"])

#2.将python数据转换成json数据
"""
json.dumps(数据) - 将python数据转换成内容符合json格式的字符串
注意：结果都是字符串

python          json
int/flota       数字
字符串          字符串（单引号会变成双引号）
布尔            布尔（True - true ， False - false）
列表/元组        数组
"""
# a.数字
js1 = json.dumps(100)
print(js1,type(js1)) #100 <class 'str'>

# b.字符串
js2 = json.dumps("hello,world")
print(js2,type(js2)) #"hello,world"  <class 'str'>

# c.布尔
js3 = json.dumps(True)
print(js3,type(js3)) #true <class 'str'>

# d.列表、元组
js4 = json.dumps((10,'abc',True))
print(js4,type(js4)) #[10, "abc", true] <class 'str'>
js5 = json.dumps([10,'abc',True])
print(js5,type(js5)) #[10, "abc", true] <class 'str'>

# e.字典
js6=json.dumps({"a":10,"b":20,"c":30})
print(js6,type(js6)) #{"a": 10, "b": 20, "c": 30} <class 'str'>

# 3.json文件操作相关方法
"""
load（文件对象） - 将文件对象的数据读出来，并且转换成python对应的数据
                    （文件对象中的内容必须是json格式的数据）
dump（数据，文件对象） - 将python数据转换成json格式的字符串，再写入文件对象中
"""

#练习：通过添加多个学生信息（姓名、年龄、和电话），
# 添加完成后，最后将数据保存在josn文件中，
# 并且上次添加的信息不回删除，下次添加的时候是在上次的基础上添加的。
while True:
    with open("data.json","r",encoding="utf-8")as ff:
        countent =ff.read()
        list1 = json.loads(countent)
        name = input("请输入姓名：")
        age =int(input("请输入年龄："))
        tel = int(input("请输入电话："))
        dict1 ={"name":name,"age":age,"tel":tel}
        list1.append(dict1)
    with open("data.json","w",encoding="utf-8")as f:
        list2=json.dumps(list1)
        f.write(list2)
    num1 = input("是否继续Y/N：")
    if num1 =="Y":
        continue
    else:
        break

# while True:
#     name = input("请输入姓名：")
#     age =int(input("请输入年龄："))
#     tel = int(input("请输入电话："))
#     list1.append({"name":name,"age":age,"tel":tel})
#     js6 =json.dumps(list1)
#     with open("data.json","a",encoding="utf-8") as ff:
#         countent = ff.write(js6)
#     num1 = input("是否继续Y/N：")
#     if num1 =="Y":
#         continue
#     else:
#         break
