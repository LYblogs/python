num1 = int(input('请输入一个数:'))
num2 = int(input('请输入一个数:'))
if num1 < num2:
    min = num1
else:
    min = num2
for x in range(1,min+1):
    if num1 % x == 0 and num2 % x == 0:
        1
print('这两个数的最大公约数为：%d'%(x))
