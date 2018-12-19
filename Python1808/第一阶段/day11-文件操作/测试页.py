# # def zhu_ce(*args):
# #     with open("files/sys_注册.txt","a",encoding="utf-8") as fe:
# #         count = fe.write(str(args[0])+"/"+str(args[1]+"\n"))
# # zhu_zhanghao =input("请输入账号：")
# # zhu_mima =input("请输入密码：")
# # zhu_ce(zhu_zhanghao,zhu_mima)
# zhu_zhanghao = input("请输入账号：")
# zhu_mima = input("请输入密码：")
# def deng_lu():
#     with open("files/sys_注册.txt", "r", encoding="utf-8") as fe:
#         while True:
#             count = fe.readline()
#             list1 = count.split("/")
#             if list1[0] ==zhu_zhanghao and list1[1]==zhu_mima:
#                 print("登录成功")
#                 with open("files/sys_注册.txt", "a", encoding="utf-8") as fe:
#                     pass
#             if list1[0] ==zhu_zhanghao and list[1] !=zhu_mima:
#                 print("密码错误")
#             if count == "":
#                 print("查无此人")
#                 break
# deng_lu()
# str="abc123/123456"
# print(str.split("/"))


deng1_lu = """
=================================
     ❀欢迎来到XX学生管理系统❀

     1. 登             录
     2. 注             册
     3. 退             出
==================================      
"""