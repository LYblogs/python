# import re
# re_str =r"\d+\.?\d+"
# str1 =input("请输入字符串：")
# result =re.findall(re_str,str1)
# sum =0
# for countent in result:
#     sum+=float(countent)
# # print(sum)
# print(ord("年"))
# print(chr(24180))
# print(hex(24180))
# # 5e74
# print(str.split("sadas/adas/23123/d","/"))

list1 = [
    {'name': '张三', 'age': 20},
    {'name': '李四', 'age': 10},
    {'name': '王五', 'age': 30}
]
# list1.sort(key=lambda item: item['age'])
# print(list1)

def key(item):
    return item["age"]
print(key(list1[1]))
# print(key({'name': '张三', 'age': 20}))
