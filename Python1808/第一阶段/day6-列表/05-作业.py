# list1 = [1,2,3,4,"abc",5,7,8]
# if  len(list1)&1== 1:
#     print(list1[int(len(list1)/2)])
# else:
#     print(list1[int(len(list1)/2-1)],list1[int(len(list1)/2)])

# 2.已知一个列表，求所有元素和。
list1 = [1,2,3,4,5,6]
print(sum(list1))

# 3.已知一个列表，输出所有奇数下标元素。
list2 = [1,2,3,4,5,6]
print(list2[::2])

# 4.已知一个列表，输出所有元素中，值为奇数的。
# list3 = [1,2,3,4,5,6,7]
# list4 =[]
# for i in list3:
#     if i&1==1:
#         list4.append(i)
# print(list4)

# 5.已知一个列表，将所有元素乘二。
# list3 =[1,2,3,4,5,6,7]
# index = 0
# for i in list3:
#     list3[index] = 2*i
#     index+=1
# print(list3)

# 6.有一个长度是10的列表，数组内有10个人名，要求去掉重复的
# 例如:names = ['张三', '李四', '大黄', '张三'] -> names = ['张三', '李四', '大黄']
names = ['张三', '张三', '李四',"盲僧", '大黄',"压缩","刘五","马六","盲僧","压缩"]
names1 = []
for i  in names:
    if i not in names1:
        names1.append(i)
print(names1)

# 7.已知一个数字列表(数字大小在0~6535之间), 将列表转换成数字对应的字符列表
list1 = [97, 98, 99]
index = 0
for i in  list1:
    list1[index]=chr(i)
    index+=1
print(list1)
# 8.用一个列表来保存一个节目的所有分数，求平均分数(去掉一个最高分，去掉一个最低分，求最后得分)
list2 =[90,80,70,99,88,78]
list2.remove(max(list2))
list2.remove(min(list2))
print("平均值是:%d"%(int(sum(list2)/len(list2))))

# 9.有两个列表A和B，使用列表C来获取两个列表中公共的元素

# 例如: A = [1, 'a', 4, 90]  B = ['a', 8, 'j', 1] --> C = [1, 'a']

A =[1,3,5,7,9,"a","z"]
B =[1,5,9,"a","b"]
C =[]
for i in A:
    if i in A and i in B:
        C.append(i)
print(C)
