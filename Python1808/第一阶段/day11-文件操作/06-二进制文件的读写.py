"""
open方法的另外一种写法：
with open（文件路径，读写方式，encoding = 编码方式） as 文件对象：
        文件操作
--> 打开文件，将文件存在文件对象中。当文件操作完成会自动关闭
"""


with open("./files/蓝莲花.txt",encoding="utf-8") as f :
    print(f.read())
print(f.closed)  #True

"""
2.二进制文件的读
普通的文本文件，也可以以二进制的形式读和写
注意：二进制不能设置编码方式
"""
with open("./files/蓝莲花.txt","rb") as f :
    content = f.read()
    print(content)

"""
3.文件不存在
当以读的方式打开一个不存在的文件，会报“FileNotFoundError:”
当以写的方式打开一个不存在的文件，不会报错，并且会创建这个文件。（任何写的方式都可以）
"""
with open("bbb.txt","w")as f:
    # print(f.read()) #FileNotFoundError: [Errno 2] No such file or directory: 'bbb.txt'
    pass
