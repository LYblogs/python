"""
指导思想：
1.使用数据的时候去本地文件中取数据
2.数据修改后，将新的数据更新到本地文件中

"""
#写一个程序统计当前程序执行次数。第一次运行程序打印1，第二次运行的时候打印2。
with open("./files/蓝莲花.txt",encoding="utf-8") as f :
    count =int(f.read())
    print("第%d次进入程序"%count)
count+=1
with open("./files/蓝莲花.txt","w") as f :
    f.write(str(count))
