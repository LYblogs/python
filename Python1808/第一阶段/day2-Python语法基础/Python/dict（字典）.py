'''
概述：
使用键-值(key-value)存储，具有极快的查找速度
key的特性：
1、字典中的key必须唯一
2、key必须是不可变的对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能为key
value:数据(字符串，列表，数字.)
'''

dict1 ={'tom':60,'lilei':70}

#元素的访问
#获取：字典名[key]
print(dict1['lilei'])

#添加
dict1["hanmeimei"] = 99
dict1["lilei"] = 80
print(dict1)

#删除
dict1.pop("tom")
print(dict1)