'''格式:
for 变量名 in 集合 
    语句'''
for i in [1,2,3,4,5]:
    print(i)
a = range(11)
for b in  a:
    print(b)
for Index, m in enumerate([1,2,3,4,5]):
    print(Index,m)
sum = 0
a = range(1,101)
for x in a:
    sum += x
print(sum)