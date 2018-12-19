"""__author__ = 余婷"""
# import requests

"""
1. open方法的另外一种写法:
with open(文件路径, 读写方式, encoding=编码方式) as 文件对象:
    文件操作

--> 打开文件，将文件存在文件对象中。当文件操作完成会自动关闭
"""
with open('files/蓝莲花.txt', encoding='utf-8') as f:
    print(f.read())

print(f.closed)   # True


"""
普通的文本文件，也可以以二进制的形式读和写

2. 二进制文件的读写
只要将读写方式设置为 'rb'/'br'就可以了。读出来的数据直接就是二进制数据
注意：二进制操作不能设置编码方式
"""
# 二进制文件的读
with open('files/蓝莲花.txt', 'rb') as f:
    content = f.read()
    print(content, type(content))

with open('files/luffy4.jpg', 'rb') as f:
    content = f.read()
    print(content)

# 二进制文件的写
with open('imge.jpg', 'wb') as f:
    f.write(content)

# 图片下载
# response = requests.get('https://wx4.sinaimg.cn/mw690/4674e705ly1fck5nxjt74j20yi1pc7mb.jpg')
# with open('下载.jpg', 'wb') as ff:
#     ff.write(response.content)


"""
3.文件不存在
当以读的方式打开一个不存在的文件，会报'FileNotFindError'
当以写的方式打开一个不存在的文件，不会报错，并且会创建这个文件
"""
# with open('bbb.txt', 'r') as f:
#     print(f.read())


with open('ddd.txt', 'bw') as f:
    # print(f.write())
    pass










