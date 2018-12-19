deng1_lu ="""
=================================
        
        ❤ 1.登录
        ❤ 2.注册
        ❤ 3.退出
         
=================================         
"""
def zhu_ce(*args):
    with open("files/sys_注册.txt","a",encoding="utf-8") as fe:
        count = fe.write(str(args[0])+"/"+str(args[1]+"\n"))

def deng_lu():
    with open("files/sys_注册.txt", "r", encoding="utf-8") as fe:
        while True:
            count = fe.readline()
            list1 = count.split("/")
            if list1[0] ==deng_zhanghao and list1[1]==deng_mima:
                _ = input("登录成功！按任意键继续！")
                break
            elif list1[0] ==deng_zhanghao and list1[1] !=deng_mima:
                print("密码错误")
                _ = input("按任意键继续！")
                break
            elif count == "":
                print("查无此人")
                _ = input("按任意键继续！")
                break

while True:
    print(deng1_lu)
    sys1_num = int(input("请选择（1-3）："))
    while sys1_num!=3:
        if sys1_num == 2:
            zhu_zhanghao = input("请输入账号：")
            zhu_mima = input("请输入密码：")
            zhu_ce(zhu_zhanghao,zhu_mima)
            _ =input("注册成功！按任意键继续！")
            break
        elif sys1_num == 1:
            deng_zhanghao = input("请输入账号：")
            deng_mima = input("请输入密码：")+"\n"
            deng_lu()
            break

