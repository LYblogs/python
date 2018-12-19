"""__author__ = 余婷"""

"""
指导思想：
1.使用数据的时候去本地文件中取数据
2.数据修改后，将新的数据更新到本地文件中
"""

# 写一个程序统计当前程序执行的次数。第一次运行程序打印1，第二次运行的时候打印2，以此类推
# count = 1
# print(count)
# count += 1
with open('files/count.txt', encoding='utf-8') as f:
    count = int(f.read())    # 读到的是字符串
    # print(count)
    print('第%d次进入程序' % count)

# 让次数加1
count += 1
with open('files/count.txt', 'w', encoding='utf-8') as f:
    # 以'w'方式打开，写入的时候只能写字符串
    f.write(str(count))