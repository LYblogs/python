"""__author__ = 余婷"""
import FileMananger
import student_manager

"""
数据结构： 用一个字典保存所有的账号和密码；账号作为key，密码作为value

数据本地化：使用json文件保存字典中数据(user_info.json)
"""


def register():
    """注册"""
    # 1.输入用户名！
    while True:
        user_name = input('请输入用户名(3~6位):')
        if 3 <= len(user_name) <= 6:
            break
        else:
            print('输入有误，请重新输入!')

    # 2.输入密码
    while True:
        password = input('请输入密码(6~12位):')
        if 6 <= len(password) <= 12:
            break
        else:
            print('输入有误，请重新输入!')

    # 3.判断账号是否已经注册过
    all_user_dict = FileMananger.read_json_file('files/user_info.json')
    # 如果文件不存在(之前没有注册过)
    if not all_user_dict:
        all_user_dict = {}

    if user_name in all_user_dict:
        print('注册失败！%s已经被注册！' % user_name)
        return
    else:
        all_user_dict[user_name] = password
        FileMananger.write_json_file('files/user_info.json', all_user_dict)
        print('注册成功！')


def login():
    """登录"""
    # 1.输入账号和密码
    user_name = input('请输入账号:')
    password = input('请输入密码:')

    # 2.判断账号是否注册过
    all_user = FileMananger.read_json_file('files/user_info.json')
    if not all_user:
        print('登录失败!账号没有注册！')
        return

    if user_name in all_user:
        if all_user[user_name] == password:
            print('登录成功!')
            # 进入学生管理页面
            student_manager.user_name = user_name
            student_manager.show_manage_page()
        else:
            print('登录失败！密码错误!')
    else:
        print('登录失败！账号没有注册！')


def show_main_page():
    """显示主页"""
    while True:
        main_page = FileMananger.read_text_file('files/mainpage.txt')
        print(main_page)

        value = input('请选择(1-3):')
        if value == '1':
            # 登录
            login()
        elif value == '2':
            # 注册
            register()
        else:
            break


if __name__ == '__main__':
    # 1.显示主页
    show_main_page()