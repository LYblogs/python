# dict1 = {"a":2,"b":3}
# print("a"in dict1)
# def student_id():
#     id =1
#     while True:
#         yield id
#         id+=1
# re =student_id()
# print(next(re))
def  creat_id():
    num = 1
    while True:
        yield num
        num+=1

re = creat_id()
