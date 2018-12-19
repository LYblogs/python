import Filemanager
import deng_lu
user_name = ""
def creat_id():
    id =1
    while True:
        yield id
        id+=1
def add_student():
    while True:
        student_name = input("请输入学生名字：")
        student_age = int(input("请输入学生年龄："))
        student_tel = int(input("请输入学生电话："))
        re =creat_id()
        student_id ="stu_%.3d"%next(re)
        dict1={"id":student_id,"name":student_name,"age":student_age,"tel":student_tel}
        if not Filemanager.read_json_file("file/"+user_name+".json"):
            add_student1 =[]
            add_student1.append(dict1)
            Filemanager.write_json_file("file/"+user_name+".json",add_student1)
            print("添加成功！")
        else:
            count1=Filemanager.read_json_file("file/"+user_name+".json")
            count1.append(dict1)
            Filemanager.write_json_file("file/" + user_name + ".json", count1)
            print("添加成功！")
        num2 = input("""❀1.继续添加
❀2.退出
请选择（1-2）：""")
        if num2=='1':
            continue
        else:
            break




def show_manage_page():
    while True:
        print('==========学生管理页面==========')
        print("""🌺🌺欢迎%s 
❀ 1.添加学生
❀ 2.查看学生
❀ 3.修改学生信息
❀ 4.删除学生
❀ 5.退出
=========================="""% user_name)
        num1 =int(input("请选择（1-5）"))
        if num1 == 1:
            add_student()
        elif num1==2:
            1
