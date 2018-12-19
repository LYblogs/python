"""__author__ = 余婷"""

"""
1.什么是模块
python中一个py文件就是一个模块

2.怎么关联多个模块
方式1：
import 模块名  - 将指定的模块导入到当前模块中，导入所有的全局变量(模块名就是py文件的文件名)

说明:
a.执行import的时候，实质会进入指定的模块对应的py文件中，去执行里面的代码
b.import导入模块的时候，会检测当前模块之前是否已经导入过，如果已经导入过就不再导入
c.通过import去导入一个模块后，可以通过 模块名.全局变量 去使用被导入的模块中的内容

"""
import test1
# import test1

# 使用test1中的变量
a = test1.test1_a
print('当前模块:', a)

# 调用test1中的函数
test1.test1_func1()

"""
方式2：
from 模块名 import 变量名/函数名 - 导入模块中指定的变量或者函数

说明:
a. 执行到导入模块的语句的时候，还是会先执行指定模块中的所有语句
b. 通过from-import导入的时候，导入多次还是只执行一次（查重）
c. 使用的时候只能用import后面的变量/函数，而且用的时候不用在前面加模块名
d. import后面可以使用逗号将多个变量/函数隔开。也可以使用*将模块中的所有的全局变量一起导入
"""
from test2 import test2_a, test2_func1
# from test2 import *       # 同时倒入test2中所有的全局变量
# from test1 import test1_a
print('当前模块', test2_a)
test2_func1()

# import random
# random.randint(10, 20)

# from random import randint
# randint(10, 20)

"""
函数 - 对功能进行封装      -  获取当前时间对应的代码封装到函数中
模块 - 对多个功能和多个数据进行封装     -  将所有和时间相关的函数或者变量放到一个py文件中
包 - 对多个模块进行封装  -  将所有和时间相关的py文件放到一个文件夹中 
什么是包： 含有__init__.py文件的文件夹

3.重命名
import 模块名 as 新模块名
from 模块名 import 变量名 as 新变量名
"""
import math as sys_math
# from test import test1 as test1_1
#
# print(test1.test1_a)
# print(test1_1.test1_a)

"""
4.包的导入
import 包名   - 会直接执行包中的__init__.py文件中的代码
import 包名.模块名  - 导入指定包中的执行模块

from 包名 import 模块名
from 包名.模块名 import 变量
"""
# import test
# import test.test1
# print(test.test1.test1_a)

from test import my_test
# print(my_test.aaa)
from test.my_test import aaa
print(aaa)


