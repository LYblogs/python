"""__author__ = 余婷"""

# 1.查(获取列表的元素)
"""
a.获取单个元素
列表[下标] - 获取指定下标对应的元素

列表一旦确定，列表中的每个元素都对应一个下标；
下标范围：0 ~ 列表长度-1；-1 ~ -列表长度
下标不能越界
"""
films = ['战狼2', '肖生克的救赎', '沉默的羔羊', '蝴蝶效应', '回到未来', '变形金刚', '小羊肖恩']
print(films[2], films[-1])
# print(films[10])   # IndexError: list index out of range

"""
b.获取多个元素(切片) - 结果是列表
列表[开始下标:结束下标:步长]
列表[开始下标:结束下标]
"""
print(films[1:5:2])
print(films[:4])
print(films[::-1])

"""
c.遍历列表(将列表中的元素一个一个取出来)
for 变量 in 列表 -> 用变量获取列表中的元素
"""
names = ['小明', '小花', '小红', '黄梅梅']
# 方法一:直接获取列表元素
for item in names:
    print(item)

# 方法二:通过遍历下标获取列表元素
for index in range(len(names)):
    print(names[index])


# 2.增(添加元素)
"""
a.列表.append(元素) - 在指定的列表的最后添加指定的元素(不会产生新的列表)
"""
films = ['战狼2', '肖生克的救赎', '沉默的羔羊', '蝴蝶效应', '回到未来', '变形金刚', '小羊肖恩']
films.append('电锯惊魂')
print(films)

# 练习：录入学生成绩，保持到一个列表中。（录入的时候不断输入学生的成绩，直到输入'end'为止）
# scores = []
# score = input('请输入成绩:')
# while score != 'end':
#     scores.append(int(score))
#     score = input('请输入成绩:')
#
# print(scores, sum(scores))

"""
b.列表.insert(下标, 元素) - 在指定的下标前插入指定的元素
"""
films = ['海贼王', '火影忍者', '进击的巨人', '一人之下', '一拳超人']
films.insert(2, '海绵宝宝')
print(films, films[2])
films.insert(0, '死神')
print(films)

# 练习2: 有一个有序的数列[1, 7, 34, 67, 100]。
# 输入任意一个数字，插入到数列中，要求插入后数列还是从下到大排序的
# 例如：3 -> [1, 3, 7, 34, 67, 100]
# 200 -> [1,7, 34, 67, 100, 200]
#  0 -> [0, 1, 7, 34, 67, 100]
nums = [1, 7, 34, 67, 100]
value = int(input('请输入一个数字:'))   # 输入一个数字，并且将输入的内容转换成int类型
# index = 0 ~ len(nums) - 1
for index in range(len(nums)):
    if nums[index] >= value:
        nums.insert(index, value)
        break
else:
    # 如果没有找到一个比输入的数大的元素
    nums.append(value)

print(nums)

# 3.删(删除列表元素)
"""
a. del 列表[下标] - 删除列表中指定下标对应的元素
del - 关键字, 可以删除任何内容
"""
films = ['战狼2', '肖生克的救赎', '沉默的羔羊', '蝴蝶效应', '回到未来', '变形金刚', '小羊肖恩']
del films[-2]
print(films)

"""
b.列表.remove(元素) - 删除指定列表中指定的元素

注意：如果指定的元素在列表中有多个，只删除最前那一个
"""
films = ['战狼2', '肖生克的救赎', '蝴蝶效应', '沉默的羔羊', '蝴蝶效应', '回到未来', '小羊肖恩']
films.remove('蝴蝶效应')
print(films)

"""
c. 
列表.pop() - 取出列表中最后一个元素
列表.pop(下标) - 取出列表中指定下标对应的元素
"""
nums = [2, 34, 56, 7, 8, 9, 0]
del_num = nums.pop()   # 将最后一个元素取出, 并且保存到变量del_num中
print(nums)
print(del_num)

del_num = nums.pop(1)
print(nums)
print(del_num)

# 练习：有一个列表，列中有数字和字符串两种类型的元素。要求将这个列表中的字符串全部放到另外一个列表中
# 例如：list1 = [1, 'ab', 303, 'hello', 89, 9, 90]
# --> list1 = [1, 303, 89, 9, 90]  并且产生一个新的列表,list2 = ['ab', 'hello']
# isinstance(10, int)  # 判断10是否是整型
"""
list1 = [1, 'ab', 'bbb', 'hello', 89, 9, 90]
index = 0   1
index = 1  'ab'   list1 = [1, 'bbb', 'hello', 89, 9, 90]
index = 2  'hello'
"""
list1 = [1, 'ab', 'bbb', 'hello', 89, 9, 90]
list2 = []
index = 0
while index < len(list1):
    if isinstance(list1[index], str):
        # 取出
        item = list1.pop(index)
        # 添加到新的列表中
        list2.append(item)
        continue

    index += 1

print(list1, list2)

# 4.改(修改列表元素的值)
"""
列表[下标] = 新值 - 将列表中指定下标对应的元素修改成指定的值
"""
list1 = [1, 2, 'abc', 4]
list1[2] = 3
print(list1)


a = "ssa" \
    "asdasd"
