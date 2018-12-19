import json
"""
1.json数据：a.只能有一个数据，并且这个数据必须是json支持的类型的数据

2.json支持的数据类型：
1.数字类型
2.字符串（双引号引起来的）
3.布尔
4.数组
5.字典
6.特殊值

3.json与python数据的转换
json.load(文件对象) - 将json文件里面的数据转换成python数据
json.loads（字符串）- 将json数据转换成python数据
json.dump（文件对象）- 将python文件里面的数据转换成json数据
json.dumps（字符串）- 将python数据转换成json数据
"""

print(json.dumps('abc')) # -> '"abc"'
print(json.dumps([1,2,'abc'])) #-> "[1, 2, "abc"]"


"""
二.异常捕获
try: - except:捕获所有异常
try: - except 异常类型: 捕获指定异常
try: - except （异常类型1，异常类型2）： 捕获多个指定异常，做出相同反应
try：- except 异常类型1：- except 异常类型2： 捕获多个异常，做出不同反应

finally - 不管try后面的代码有没有异常，也不管异常是否捕获到，都会执行finally后面的代码段

"""

"""
三.抛出异常
raise 异常类型
异常类型必须是一个类，并且这个类是exception的子类

"""