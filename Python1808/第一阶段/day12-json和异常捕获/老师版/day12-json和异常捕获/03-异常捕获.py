"""__author__ = 余婷"""
"""
1.什么是异常
程序执行过程中出现错误，也叫出现异常

2.异常捕获
让本来会出现异常的位置，不出现异常，而是自己去处理异常出现的情况

3.怎么捕获异常
情况一：捕获所有的异常
a.语法：
try:
    代码段1
except:
    代码段2
    
b.执行过程: 执行代码段1，如果代码段1中出现异常，不会奔溃，而是马上执行代码段2。
         如果代码段1没有异常，不会执行代码段2
    
"""

try:
    print(int('abc'))
    print('~~~~~')
    print([1, 2, 3][10])
    print('++++++')
except:
    print('出现异常!')

print('===========')

"""
情况二：捕获指定的异常
a.语法：
try:
    代码段1
except 错误类型名:
    代码段2
    
b.执行过程: 执行代码段1，当代码段1出现指定类型的异常后不奔溃，而是执行代码段2
"""

try:
    print([1, 2, 3][10])
    print('~~~~~')
    print(int('abc'))
    print('++++++')
except IndexError:
    print('下标越界!')

print('!!!!!')


"""
情况三：同时捕获多个异常，对不同的异常做出相同的反应
try:
    代码段1
except (错误类型1, 错误类型2, 错误类型3...):
    代码段2
    
执行过程：执行代码段1，当代码段1中出现了指定的异常,不崩溃，然后执行代码2
"""
try:
    print([1, 2][10])    # IndexError
    # print(int('abc'))   # ValueError
    # print({'a': 1}['b'])  # KeyError
except (IndexError, KeyError, ValueError, FileNotFoundError, StopIteration):
    print('出现多种异常中的一个!')


"""
情况四：同时捕获多个异常，对不同的异常做出不同的反应
try:
    代码段1
except 错误类型1:
    代码段2
except 错误类型2:
    代码段3
...

"""
try:
    # print([1, 2][10])
    print(int('abc'))
except KeyError:
    print('键错误!')
except ValueError:
    print('值错误!')
except IndexError:
    print('下标越界!!!!')


"""
4.try-except-finally
try:
    代码段1
except:
    代码段2
finally:
    代码段3
    
不管代码段1中是否出现异常，也不管异常是否能够捕获到，finally后面的代码段3都会执行!(写遗书的位置!)
"""
try:
    print([1, 2][10])
except IndexError:
    print('下标越界错误！')
finally:
    print('最后！！！')

print('最后~~~')


"""
什么时候使用异常捕获：
明明知道某段代码可能会出现异常，但是又没有办法避免，就使用异常捕获
"""
# 练习：输入成绩，直到输入的数据输入正确为止！
while True:
    try:
        score = float(input('输入成绩：'))
        break
    except ValueError:
        print('输入有误！请输入数字')
        # score = float(input('输入成绩：'))


# 封装一个函数，功能是获取指定文件中的内容(普通文本文件)
# 从封装角度：调用者做的事情越少越好！
def get_file_content(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print('文件路径有误！')
        return ''


print(get_file_content('new.json2'))