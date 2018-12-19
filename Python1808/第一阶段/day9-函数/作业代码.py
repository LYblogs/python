# 0.写一个匿名函数，判断指定的年是否是闰年 （对4%==0 or ）
# rui_nian =lambda year:"是闰年"if \
#     (year%4==0 and year%100!=0)or year%400==0  else "不是闰年"
# print("100%s"%rui_nian(100))
# print("4%s"%rui_nian(4))
# print("2000%s"%rui_nian(2000))



# 1.写一个函数将一个指定的列表中的元素逆序
# ( 如[1, 2, 3] -> [3, 2, 1])(注意:不要使  表自带的逆序函数)
# def  reverse_list(list1:list):
#     for index in range(len(list1)):
#         list1.insert(index, list1.pop())
#     return list1
# print(reverse_list([1,2,3,4,5,6]))


# 2.写一个函数，提取出字符串中所有奇数位上的字符

# def ji_num(str1:str):
#     tuple1=tuple(str1[1::2])
#     str2=""
#     for i in range(len(tuple1)):
#         str2+=tuple1[i]
#     return str2
# print(ji_num("abcdefghijk"))

# 3.写一个函数，统计指定列表中指定元素的个数(不用列表自带的count方法)
# def num_time(list1:list,items:str):
#     num=0
#     for i in list1:
#         if items ==i:
#             num+=1
#     return num
#
#
# print("次数为：%d"%num_time([1,4,6,6,5,6,88,66,6],6))
# print("次数为：%d"%num_time(["abc","cc","a","abc","zzz",1],"abc"))



# 4.写一个函数，获取指定列表中指定元素的下标
# (如果指定元素有多个，将每个元素的下标都返回)

# def items_index(list1:list,items):
#     i = 0
#     str1 =""
#     for index in range(i,len(list1)):
#         if list1[index]==items:
#             str1+=str(index)
#             i=index
#
#     return str1
# print(",".join(items_index([1,2,3,1,2,1],1)))


# 5.写一个函数，能够将一个字典中的键值对添加到另外一个字典中
# (不使用字典自带的update方法)
# def dict_add(dict1:dict,dict2:dict):
#     for key in dict1:
#         dict2[key] = dict1[key]
#     return dict2
# print(dict_add({"a":1,"ad":100},{"b":2,"eee":"dee"}))


# 6.写一个函数，能够将指定字符串中的所有的小写字母转换成大写字母；
# 所有的大写字母转换成小写字母(不能使用字符串相关方法)

# def exc_str(str1:str):
# #     str2 =""
# #     for i in str1:
# #         if  "A"<=i<="Z":
# #             num= ord(i)+32
# #             str_num =chr(num)
# #         if  "a"<=i<="z":
# #             num = ord(i) - 32
# #             str_num = chr(num)
# #         str2+=str_num
# #     return str2
# #
# # print(exc_str("aasdAAA"))




# 7.写一个函数，能够将指定字符串中的指定子串替换成指定的其他子串
# (不能使用字符串的replace方法)
# 例如: func1('abcdaxyz', 'a', '\') - 返回: '\bcd\xyz'
# def exc_str(str1:str,*args):
#     str2 =""
#     for i in str1:
#         if i == args[0]:
#             str2+=args[1]
#         else:
#             str2+=i
#     return str2
#
# print(exc_str("a/ce/s","/","a"))



# 8.实现一个输入自己的items方法，可以将自定的字典转换成列表。
# 列表中的元素是小的列表，里面是key和value (不能使用字典的items方法)
# 例如:{'a':1, 'b':2} 转换成 [['a', 1], ['b', 2]
def exc_list(dict1:dict):
    list1=[]
    for key in dict1:
        list1.append([key,dict1[key]])
    return list1


print(exc_list({"a":1,"b":2}))