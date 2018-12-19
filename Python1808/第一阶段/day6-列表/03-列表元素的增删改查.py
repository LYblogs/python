# 1.查（获取列表的元素）
"""
a.获取单个元素
列表[下标] - 获取指定下标对应的元素

列表一但确定，列表中的每个元素都对应一个下标；
下标范围：0~列表长度-1 ； -1 ~ 列表长度（下标不能越界）


"""
films = ["回村的诱惑", "回家的诱惑", "回屯的诱惑"]
print(films[2])

"""
b.获取多个元素（切片） - 结果是列表
列表[开始：结束：步长]
"""

# 2.增（添加元素）
"""
a.列表.append（元素）- 在指定的列表的最后添加指定的元素

"""
# 练习：录入学生成绩，保存到一个列表中。（录入的时候不断输入学生成绩，直到输入"end"）
# list2 = []
# num = 0
# score = input("请输入成绩：")
# while True:
#     if score == "end":
#         print(list2)
#         break
#     else:
#         list2.append(int(score))
#         num +=1
#         score = input("请输入成绩：")
# print(int(sum(list2)/num))

"""
b.列表.insert（下标，元素） - 在指定下标前插入指定的元素



"""

films = ["海贼王", "进击的巨人", "一拳超人", "一人之下"]
films.insert(2, "海绵宝宝")
print(films)
films.insert(0, "死神")
print(films)

# 练习：有一个有序的数列[1,7,34,67,100],输入任意一个数字，插入到序列中，要求插入后，数列还是从小到大排序的。
list2 = [1, 7, 34, 67, 100]
num1 = int(input("请输入一个数字:"))
for i in range(len(list2)):
    if list2[i] >= num1:
        list2.insert(i, num1)
        break
else:
    list2.append(num1)
print(list2)

"""
c.遍历列表（将元素中的元素一个一个的取出来）
   for  变量  in 列表 - >  用变量获取列表中的元素
    通过遍历下标获取列表元素  

"""

# 3.删（删除列表元素）
"""
a.del 列表[下标] - 删除列表中指定下标对应的元素
del - 关键字 ， 可以删除任何内容


b.列表.remove(元素) - 删除指定列表中指定的元素
注意：如果指定的元素在列表中有多个，只删除第一个匹配的元素

c.列表.pop（） - 取出列表中最后一个元素   只是把元素从序列中取出来，并可以重新使用
列表.pop（下标）- 取出列表中指定小标对应的元素
"""
# 练习：有一个列表，列表中有数字和字符串有两种元素。要将这个列表中的字符串全部放在另一个列表中
list3 = [1, "ab", 303, "hello", 89, 9, 90]
list4 = []
list5 =list3.copy()
num = 0
for index in list5:
    if isinstance(index, str):
        del_index = list3.pop(num)
        list4.append(del_index)
    else:
        num += 1
print(list3)
print(list4)

#4.改（修改列表元素的值）
"""
列表[下标] = 新值 - 将列表中指定下标对应的元素修改成指定的值

"""
list1 = [1,2,"abc",4]
list1[2] = 3
print(list1)