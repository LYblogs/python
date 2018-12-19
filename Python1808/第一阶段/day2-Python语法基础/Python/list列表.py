#创建一个空列表
list1 = []
print(list1)
#创建带有元素的列表
list2 = [18,19,20,21,22]
index = 0
sum = 0
while index < 5:
    sum += list2[index]
    index += 1
    if index ==5:
        print('平均值为：%d'%(sum/5))
#注意：元素可以是不同类型的
list3 = [1,2,'sunck','good',True]
print(list3)


#列表元素的访问
#取值   格式：列表名[下标]
list4 = [1,2,3,4,5]
print(list4[2])

#替换
list4[2] = 300
print(list4)



#列表操作：
#列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)

#列表的重复
list8 = [1,2,3]
print(list8 * 3)

#判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)

#列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

#二维列表
list11 = [[1,2,3],[4,5,6]]
print(list11)
print(list11[1][0])


#列表方法
#list.append :添加新的元素
list12 =[1,2,3]
list12.append(4)
list12.append([5,6,7])
print(list12)

#list.extend 在末尾一次添加另一个列表的多个值
list13 =[1,2,3,4]
list13.extend([6,7,8])
print(list13)

#list.insert 在下标处添加一个元素，原数据向后移
list14 = [1,2,3,4,5]
list14.insert(1,[5,7])
list14.insert(0,5)
print(list14)


#list.pop 移除列表中指定下标处的元素，默认移除最后一个元素
list15 = [1,2,3,4,5]
list15.pop()
list15.pop(2)
print(list15)


#list.remove  移除列表中的某个元素，第一个匹配的元素
list16 = [1,2,3,4,5,4,3,4]
list16.remove(4)
print(list16)  


#list.clear 全部删除
list17 = [1,2,3,4,5]
list17.clear()
print(list17)

#查找  查找某个值第一个匹配的索引值
list18 = [1,2,3,4,5]
index18 = list18.index(3)
print(index18)


#列表中元素的个数
list19 = [1,2,3,4,5]
print(len(list19))


#获取最大/最小值
list20 = [1,2,3,4,5]
print(max(list20))
print(min(list20))


#list.count() 获取列表中指定数值的个数
list21 = [1,2,3,4,5,1,1,21,3,4,5,90]
print(list21.count(1))

num= 0
index = list21.count(1)
while num < index:
    list21.remove(1)
    num += 1
print(list21)

#list.reverse() 倒叙
list22 = [2,1,3,4,5]
list22.reverse()
print(list22)

#list.sort() 升序
list23 = [2,1,3,4,5]
list23.sort()
print(list23)


#浅拷贝 引用
list24 = [1,2,3,4,5]
list25 = list24
list25[1] = 100
print(list24)
print(list25)
print(id(list24))
print(id(list25))


#深拷贝  内存拷贝
list26= [1,2,3,4,5]
list27 = list26.copy()
list27[2] = 200
print(list26)
print(list27)
print(id(list26))
print(id(list27))


#将元祖转成列表
list28 = list((1,2,3,4,5))
print(list28)
