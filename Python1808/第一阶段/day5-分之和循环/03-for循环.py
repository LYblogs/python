"""
python中的循环结构有两种：for循环和while循环
什么时候用循环：某个操作需要重复执行，就考虑用循环

1.for循环
语法：
for 变量 in 序列：
    循环体
说明：
for - 关键字
变量 - 随便命名，满足变量名的要求
in - 关键字
序列 - 可以是字符串、列表、元组、字典、集合、迭代器、range
循环体 - 和for保持一个缩进的一条或者多条语句（需要重复执行的代码）

执行过程：
让变量去序列中取值，一个一个的取，取完为止；每取一个值，执行一次循环体
（for循环中，序列中值得个数，决定了循环的次数;序列中的内容，控制每次变量取到的值）
注意：如果for后面的变量取到的值，在循环体里面不使用，那么这个变量命名的时候，用一个_来命名

2.range
range（n）- 产生一数字序列，序列中的内容是0~n-1（结果是序列）
range（m，n）- 产生一数字序列，序列的内容是m~n-1（结果是序列）
range（m，n，step）- 产生一数字序列，序列的内容是从m开始，每次加step，取到n为止。

range一般用在：1.需要产生指定范围的数字序列
               2.单纯的控制for循环的次数
"""
for num in range(10):
    print(num) #0~9
for num in range(10,21):
    print(num)
print("*****")

list1 = []
for i in range(10):
    list1.append(i)
print(list1)
# 练习：求1+2+3+...+100和
sum1 = 0
for  i in range(101):
    sum1 += i
print("和为：%d"%(sum1))

#练习：2+4+6...+100
# 方法1
sum2 = 0
for  num in range(2,101,2):
    sum2 +=num
print("和为：%d"%(sum2))
# 方法2
sum3 = 0
for num1 in range(101):
    if not num1 & 1:
        sum3+=num1
print(sum3)

#练习：写python统计一个字符串中数字字符的个数
# str1 =input()
str1 = "sdsdd1212187"
sum4 = 0
for index in str1:
    if "0"<=index<="9": #if index.isdigit():
        sum4 += 1
print(sum4)
# 练习：所有三位数回文数的和
sum5 = 0
for i in range(100,1000):
    a = i //100
    c = i % 10
    if  a==c:
        sum5+=i
print(sum5)
