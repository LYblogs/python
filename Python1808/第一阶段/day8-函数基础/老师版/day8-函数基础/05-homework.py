"""__author__ = 余婷"""

# 1.已知一个列表，求列表中心元素。
# list1 = [1, 2, 3, 4, 5]   # index = 2 = len(list1) // 2
list1 = [1, 2, 3, 4, 5, 6]   # index = 2,3 = len(list1)//2, len(list1)//2-1

length = len(list1)
if length & 1:
    print(list1[length//2])
else:
    # length >> 1 相当于 length//2
    print(list1[length >> 1] - 1)
    print(list1[length >> 1])

# 2.已知一个列表，求所有元素和。
print(sum(list1))

# 3.已知一个列表，输出所有奇数下标元素。
list1 = [1, 2, 3, 4, 5, 6]
for index in range(1, len(list1), 2):
    print(list1[index], end=' ')

print()
# 4.已知一个列表，输出所有元素中，值为奇数的。
list1 = [10, 21, 35, 40, 5, 69, 2]
for item in list1:
    # item % 2 相当于 item % 2  == 1
    if item % 2 == 1:
        print(item, end=' ')
print()

# 5.已知一个列表，将所有元素乘二。
list2 = [1, 3, 4, 1, 2]  # [2, 6, 8, 2, 4]
for index in range(len(list2)):
    list2[index] *= 2
print(list2)

# 6.有一个长度是10的列表，数组内有10个人名，要求去掉重复的
# 方法一:
list2 = [1, 3, 4, 1, 2, 1, 2]   # [1, 3, 4, 2]
numbers = []
for item in list2:
    if item not in numbers:
        numbers.append(item)
list2 = numbers
print(list2)

# 方法二:
list2 = [1, 3, 4, 1, 2, 1, 2]
for item in list2.copy():
    # 统计元素的个数
    count = list2.count(item)
    # 如果个数大于1，就删一个
    if count > 1:
        list2.remove(item)
print(list2)

# 7.已知一个数字列表(数字大小在0~6535之间), 将列表转换成数字对应的字符列表
# 例如: list1 = [97, 98, 99] -> list1 = ['a', 'b', 'c']
list2 = [89, 78, 98, 110, 120, 7823]
for index in range(len(list2)):
    list2[index] = chr(list2[index])

print(list2)






