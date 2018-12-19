import Filemanager
import student_manager
#注册
def register():
    #输入用户名
    while True:
        user_name = input("请输入用户名(3~6位)：")
        if 3<= len(user_name)<=6:
            break
        else:
            print("输入有误！请重新输入")
    #输入密码
    while True:
        user_mima = input("请输入密码（6~12）位：")
        if 6<=len(user_mima)<=12:
            break
        else:
            print("格式输入不正确，请重新输入！")
    #判断用户名是否重复
    """
    数据结构：用一个字典保存所有的账号和密码；账号作为key，密码作为value
    数据本地化：使用json文件保存字典中的数据(user_info.json)
    """
    countent =Filemanager.read_json_file("file/user_info.json")
    if not countent:
        countent={}
    if user_name in countent:
        print("注册失败！用户已经存在")
        return
    else:
        print("注册成功！")
        countent[user_name]=user_mima
        Filemanager.write_json_file("file/user_info.json",countent)
#登录
def login():
    """
    登录
    :return:
    """
    #输入账号密码
    user_name = input("请输入账号：")
    user_mima = input("请输入密码:")
    #判断是否注册过
    all_user =Filemanager.read_json_file("file/user_info.json")
    if not all_user:
        print("登录失败！账号未注册")
    if user_name in all_user:
        if all_user[user_name] ==user_mima:
            print("登录成功")
            #进入学生管理页面
            student_manager.user_name = user_name
            student_manager.show_manage_page()
        else:
            print("密码错误")
            print(all_user[user_name])
    else:
        print("登录失败！未注册")

def show_main_page():
    """1.显示主页"""
    while True:
        with open("file/main_page.txt",encoding="utf-8")as f:
            content =f.read()
            print(content)
        num1 =int(input("请选择（1-3）："))
        if num1  ==1:
            #登录
            login()
        elif num1 ==2:
            register()
        else:
            break
if __name__ == '__main__':
    # 1.显示主页
    show_main_page()