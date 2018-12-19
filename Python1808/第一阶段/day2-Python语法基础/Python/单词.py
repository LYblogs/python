str = input()
str1 = str.strip()
index = 0
sum = 0
while index < len(str1):
    while str1[index]  != " ":
        index += 1
        if index == len(str1):
            break
    sum += 1
    if index == len(str1):
        break
    while str1[index] == ' ':
        index +=1
print(sum)