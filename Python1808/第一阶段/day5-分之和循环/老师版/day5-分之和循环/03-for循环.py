"""__author__ = 余婷"""
"""
python中的循环结构有两种：for循环和while循环

什么时候用循环：某个操作需要重复执行，就考虑用循环
"""
# 1.for循环
"""
a.语法：
for 变量 in 序列:
    循环体

b.说明：
for - 关键字
变量 - 变量名，随便命名(满足变量名的要求)
in - 关键字
序列 - 可以是字符串、列表、元祖、字典、集合、迭代器、range
循环体 - 和for保持一个缩进的一条或者多条语句(需要重复执行的代码)

c.执行过程：
让变量去序列中取值，一个一个的取，取完为止；每取一个值，执行依次循环体
（for循环中，序列中值的个数，决定了循环的次数; 序列中的内容，控制每次变量取到的值）

d.注意：
如果for后面的变量取到的值，在循环体里面不使用，那么这个变量命名的时候，用一个_来命名
"""
"""
x = a    print('=====')
x = b    print('=====')
x = c    print('=====')
"""
for x in '1234':
    print(x)
    print('=====')


# 2.range
"""
range(n) - 产生一数字序列，序列中的内容是0 ~ n-1 (结果是序列)
range(m,n) - 产生一数字序列，序列中的内容是m ~ n-1
range(m,n,step) - 产生一数字序列, 从m开始，每次加step,直到n前为止

range一般用在:a.需要产生指定范围的数字序列 
             b.单纯的控制for循环的循环次数
"""
for num in range(10):
    print(num)

print('~~~~~~~~~~')
for num in range(10, 21):
    print(num)

print('~~~~~~~~~~')
for num in range(0, 10, 2):
    print(num)

# 练习：求1+2+3+...+100
print('~~~~~~~~~~~~~')
"""
sum1 = 0
num = 1  sum1 += num  sum1 = sum1+num = 0+1
num = 2  sum1 += num  sum1 = sum1+num = 1+2
num = 3  sum1 += num  sum1 = sum1+num = 1+2+3
num = 4  sum1 += num  sum1 = sum1+num = 1+2+3+4
...
num = 100 sum1 += num  sum1 = sum1+num = 1+2+..+99+100

"""
sum1 = 0   # 保存和
for num in range(1, 101):
    # sum1 = sum1+num
    sum1 += num
print(sum1)


# 练习：2+4+6+8+...100
# 方法1：不用if语句
sum1 = 0
for num in range(2, 101, 2):
    sum1 += num
print(sum1)

# 方法2；用if语句
sum1 = 0
for num in range(101):
    if num % 2 == 0:
        sum1 += num

# 练习：写程序统计一个字符串中数字字符的个数
# 'ajshf237hajfk90sss7'  -> 数字字符个数是:6

str1 = 'ajshf237hajfk90sss7'
count = 0    # 保存数字字符的个数
# 将字符串中的每次字符取出来
for char in str1:
    # 判断是否是数字字符
    if '0'<=char<='9':
        # print(char)
        count += 1
print('数字字符个数是:%d' % (count))

# 用循环控制打印10行'***'
for _ in range(10):
    print('***')



