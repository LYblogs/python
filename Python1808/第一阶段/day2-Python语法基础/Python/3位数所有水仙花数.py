num = 100
while  num <= 999:
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if  num == pow(a,3) + pow(b,3) + pow(c,3):
        print(num)
    num += 1