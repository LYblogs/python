num1 = int(input('请输入一个三位数：'))
a = num1 // 100
b = num1 // 10 % 10
c = num1 % 100
if  a == c:
    print('True')
else:
    print('False')