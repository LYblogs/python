"""__author__ = 余婷"""
# ===============1.数据结构的设置==============
"""
数据关系： 一个学生管理系统可以保存多个学生信息。一个学生保存姓名、年龄、电话、学号等信息。

一个学生管理系统对应的数据模型： 一个列表
一个学生对应的数据模型: 一个字典

整个数据结构: 
student_system= 
[ 
    {'name':x, 'age':x, 'tel':x, 'id':x},
    {'name':x, 'age':x, 'tel':x, 'id':x},
    {'name':x, 'age':x, 'tel':x, 'id':x},
    {'name':x, 'age':x, 'tel':x, 'id':x},
    {'name':x, 'age':x, 'tel':x, 'id':x},
    {'name':x, 'age':x, 'tel':x, 'id':x},
    ...
    {'name':'张三', 'age':18, 'tel':'2333', id:'0010'}
]
"""


# ===============2.页面设计和控制==============
page = """============================
  🌺🌺欢迎来到XX学生管理系统🌺🌺
  ♥ 1.添加学生
  ♥ 2.查找学生信息
  ♥ 3.删除学生
  ♥ 4.修改学生信息
  ♥ 5.退出
============================"""
while True:
    # 1.显示主页面
    print(page)
    # 2.给出选择
    value = input('请选择(1-5):')
    # 3.根据不同的选择做不一样的反应
    if value == '1':
        # ====添加学生=====
        while True:
            name = input('请输入姓名:')
            age = input('请输入年龄:')
            tel = input('请输入电话号码:')
            print('添加成功！')
            print('1.继续\n2.返回')
            value1 = input('请选择(1-2):')
            if value1 == '1':
                continue
            else:
                break

    elif value == '2':
        print('查找学生信息的功能')
    elif value == '3':
        print('删除学生的功能')
    elif value == '4':
        print('修改学生信息')
    else:
        print('退出成功！')
        break
