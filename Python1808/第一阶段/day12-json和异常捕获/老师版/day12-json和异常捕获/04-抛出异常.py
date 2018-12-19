"""__author__ = 余婷"""

"""
抛出异常：主动让程序出现异常

语法：
raise 错误类型    -  程序执行到raise的时候直接抛出异常

注意：错误类型必须是一个类，并且是Exception的子类
"""
# raise KeyError
print('====')


# 输入年龄，如果输入的年龄的范围不在0~100,程序就奔溃
class AgeError(Exception):
    def __str__(self):
        return '年龄越界了！'


# raise AgeError





