"""
生成器就是迭代器；迭代器不一定是生成器
生成器就是带有yield关键字的函数的结果
调用带有yield关键字的函数，拿到的结果就是一个生成器。生成器的元素就是yield关键字后面的值


只要有yield关键字，就不会执行函数体与获取返回值，而是创建一个生成器
当获取生成器的元素的时候，才会执行函数的函数体，执行到yield语句位置，
并且将yield后面的值作为结果返回；并且保存当前执行的位置;
直到函数结束或者遇到yield为止


生成器对应的函数，执行完成遇到yield的次数，决定了生成器能产生数据的个数
"""
def x():
    print("函数里")
    yield 100
    print("!!!")
    yield 200
print(x())
re = x()
#next(x()) - 执行x（）对应的函数体，将yield关键字后面的值作为结果
print(next(re))
print(next(re))

def numbers():
    for x in range(101):
        yield x

re = numbers()
for i in range(101):
    print("迭代器：",next(re))

    #写一个生成器可以无限产生学号
def  creat_id():
    num = 1
    while True:
        yield num
        num+=1

re = creat_id()

print(next(re))


#写一个生成器，可以不断产生斐波拉契数列1,1,2,3,5,8,13...
def fb_num():
    num1 = 0
    num2 = 1
    index = 0
    while True:
        num1,num2=num2,num1+num2
        index+=1
        yield "第%d数为：%d"%(index,num1)
re = fb_num(10)

for i in re:
    print(re)

print(int(True))