"""__author__ = 余婷"""

# 0.写一个匿名函数，判断指定的年是否是闰年
"""
闰年：能够被4整除但是不能被100整除。或者能够被400整除
"""
isleapyear = lambda year: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(isleapyear(2012))
print(isleapyear(2008))
print(isleapyear(2018))
print(isleapyear(2000))


# 1.写一个函数将一个指定的列表中的元素逆序( 如[1, 2, 3] -> [3, 2, 1])(注意:不要使 表自带的逆序函数)
def reverse(list1: list):
    length = len(list1)
    for index in range(length//2):
        list1[index], list1[length-1-index] = list1[length-1-index], list1[index]


my_list = [1, 2, 3]   # index = 0  list1[index] = list1[len(list1)-index-1]
reverse(my_list)
print(my_list)


# 2.写一个函数，提取出字符串中所有奇数位上的字符
def get_substr(str1: str):
    strstr = ''
    for index in range(len(str1)):
        if index & 1:
            strstr += str1[index]
    return strstr


print(get_substr('abcdefg'))


# 3.写一个函数，统计指定列表中指定元素的个数(不用列表自带的count方法)
def get_count(list1, item):
    count = 0
    for x in list1:
        if x == item:
            count += 1
    return count


print(get_count([1, 23, 3, 4, 4, 23], 4))


# 7.写一个函数，能够将指定字符串中的指定子串替换成指定的其他子串(不能使用字符串的replace方法)
# 例如: func1('abcdaxyz', 'a', '//') - 返回: '//bcd//xyz'
def replace(str1: str, old, new):
    # 先切割
    str_list = str1.split(old)

    strstr = str_list[0]
    for index in range(1, len(str_list)):
        strstr += '+'+str_list[index]

    return strstr


print(replace('abcabchasjhsabchjshdjfabcsjhdfjhabc123', 'abc', '+'))