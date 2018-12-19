import random
list = []
num = 10000
num1 = 0
while num <= 99999:
    a = num // 10000
    b = num // 1000 % 10
    c = num // 100 % 10
    d = num // 10 % 10
    e = num % 10
    if a == e and b ==d:
        list.append(num)
    num += 1
print(random.choice(list))