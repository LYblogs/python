# 1. 编写一个函数，求1+2+3+...+N
# N =int(input())
# def N_sum(N):
#     sum = 0
#     for i in range(N+1):
#         sum+=i
#     print(sum)
# N_sum(N)
# 2. 编写一个函数，求多个数中的最大值
# list1 = [187,19,30,655,44]
# def num_max(list1):
#     index=0
#     max = list1[0]
#     while index<len(list1):
#         if list1[index]>max:
#             max = list1[index]
#         index+=1
#     print(max)
# num_max(list1)

# 3. 编写一个函数，实现摇色子的功能，打印n个色子的点数和
# import random
# n = int(input("请输入有多少个色子："))
# def sum_saizi(n):
#     sum = 0
#     for i in range(n):
#         num =random.choice(range(1,7))
#         sum+=num
#     print(sum)
# sum_saizi(n)



# 4. 编写一个函数，交换指定字典的key和value。
# 例如:{'a':1, 'b':2, 'c':3} ---> {1:'a', 2:'b', 3:'c'}
# dict1 ={'a':1, 'b':2, 'c':3}
# def exchange_key(dict1):
#     for key in dict1.copy():
#         dict1[dict1[key]] = key
#         del dict1[key]
#     print(dict1)
# exchange_key(dict1)
# 5. 编写一个函数，三个数中的最大值
# list1 = [187,19,30]
# def num_max(list1):
#     index=0
#     max = list1[0]
#     while index<len(list1):
#         if list1[index]>max:
#             max = list1[index]
#         index+=1
#     print(max)
# num_max(list1)


# 6. 编写一个函数，提取指定字符串中的所有的字母，然后拼接在一起后打印出来
# 例如：'12a&bc12d--' ---> 打印'abcd'

# str1 = input("请输入字符串:")
#
# def  take_str(str1):
#     str2=""
#     for i in str1[:]:
#         if i.isalpha():
#             str2+=i
#     print(str2)
# take_str(str1)

# 7. 写一个函数，求多个数的平均值
# list1 = [121,225,33,888,999]
# def  num_ave(list1):
#     sum = 0
#     for i in list1:
#         sum+=i
#     index =len(list1)
#     print(sum/index)
# num_ave(list1)

# 8. 写一个函数，默认求10的阶层，也可以求其他数的阶层
# def  num_jc(num,key=None):
#     if num ==:
#         jc = 1
#         for i in range(1, 11):
#             jc *= i
#         print(jc)
#     jc = 1
#     for i in range(1,num+1):
#         jc*=i
#     print(jc)
# num_jc()

# 9. 写一个函数，可以对多个数进行不同的运算
# 例如: operation('+', 1, 2, 3) ---> 求 1+2+3的结果
#  operation('-', 10, 9) ---> 求 10-9的结果
#  operation('*', 2, 4, 8, 10) ---> 求 2*4*8*10的结构
# tuple1=("*",2,4,8,10)
# def num_jg(tuple1):
#     str1 = ""
#     for i in tuple1[1:]:
#         str1 +=str(i)
#     print(eval(tuple1[0].join(str1)))
# num_jg(tuple1)

# def num_jg(str1,*num):
#     if  str1 =="+":
#         sum = 0
#         for i in num:
#             sum+=i
#         print("它们的和为：%d"%(sum))
#     if str1=="*":
#         cj =1
#         for i in num:
#             cj*=i
#         print("它们的积为：%d"%(cj))
#     if str1 =="-":
#         jj=num[0]
#         for i in num:
#             jj-=i
#         print("它们的差为：%d"%(jj))
# num_jg("+",1,5,6)
# num_jg("*",1,5,6)
# num_jg("-",1,5,6)
max