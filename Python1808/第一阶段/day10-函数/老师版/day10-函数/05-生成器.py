"""__author__ = 余婷"""

"""
1.什么是生成器
生成器就是迭代器；迭代器不一定是生成器

调用带有yield关键字的函数，拿到的结果就是一个生成器。生成器中元素就是yield关键字后边的值

2.生成器怎么产生数据
只要函数中有yield关键字，调用函数不会再执行函数体获取返回值，而是创建一个生成器。
当获取生成器的元素的时候,才会执行函数的函数体,执行到yield语句为止，并且将yield后面的值作为结果返回；
并且保存当前执行的位置。
获取下一个元素的时候，就从上次结束的位置接着往下去执行函数，直到函数结束或者遇到yield为止;
如果遇到yield就将yield后面的值作为结果返回，并且保存当前执行的位置。如果函数结束了，就出现StopIteration异常


生成器对应的函数，执行完成遇到yield的次数，决定了生成器能产生的数据的个数
"""
def func1():
    print('abc')
    yield 123
    print('!!!!!!')
    yield 100


re = func1()
print(re)

# next(re) - 执行re对应的函数的函数体,将yield关键字后边的值作为结果
print('===:', next(re))
# print('===:', next(re))
# print('===:', next(re))


def numbers():
    for x in range(101):
        yield x
        print('next', x)


gener = numbers()
print(next(gener))
print(next(gener))
print(next(gener))


# 写一个生成器可以无限产生学号
def creat_id():
    num = 0
    while True:
        yield 'stu'+str(num)
        num += 1

gener_id = creat_id()
print(next(gener_id))
for x in range(10):
    print(next(gener_id))

print(next(gener_id))


# 练习：写一个生成器，可以不断产生斐波那契数列：1，1，2，3，5，8，13，21....
#
def sequence(n):
    pre_1 = 0
    pre_2 = 1
    for _ in range(n):
        yield pre_2
        pre_1, pre_2 = pre_2, pre_1+pre_2


gen = sequence(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
for x in gen:
    print('for:', x)



