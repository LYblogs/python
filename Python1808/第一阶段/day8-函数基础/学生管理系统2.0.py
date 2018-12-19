page = """
=================================
❀❀❀欢迎liyi：

    ❀ 1.添加学生
    ❀ 2.查看学生
    ❀ 3.修改学生信息
    ❀ 4.删除学生
    ❀ 5.退出
=================================
"""
di_1="""===========================================
添加成功！
❀ 1.继续添加
❀ 2.返回上一层
==========================================="""
di_2 ="""❀1.查看所有学生
❀ 2.按姓名查找
❀ 3.按学号查找
❀ 4.返回上一层"""
di_3="""❀ 1.修改学生姓名
❀ 2.修改学生年龄
❀ 3.修改学生电话
❀ 4.返回
"""
deng1_lu = """
=================================

        ❤ 1.登录
        ❤ 2.注册
        ❤ 3.退出

=================================         
"""


def zhu_ce(*args):
    with open("files/sys_注册.txt", "a", encoding="utf-8") as fe:
        count = fe.write(str(args[0]) + "/" + str(args[1] + "\n"))


def deng_lu():
    with open("files/sys_注册.txt", "r", encoding="utf-8") as fe:
        while True:
            count = fe.readline()
            list1 = count.split("/")
            if list1[0] == deng_zhanghao and list1[1] == deng_mima:
                _ = input("登录成功！按任意键继续！")
                break
            elif list1[0] == deng_zhanghao and list1[1] != deng_mima:
                print("密码错误")
                _ = input("按任意键继续！")
                break
            elif count == "":
                print("查无此人")
                _ = input("按任意键继续！")
                break

student_system=[]


def creat_id():
    """
    学号生成
    :return:
    """
    num = 1
    while True:
        yield num
        num += 1
re = creat_id()
def nuw_studen(**kwargs):

    """
    添加学生信息
    :return:
    """
    kwargs["学号"] = "stu_00" + str(next(re))
    return kwargs
def view_student():
    """
    查看所有学生
    :return:
    """
    for i in range(len(student_system)):
        print("学号", ":",student_system[i]["学号"], end=" ")
        print("姓名", ":",student_system[i]["name"], end=" ")
        print("年龄", ":",student_system[i]["age"], end=" ")
        print("电话", ":",student_system[i]["tel"])

def name_student():
    """
    按照学生名字查找信息
    :return:
    """
    index = 0
    for i in range(len(student_system)):
        if student_system[i]["name"] == name_:
            print(index,"        ",end="")
            print("学号", ":",student_system[i]["学号"], end=" ")
            print("姓名", ":",student_system[i]["name"], end=" ")
            print("年龄", ":",student_system[i]["age"], end=" ")
            print("电话", ":",student_system[i]["tel"])
            index+=1
def student1_id():
    """
    按学号查找学生信息
    :return:
    """
    for i in range(len(student_system)):
        if student_system[i]["学号"] == student_id:
            print("学号", ":",student_system[i]["学号"], end=" ")
            print("姓名", ":",student_system[i]["name"], end=" ")
            print("年龄", ":",student_system[i]["age"], end=" ")
            print("电话", ":",student_system[i]["tel"])

def  exc_name(id:str,new_name:str):
    """
    修改学生姓名
    :return:
    """
    for i in student_system:
        if i["学号"] ==id:
            i["name"]=new_name
def  exc_age(id:str,new_age:int):
    """
    修改学生年龄
    :param id:
    :param new_age:
    :return:
    """
    for i in student_system:
        if i["学号"] ==id:
            i["age"]=new_age
def  exc_tel(id:str,new_tel:int):
    """
    修改学生电话
    :param id:
    :param new_age:
    :return:
    """
    for i in student_system:
        if i["学号"] ==id:
            i["tel"]=new_tel
def del_student22():
    i=0
    if del_student != del_student1:
        print("两次学号输入不一致")
    else:
        for i in student_system:
            if i["学号"] == del_student:
                student_system.remove(i)
                i+=1
        if i ==1:
            print("删除成功！")
        else:
            print("查无此人")
#声明变量
while True:
    print(deng1_lu)
    sys1_num = int(input("请选择（1-3）："))
    while sys1_num != 3:
        if sys1_num == 2:
            zhu_zhanghao = input("请输入账号：")
            zhu_mima = input("请输入密码：")
            zhu_ce(zhu_zhanghao, zhu_mima)
            _ = input("注册成功！按任意键继续！")
            break
        elif sys1_num == 1:
            deng_zhanghao = input("请输入账号：")
            deng_mima = input("请输入密码：") + "\n"
            deng_lu()
            break
    print(page)
    #打印主界面
    num1 = int(input("请选择（1-5）："))
    while num1!=5:
        if num1 == 1:
            student_system.append(nuw_studen(name=input("请输入姓名:"),age=input("请输入年龄:"),tel=int(input("请输入电话:"))))
            print(di_1)
            num2 =int(input("请选择1-2："))
            while num2!=2:
                if num2 ==1:
                    student_system.append(
                        nuw_studen(name=input("请输入姓名:"), age=input("请输入年龄:"), tel=int(input("请输入电话:"))))
                    print(di_1)
                    num2 = int(input("请选择1-2："))
                else:
                    print("请输入正确数字1-2：")
            else:
                print(page)
                pass
                break
        elif  num1 ==2:
            print(di_2)
            num2 =int(input("请选择1-4:"))
            while num2 !=4:
                if num2 ==1:
                    view_student()
                elif num2 ==2:
                    name_ =input("请输入学生名字:")
                    name_student()
                elif  num2 ==3:
                    student_id = input("请输入学号（格式：stu_xxx）：")
                    student1_id()
                else:
                    print("请正确输入:")
                _ = input("按回车键继续")
                print(di_2)
                num2 = int(input("请选择1-4:"))
            else:
                print(page)
                break
        elif num1 == 3:
            print(di_3)
            num3 = int(input("请选择1-4："))
            while num3!=4:
                if num3 ==1:
                    exc_name(id=input("请输入学号（格式stu_xxx）:"),new_name=input("请输入正确的名字:"))
                    print("修改成功!")
                elif num3==2:
                    exc_age(id=input("请输入学号（格式stu_xxx）:"), new_age=int(input("请输入正确的年龄:")))
                    print("修改成功!")
                elif num3 == 3:
                    exc_tel(id=input("请输入学号（格式stu_xxx）:"), new_tel=int(input("请输入正确的电话:")))
                    print("修改成功!")
                else:
                    print("请正确输入：")
                _ = input("请按回车键继续")
                num3 = int(input("请选择1-4："))
            else:
                print(page)
                break
        elif num1 ==4:
            print("""❀1.删除学生
❀2.返回上一层""")
            num4=int(input("请选择1-2:"))
            while num4!=2:
                if num4 ==1:
                    del_student =input("请输入学生学号：")
                    del_student1 =input("请再次输入学生学号：")
                    del_student22()
                else:
                    print("请正确输入：")
                _ = input("请按回车键继续")
                print("""❀1.删除学生
❀2.返回上一层""")
                num4 = int(input("请选择1-2："))
            else:
                print(page)
                break

        else:
            print("请输入正确指令")
            print(page)
        continue
    else:
        print("系统结束！")
        break