"""__author__ = 余婷"""

# 1.
"""
numbers = 1
i = 0-19
i = 0   numbers = 1*2=2^1
i = 1   numbers = 2*2 = 2^2
i = 2   numbers = 2*2*2 = 2^3
...
i = 19  numbers = 2^20
"""
numbers = 1
for i in range(0, 20):
    numbers *= 2
print(numbers)
# 求2的20次方

# 2.
"""
num = 1 ~ 100
"""
summation = 0
num = 1
while num <= 100:
    if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
        summation += 1
    num += 1
print(summation)
# 统计1~100中能被3或者7整除但是不能同时被3和7整除的数的个数

# 1.求1到100之间所有数的和、平均值

# 2.计算1-100之间能3整除的数的和
sum1 = 0
for x in range(0, 101, 3):
    sum1 += x
print(sum1)


# 补充：sum函数是python内置函数：用来求数字序列的和
print(sum(range(101)))


# 3.求斐波那契数列列中第n个数的值：1，1，2，3，5，8，13，21，34....
# 第n个数 = 第n-1个数 + 第n-2个数
pre_1 = 1   # 第n-1个数
pre_2 = 1   # 第n-2个数
current = 1  # 当前数(第n个数),当n=1或者2的时候，当前数就是1

n = 6   # 第几个数
"""
num = 3  current=1+1= 2 pre_1,pre_2 = 2,1
num = 4  current=2+1=3  pre_1,pre_2=3,2
...
"""
for num in range(3, n+1):
    current = pre_1 + pre_2
    pre_1,pre_2 = current, pre_1

print('第%d个数是%d' % (n, current))


# 4.判断101-200之间有多少个素数，并输出所有素数。
# 素数：除了1和它本身不能被其他的数整除 -->
# 1）.将101-200中的每个都取出来
# 2）.判断取出来的每个数是否是素数：判断这个数从2开始到这个数-1是有一个能够被它整除的
for num in range(101, 201):
    # 判断这个num是否是素数
    for x in range(2, num):
        # 如果2~num-1之间有一个能够被num整除的就说明num不是素数
        if num % x == 0:
            # print(num, '不是素数')
            break  # 只需要找到一个就可以证明num不是素数
    else:
        print(num, '是素数')


# 方法二
for num in range(101, 201, 2):
    count = 0  # 存储2~num-1之间有几个能够被num整除的
    for x in range(2, num):
        if num % x == 0:
            count += 1
            break

    if count == 0:
        print(num,'是素数')

# 4.打印出所有的⽔水仙花数,所谓⽔水仙花数是指⼀一个三位数，其各位数字⽴立⽅方和等于该数本身。
# 例例如：153是 ⼀一个⽔水仙花数,因为153 = 1^3 + 5^3 + 3^3
for num in range(100, 1000):
    ge_wei = num % 10
    shi_wei = num // 10 % 10
    bai_wei = num // 100
    if num == ge_wei**3 + shi_wei**3 + bai_wei**3:
        print(num, '是水仙花数')


# 有⼀一分数序列列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列列的第20个分数
# 方案1：
# 当前分⼦: 上一个分数的分子加分母
# 当前分母：上一个分数的分子
fen_zi = 2
fen_mu = 1

n = 20
for x in range(2, n+1):
    fen_zi, fen_mu = fen_zi+fen_mu, fen_zi

print('%d/%d' % (fen_zi, fen_mu))


# 方案2
# 第n个分子: 第n-1个分子+第n-2个分子
# 第n个分母：第n-1个分母+第n-2个分母
fen_zi_1 = 2
fen_mu_1 = 1
fen_zi_2 = 3
fen_mu_2 = 2
current_fenzi = 0
current_fenzmu = 0
n = 20
for x in range(3, n+1):
    current_fenzi = fen_zi_1+fen_zi_2
    current_fenzmu = fen_mu_1 + fen_mu_2
    fen_zi_2, fen_mu_2, fen_zi_1, fen_mu_1 = current_fenzi, current_fenzmu, fen_zi_2, fen_mu_2

if n == 1:
    print('2/1')
elif n == 2:
    print('3/2')
else:
    print('%d/%d' % (current_fenzi, current_fenzmu))


# 5.给⼀一个正整数，要求：1、求它是⼏几位数 2.逆序打印出各位数字
# 方案一：
n = 2378273
str_n = str(n)
print('%d有%d位' % (n, len(str_n)))
print(str_n[::-1])

# 方案二：
n = 1236
count = 1
while n // 10:
    count += 1
    n //= 10
print(count)

n = 1236
for _ in range(count):
    print(n % 10, end='')
    n //= 10
