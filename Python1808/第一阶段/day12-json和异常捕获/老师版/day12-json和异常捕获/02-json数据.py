"""__author__ = 余婷"""

"""
1.什么是json数据
json是一种数据格式，满足json格式的数据就是json数据。
文件后缀是.json,并且文件中内容满足json格式


2.json格式
一个json中只有一个数据；并且这个数据是json支持的数据类型的数据

json支持的数据类型
数字类型 - 包含所有的数字，包括整数和小数, 例如： 100， 12.5， -20  
字符串 - 使用双引号括起来字符集, 例如: "123", "abc123", "&*ash"
布尔 - true和false
数组 - 相当于python中的列表, 使用中括号括起来，括号里面是json支持的任意类型的数据
       例如：["abc", 100, true], [12, 89, 89, 90]
字典 - 相当于python中的字典, 使用{}括起来，括号里面是键值对。
       键一般是字符串，值是json支持的任意类型的数据
       {"name": "张三", "age": 18}
特殊值 - null(相当于None)， 表示空  


3.python中有一个内置的模块用来支持对json数据的处理: json     
a.将json数据转换成python数据
b.将python数据转换成json数据
"""
import json

# 1.将json数据转换成python数据
"""
loads(字符串) - 将json格式的数据转换python对应的数据
注意：这儿的字符串的内容必须是json格式的数据

json        python
数字         整型/浮点型
字符串       字符串(双引号会变单引号)
布尔         布尔(true -> True, false -> False)
数组         列表
字典         字典
null         None
"""
# a. 数字转int/float
py1 = json.loads('100')
print(py1, type(py1))
py2 = json.loads('100.12')
print(py2, type(py2))

# b. 字符串
py3 = json.loads('"json"')
print(py3, type(py3))

# c. 布尔
py4 = json.loads('true')
print(py4)

# d.列表
py5 = json.loads('[100, "abc", true, null]')
print(py5)

# e.字典
py6 = json.loads('{"a": 1, "b":[1, 2], "c": true}')
print(py6)

# 练习1：
# 读文件中的内容
with open('data.json', encoding='utf-8') as f:
    content = f.read()
# 将读出来的内容转换成python数据
data_dict = json.loads(content)
print(data_dict['data'][2]['age'])

# 2.将python数据转换成json数据
"""
dumps(数据) - 将python数据转换成内容符合json格式的字符串
注意：最终结果是字符串

python       json
int/float    数字
字符串        字符串(单引号会变双引号)
布尔          布尔(True - true, False - false)
列表/元祖      数组
字典          字典
"""
# a. int和float
js1 = json.dumps(100)
print(js1, type(js1))

js1 = json.dumps(100.12)
print(js1, type(js1))

# b.字符串
js2 = json.dumps('hello world')
print(js2)

# c.布尔
js3 = json.dumps(True)
print(js3)

# d.列表、元祖
js4 = json.dumps((10, 'abc', True))
print(js4)
js4 = json.dumps([100, 'aaa', False, None])
print(js4)

# e.字典
js5 = json.dumps({'a': 10, 'b': 'abc', 'c': ['a', 'b']})
print(js5)

# 练习2：添加多个学生信息（姓名，年龄，电话），添加完成后，将数据保存到json文件中
# 并且，上次添加的信息不会删除，下次再添加的时候，是在上次的基础上添加的
"""
姓名:
年龄:
电话:
aaa, 12, 12222
"""
# all_students = []   # 保存所有学生的信息

with open('students.json', encoding='utf-8') as f:
    # 从文件中把数读出来
    content = f.read()
    # 将数据转换成列表
    all_students = json.loads(content)

# while True:
#     name = input('姓名:')
#     age = int(input('年龄:'))
#     tel = input('电话:')
#     # 创建学生对应的字典
#     stu = {'name': name, 'age': age, 'tel': tel}
#     # 保存学生信息
#     all_students.append(stu)
#
#     value = input('是否继续(Y/N):')
#     if value == 'N':
#         break

print(all_students)
# 将数据写入文件中
with open('students.json', 'w', encoding='utf-8') as f:
    content = json.dumps(all_students)
    f.write(content)

#  3.json文件操作相关方法
"""
load(文件对象)  - 将文件对象中的数据读出来，并且转换成python对应的数据
                 (文件对象中的内容必须是json格式的数据)
dump(数据, 文件对象) - 将python数据转换成json格式的字符串，再写入文件对象中
"""
print('================')
with open('test.txt', encoding='utf-8') as f:
    content = json.load(f)
    print(content, type(content), sep='\n')


# with open('new.json', 'w', encoding='utf-8') as f:
#     json.dump([1, 2, 3], f)


def yt_dump(obj, file):
    with open(file, 'w', encoding='utf-8') as f:
        strstr = json.dumps(obj)
        f.write(strstr)


yt_dump(['a', 'b', 'c'], 'new.json')


# 作业： 封装自己的load方法，要求传入文件地址，就将文件对应的数据读出来并且转换成python数据
