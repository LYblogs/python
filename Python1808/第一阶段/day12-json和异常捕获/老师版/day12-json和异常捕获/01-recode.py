"""__author__ = 余婷"""

"""
1.生成式(生成式的结果就是一个生成器)
(表达式 for 变量 in 序列)

# def func1():
#     for 变量 in 序列:
#         yield 表达式

(表达式 for 变量 in 序列 if 条件语句)

# def func1():
#     for 变量 in 序列:
#         if 条件语句:
#              yield 表达式

2.模块和包
模块: 一个py文件就是一个模块
包: 一个带有__init__.py文件的文件夹
import 
from - import 

3.文件操作
open(文件路径, 打开方式, encoding=编码方式)

'r' - 读出来的是字符串
'w' - 写字符串到文件中
'br' - 读出来的是字节(二进制)
'bw' - 写二进制数据到文件中
'a' - 写，追加(写字符串到文件中)
编码方式 - 文本文件的编码方式
         'utf-8'
         'gbk'
         
f.read()
f.readline()
f.readlines()
f.write()


with open(文件路径, 打开方式, encoding=编码方式) as f:
    文件操作

"""
from package1 import test1 as T1, test2 as T2

dict1 = dict((value, key) for key, value in {'a': 1, 'b': 2, 'c': 3}.items())
print(dict1)


def my_dict(seq):
    new_dict = {}
    for item in seq:
        if len(item) != 2:
            raise ValueError
        new_dict[item[0]] = item[1]
    return new_dict


dict1 = my_dict((value, key) for key, value in {'a': 1, 'b': 2, 'c': 3}.items())
print(dict1)

