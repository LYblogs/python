"""__author__ = 余婷"""

import copy
"""
copy.copy(对象)  - 浅拷贝 （直接拷贝元素的值产生一个新的地址）
copy.deepcopy(对象) - 深拷贝(不会直接复制地址，而是将地址对应的值拷贝一份产生新的地址)
"""
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
list1 = [numbers1, numbers2]

print('1.浅拷贝：')
list2 = list1.copy()
print('修改前list1:', list1)
print('修改前list2:', list2)
print('针对list1进行修改')
list1.append(111)
list1[0].append(100)
print('修改后list1:', list1)
print('修改后list2:', list2)


numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
list1 = [numbers1, numbers2]
print('2.深拷贝')
list2 = copy.deepcopy(list1)
print('修改前list1:', list1)
print('修改前list2:', list2)
print('针对list1进行修改')
list1.append(111)
list1[0].append(100)
print('修改后list1:', list1)
print('修改后list2:', list2)
