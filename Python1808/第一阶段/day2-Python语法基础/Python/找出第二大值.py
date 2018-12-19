list1 = []
num = 0
while num < 5:
    val = int(input())
    list1.append(val)
    num += 1
print(list1)
list1.sort()
count = list1.count(len(list1)-1)
print(count)
a = 0
while a < count:
    list1.pop()
    a += 1
print(list1[len(list1)-1])