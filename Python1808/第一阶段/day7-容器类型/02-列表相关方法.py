"""
##1.列表赋值
a.直接使用一个列表变量给另一个列表变量赋值，赋的是地址。
赋完值之后，对其中一个列表进行增删改，会影响另一个列表。
list1 = [l,2,3]
list2 = list1
list2.append（100）
print（list1） # [1,2,3,100]

b.如果赋值的时候赋的是列表的切片或者拷贝，会产生新的地址，
然后使用新的地址去赋值。赋完值后，两个列表相互之间不影响。
list1 = [l,2,3]
list2 = list1[:](切片)  # ==list2 = list1.copy（）
list2.append（100）
print（list1） # [1,2,3]

"""

##2.列表中的方法
"""
1.列表.count（元素） - 获取指定元素在列表中出现的次数
2.列表1.extend（序列） - 将序列中所有的元素都添加到列表的末尾中
"""
list1 = [1,2,3]
list1.extend("ace1bb")
print(list1)

#####3.列表.index（元素） - 获取指定元素在列表中的下标值(如果元素有多个，只取第一个匹配的元素)
list1 = [1,3,4,[5,1],"ab",[1,5]]
print(list1.index([1,5]))

#####4.列表.reverse（） - 将列表中的元素倒序。
list1 = [1,3,4,[5,1],"ab",[1,5]]
list1.reverse()
print("reverse=:",list1)

#####5.列表.sort（） - 将列表进行升序排序(小到大)。
#####5列表.sort（reverse=True） - 将列表进行升序排序（大到小）。
"""  
注意：列表的元素：a.列表元素类型必须一样
                  b.列表元素支持比较运算符
"""
list1 = [1,3,4,5,1,1,5]
list1.sort()
print(list1) # (小到大) [1, 1, 1, 3, 4, 5, 5]
list1.sort(reverse = True)
print(list1) # (大到小)  [5, 5, 4, 3, 1, 1, 1]

list1 = [1,3,4,5,1,1,5]
list2 = list1.copy()
print(id(list1))
print(id(list2))

