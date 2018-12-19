"""__author__ = 余婷"""
import json
"""
一.json数据
1.json数据:a.只有一个数据   b.数据类型是json支持的类型

2.json数据转python  
json.load(文件对象)
json.loads(字符串)

3.python数据转json
json.dump(数据, 文件对象)
json.dumps(数据)  - 字符串
"""
json.dumps('abc')  # -> '"abc"'
json.dumps([1, 2, 'aaa'])   # '[1, 2, "aaa"]'

"""
二.异常捕获
try - except    -  捕获所有异常
try - except 异常类型   - 捕获一个指定异常
try - except (异常类型1, 异常类型2,...)   - 捕获多个指定异常
try - except 异常类型1 - except 异常类型1  - 捕获多个指定异常

finally - 不管try后面的代码有没有异常，异常是否能够捕获到，都会执行
"""

"""
三. 抛出异常
raise 异常类型  -  让程序主动报错

异常类型 - 必须是Exception的子类
"""



