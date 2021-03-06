"""
一旦一个字符串确定了，那么每个字符串中的每个字符的位置就确定了
而且每个字符会对应一个用来表示其位置和顺序的下标值
"""
"""1.下标（索引）
字符串中每个字符都有一个下标，代表其在字符串中的位置
下标的范围：0~字符串长度-1
           -1~字符串长度（-1代表最后一个字符的位置） 
"""

"""
2.获取单个字符
语法：字符串[下标] -  获取字符串中，指定下标对应的字符
说明：字符串- 可以是字符串常量，也可以是字符串变量
str = "abcd"
print(str[2])

3.获取部分字符
语法：字符串[开始下标：结束下标：步长]
说明：字符串 - 可以是字符串常量，也可以是字符串变量
    [] - 固定写法
     开始下标、结束下标 - 下标值
     步长 - 整数
功能：
从开始下标开始获取到结束下标前为止。每次下标值增加步长。结果还是字符串。

注意：当步长是整数（从前往后取），开始下标对应的字符要在结束下标对应的字符前
      当步长是负数（从后往前取），开始下标对应的字符要在结束下标对应的字符后面

4.获取部分字符，省略下标
 开始下标和结束下标都可以省略
- 开始下标省略
字符串[：结束下标]
步长是正数：从字符串开头开始往后获取
步长是负数：从字符串结尾开始往前获取
- 结束下标省略
字符串[开始下标：：步长]
步长是正数：从开始下标从前往后获取到字符串结束
步长是负数：从开始下标从后往前获取到字符串开头
print（str[::-1]） #相当于字符串倒叙
"""
