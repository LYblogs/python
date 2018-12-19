print("="*30)
print("❀❀❀欢迎liyi：")
print()
print("      ","❤ 1.添加学生")
print("      ","❤ 2.查看学生")
print("      ","❤ 3.修改学生信息")
print("      ","❤ 4.删除学生")
print("      ","❤ 5.退出")
print("="*30)
#1、显示主界面
list1 =[]
list2 =[]
list3 =[]
list4 = []
index = 0
xuehao = 1
num1 = int(input("请选择（1-5）："))
# 2、 给出选择
while True:
    if num1 == 1:
        name = input("请输入学生姓名：")
        age = int(input("请输入学生年龄："))
        tel = int(input("请输入学生电话:"))
        list1.append(name)
        list2.append(age)
        list3.append(tel)
        list4.append(xuehao)
        xuehao += 1
        print("添加成功")
        print("1.继续")
        print("2.返回")
        num2 = int(input("请选择(1-2):"))
        if num2 ==1:
            continue
        else:
            print("=" * 30)
            print("❀❀❀欢迎liyi：")
            print()
            print("      ", "❤ 1.添加学生")
            print("      ", "❤ 2.查看学生")
            print("      ", "❤ 3.修改学生信息")
            print("      ", "❤ 4.删除学生")
            print("      ", "❤ 5.退出")
            print("=" * 30)
            num1 = int(input("请选择（1-5）："))
    elif num1 ==2:
        print("1.查看所有学生")
        print("2.按姓名查找")
        print("3.按学号查找")
        print("4.返回")
        num3 = int(input("请选择（1-4）："))
        if num3 == 1:
            for i in range(len(list1)):
                print("学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d"%(list4[index],list1[index],list2[index],list3[index]))
                index+=1
                print()
                print()
        elif num3 ==2:
            name1 =input("请输入学生姓名:")
            xiabiao =list1.index(name1)
            print("学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d"%(list4[xiabiao],list1[xiabiao],list2[xiabiao],list3[xiabiao]))

            xh =int(input("请输入学生学号：stu_00"))
            xb = list4.index(xh)
            print("学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d"%(list4[xb],list1[xb],list2[xb],list3[xb]))
        elif num3 == 3:
            print("=" * 30)
            print("❀❀❀欢迎liyi：")
            print()
            print("      ", "❤ 1.添加学生")
            print("      ", "❤ 2.查看学生")
            print("      ", "❤ 3.修改学生信息")
            print("      ", "❤ 4.删除学生")
            print("      ", "❤ 5.退出")
            print("=" * 30)
            num1 = int(input("请选择（1-5）："))
        else:
            print("输入有误")
            num3 = int(input("请重新选择（1-4）："))
    elif num1 ==3:
        print("1.修改学生姓名")
        print("2.修改学生年龄")
        print("3.修改学生电话")
        print("4.返回")
        num4 =int(input("请选择（1-4）："))
        if num4==1:
            xh1 = int(input("请输入学生学号："))
            name3 = input("请输入新学生姓名：")
            xb2 = list4.index(xh1)
            list1[xb2]=name3
            print("修改后的信息为：""学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d"%(list4[xb2],list1[xb2],list2[xb2],list3[xb2]))
        elif num4 ==2:
            xh1 = int(input("请输入学生学号："))
            age1 = int(input("请输入新学生年龄："))
            xb2 = list4.index(xh1)
            list2[xb2] = age1
            print("修改后的信息为：""学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d" % (list4[xb2], list1[xb2], list2[xb2], list3[xb2]))
        elif num4 ==3:
            xh1 = int(input("请输入学生学号："))
            tel1 = int(input("请输入新学生电话："))
            xb2 = list4.index(xh1)
            list3[xb2] = tel1
            print("修改后的信息为：""学号:stu_%.3d  姓名：%s  年龄：%d  电话：%d" % (list4[xb2], list1[xb2], list2[xb2], list3[xb2]))
        elif num4 ==4:
            print("=" * 30)
            print("❀❀❀欢迎liyi：")
            print()
            print("      ", "❤ 1.添加学生")
            print("      ", "❤ 2.查看学生")
            print("      ", "❤ 3.修改学生信息")
            print("      ", "❤ 4.删除学生")
            print("      ", "❤ 5.退出")
            print("=" * 30)
            num1 = int(input("请选择（1-5）："))
        else:
            print("输入有误")
            num4 = int(input("请重新选择（1-4）："))
    elif num1 ==4:
        xh2 = int(input("请输入要删除学生的学号："))
        xb3=list4.index(xh2)
        del list1[xb3]
        del list2[xb3]
        del list3[xb3]
        del list4[xb3]
        print("已经删除学生信息")
        num5 = input("按回车键返回")
        print("=" * 30)
        print("❀❀❀欢迎liyi：")
        print()
        print("      ", "❤ 1.添加学生")
        print("      ", "❤ 2.查看学生")
        print("      ", "❤ 3.修改学生信息")
        print("      ", "❤ 4.删除学生")
        print("      ", "❤ 5.退出")
        print("=" * 30)
        num1 = int(input("请选择（1-5）："))
    elif num1 == 5:
        print("退出成功!")
        break
    else:
        print("输入有误！")
        num1 = int(input("请重新选择（1-5）："))

