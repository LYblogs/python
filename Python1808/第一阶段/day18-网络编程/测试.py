# import re
# str1 ="草你麻痹的 你是sb吗"
# result =re.sub(r"[草麻痹]|sb","*",str1)
# # print(result)
# def func2():
#     return [1, 2]
# list1 = func2()  #[1,2]
# func2().append(3)
# print(list1)
# print(type(0x66))
# mydict={"a":1,"b":2,"c":3}
# mydict_new=dict(zip(mydict.values(),mydict.keys()))
# print(mydict.keys())
# A0 ={"a":1,"b":2,"c":3,"d":4,"e":5}
# A1 = 0,1,2,3,4,5,6,7,8,9
# # print(1 in A0)
# A2 =[]
# A3=[1,2,3,4,5]
# A4=[1,2,3,4,5]
# A5={0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
# A6=[[0,0],[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81]]
A0=dict(zip(("a","b","c","d","e"),(1,2,3,4,5)))
print(A0)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1=range(10)
A2=[i for i in A1 if i in A0]
print(A2)#[]
A3=[A0[s] for s in A0]
print(A3) #[1, 2, 3, 4, 5]
A4=[i for i in A1 if i in A3]
print(A4) #[1, 2, 3, 4, 5]
A5 ={i:i*i for i in A1}
print(A5) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 =[[i,i*i] for i in A1]
print(A6) #[[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]


