# # str = "-123"
# # print(str[::-1])
#
# class Solution:
#     def reverse( x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         str1=str(x)[::-1]
#         return int(str1)
#     reverse(x=-123)
# print(2**31)

# list1=[1,2,3,4]
# print(list1[0]+list1[1])
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     list1=[]
#     for index in range(len(nums)):
#         for index1 in range(index,len(nums)):
#             if nums[index]+nums[index1] == target and nums[index]!=nums[index1]:
#                 list1.append(index)
#                 list1.append(index1)
#     return list1
#
# print(twoSum([1,4,5,6],10))

#
# def func2():
#     print("我是函数2")
#
# list2 = [func2,100]
# print(list2[0]()) #我是函数2
#                   #None



# def test(x):
#     print(x)
# # 声明一个int类型的变量a
# a = 10
# #将变量a作为实参传递给变量test
# test(a)
#
# # 声明一个function类型的变量
# def func3():
#     print("我是函数3")
#     return "我是函数test"
# test(func3())  #func3() => "我是函数test"

#
# iter2 = iter([1, 10, 100, 1000])
# for x in iter2:
#     print('==:', x)

#
# def  creat_id():
#     num = 1
#     while True:
#         yield num
#         num+=1
#
# re = creat_id()
# a = next(re)
# b = next(re)
# print(a,b)
# def creat_id():
#     """
#     学号生成
#     :return:
#     """
#     num = 1
#     while True:
#         yield num
#         num += 1
# re = creat_id()
#
# def nuw_studen(**kwargs):
#     """
#     添加学生信息
#     :return:
#     """
#     kwargs["学号"]="stu_00"+str(next(re))
#     return kwargs
# print(nuw_studen(name=1,age=18,tel=12121))
# print("学号",":",nuw_studen(name=1,age=18,tel=12121)["学号"],end=" ")
# print("姓名",":",nuw_studen(name=1,age=18,tel=12121)["name"],end=" ")
# print("年龄",":",nuw_studen(name=1,age=18,tel=12121)["age"],end=" ")
# print("电话",":",nuw_studen(name=1,age=18,tel=12121)["tel"],end=" ")

# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# s= "DID"
# # for i in s:
# #     for x in s
# # for i in s:
