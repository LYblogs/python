num = int(input('请输入一个五位数：'))
a =num // 10000
b =num //1000 %10
c = num // 100 % 10
d = num // 10 % 10
e = num % 10
if a == e and b == d:
    print('这个数是回文数')
else:
    print('这个数不是回文数')