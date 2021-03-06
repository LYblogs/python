"""
1.列表（list） - 可变 ， 有序
获取元素 - 通过下标获取元素

增 - append ，insert，extend（直接添加序列所有的元素） 列表.extend(序列) - 将序列中所有的元素都添加到列表中
              b.列表.insert(下标, 元素) - 在指定的下标前插入指定的元素
删 - remove（元素） ，del（下标），pop（下标），clear
改 -  列表[下标] = 新值

2.元组（tuple） - 不可变 ， 有序
获取元素 - 通过下标获取元素
变量1，变量2 - 元素1， 元素2
变量1，*变量2 = 元素1，元素2，。。。元素n

3.字典(dict) - 可变 ，无序
获取元素 - 通过键获取元素
增 - 字典[key] = 值   字典.update（序列） 注意:在这儿的序列要求是能够转换成字典的序列。序列中的元素是只有两个元素的小序列
                                                dict1.update([[1, 2], ['a', 2], [2, 'b']])
删 - del 字典[key]    字典.pop(key)

改 - 字典[key] = 新值
"""
list1 = [1,2,3]
list1.extend("ace1bb")
print(list1)


dict1 = {'a': 100, 'b': 200}
# 当key值有重名的时候，会用序列中键值对对应的值，更新原字典的key对应的值
dict1.update({'aa': 10, 'bb': 20, 'a': 'abc'})
print(dict1)

dict1.update([[1, 2], ['a', 2], [2, 'b']])
print(dict1)