# numbers=1
# for i in range(0,20):
#    numbers*=2
# print(numbers)
# print(1*2**20)
# summation = 0
# num = 1
# while num <= 100:
#     if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
#         summation += 1
#     num += 1
# print(summation)



# # 1. 求斐波那契数列中第n个数的值：1，1，2，3，5，8，13，21，34....
# num = int(input("斐波那契数列中第n个数的值："))
# n1 = 1
# n2 = 1
# index = 2
# num1 = 0
# while True:
#     if num == 1 or num == 2:
#         print(1)
#         break
#     while index < num:
#         num1= n1 + n2
#         n1 = n2
#         n2 = num1
#         index += 1
#     print(num1)
#     break

# 计算1-100之间能3整除的数的和
# 方法1:
# sum =0
# for i in range(101):
#     if i%3==0:
#         sum += i
# print(sum)
# # 方法2：
# sum = 0
# num = 0
# while num <= 100:
#     if  num%3 == 0:
#         sum+=num
#     num+=1
# print(sum)

# 2. 判断101-200之间有多少个素数，并输出所有素数。
# 判断素数的方法：用一个数分别除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数
# sum = 0
# for i in range(101,201):
#     num = 2
#     while num<i:
#         if i % num ==0:
#             break
#         else:
#             num+=1
#         if  num==i:
#             print(i)
#             sum+=1
# print("素数有%d个"%(sum))

# 打印出所有的水仙花数,所谓水仙花数是指一个三位数，其各位数字立方和等于该数本身。例如：153是
# 一个水仙花数,因为153 = 1^3 + 5^3 + 3^3
# num = 100
# # while num<999:
# #     a = num // 100
# #     b = num // 10 % 10
# #     c = num % 10
# #     if  num == a**3+b**3+c**3:
# #         print(num)
# #     num+=1

# 4.有一分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个分数
# 分子：上一个分数的分字加分母 分母: 上一个分数的分子
# fz = 2 fm = 1    fz+fm / fz

# fz1=2
# fm1=1
# index = 1
# for i in range(19):
#     fn = fz1 +fm1
#     fm1 = fz1
#     fz1 = fn
#     index +=1
# print("第%d个数为：%d/%d"%(index,fz1,fm1))


# 5. 给一个正整数，要求：1、求它是几位数 2.逆序打印出各位数字
# str1 = input()
# num1 = len(str1)
# str2 = str1[::-1]
# print("它是%d位数"%(num1))
# print(str2)

# 1.控制台输入年龄，根据年龄输出不同的提示(例如:老年人，青壮年，成年人，未成年，儿童)
# age = int(input("请输入您的年龄："))
# if  age<=0:
#     print("请输入正确年龄")
# elif age<=6:
#     print("儿童")
# elif age<18:
#     print("未成年")
# elif age<=25:
#     print("成年人")
# elif age<=40:
#     print("青壮年")
# elif age<=100:
#     print("老年人")
# else:
#     print("请输入正确年龄")


# 2.计算5的阶乘5!的结果是
# a = 1
# n = 1
# for i  in   range(5):
#     a*=n
#     n+=1
# print("5!=%d"%(a))
# 3.求1+2!+3!+...+20!的和 1.程序分析：此程序只是把累加变成了累乘。
# sum = 0
# for i in range(1,21):
#     a = 1
#     n = 1
#     while n<=i:
#         a*=n
#         n+=1
#     sum+=a
# print("它们的和为：%d"%(sum))

# 4.计算 1+1/2!+1/3!+1/4!+...1/20!=?
# sum = 0
# for i in range(1,21):
#     a = 1
#     n = 1
#     while n <= i:
#         a *= n
#         n += 1
#     sum+=a**-1
# print("它们的和为：%0.10f"%(sum))




# 5.循环输入大于0的数字进行累加，直到输入的数字为0，就结束循环，并最后输出累加的结果。

# sum = 0
# # num = int(input("请输入一个数："))
# # while   True:
# #     sum += num
# #     if  num ==0:
# #         break
# #     else:
# #         num = int(input("请输入一个数："))
# # print("它们的和是：%d"%sum)

# 6.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。 
# 1.程序分析：关键是计算出每一项的值。
# a = int(input("请输入需要计算的数:"))     #2
# num1 = int(input("请再输入次数:"))# 5
# sum = 0
# b = a
# c = 0
# for i in range(1,num1+1):
#      if num1 == 1:
#          print("和为：%d"%(a))
#          break
#      else:
#          sum += a
#          a=b+a*10
#      print(a, end="")
#      c+=1
#      if c==num1:
#          print("=",end="")
#      else:
#          print("+",end="")
# print(sum)

# 7.输入三个整数x,y,z，请把这三个数由小到大输出。
# num1 = int(input("请输入第1个数:"))
# num2 = int(input("请输入第2个数:"))
# num3 = int(input("请输入第3个数:"))
# if  num1<num2:
#     max = num2
#     sec = num1
#     thi = num3
# if  num1<num3:
#     max = num2
#     sec = num3
#     thi = num1
# if  num2<num3:
#     max = num3
#     sec = num2
#     thi = num1
# print("从小到大排列为：%d  %d  %d"%(thi,sec,max))

# a.根据n的值的不同，输出相应的形状
# n = 5时             n = 4
# *****               ****
# ****                ***
# ***                 **
# **                  *
# *
# a=1
# n = int(input("请输入一个奇数："))
# for i in range(n):
#     if  n &1 ==0:
#         n = int(input("请输入一个奇数："))
#         continue
#     else:
#         str1 ="*"*a
#         print(str1.center(10))
#         a+=2
#         if  a>n:
#             break

# a=1
# # for i in range(1,10):
# #     for j in range(1,10):
# #         if j>a:
# #             break
# #         print("%d*%d=%d" % (j, i, i * j), end=" ")
# #     a+=1
# #     print()

# 10.这是经典的"百马百担"问题，有一百匹马，驮一百担货，
# 大马驮3担，中马驮2担，两只小马驮1担，问有大，中，小马各几匹？

