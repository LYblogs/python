num = int(input('请输入一个数：'))
if num == 2:
    print("是质数")
num1 = 2
while num1 < num:
    if num % num1 == 0:
        print('不是质数')
    num1 += 1
    if num1 == num:
        print('是质数')



