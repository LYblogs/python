"""
1.变量 = 值（声明变量）

name = "李毅"
num1 = num2 = num3
num11 ， num12 = 10,30

"""
# summation = 0
# num = 1
# while num <= 100:
#     if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
#         summation += 1
#     num += 1
# print(summation)
# num = int(input("斐波那契数列中第n个数的值："))
# n1 = 1
# n2 = 1
# index = 2
# num1 = 0
# if not (not (num == 1) and not (num == 2)):
#     print(1)
# while index < num:
#     num1= n1 + n2
#     n1 = n2
#     n2 = num1
#     index += 1
# print(num1)
# sum = 0
# # for num in range(101,201):
# #     for  i in range(2,num):
# #         if  num % i == 0:
# #             break
# #     else:
# #         sum+=1
# #         print(num)
# # print(sum)

num = 100
while num<999:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if  num == a**3+b**3+c**3:
        print(num)
    num+=1
