num1 = int(input('请输入一个三位数：'))
a = num1 // 100
b = num1 // 10 % 10
c = num1 % 10
if num1 == pow(a,3) + pow(b,3) + pow(c,3):
    print ('是水仙花数')
else:
    print('不是水仙花数')    
