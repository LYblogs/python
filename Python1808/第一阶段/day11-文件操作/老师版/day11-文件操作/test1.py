"""__author__ = 余婷"""


def test1_func1():
    def test1_func2():
        print('我是模块1——1')
    print('我是模块1')

print('test1:', __name__)

if __name__ == '__main__':
    print('=======================')
    print('test1')
    test1_a = 100
    for x in range(100):
        print(x)

    test1_func1()
    print('=======================')