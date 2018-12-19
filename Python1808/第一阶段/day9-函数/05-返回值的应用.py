"""
返回值能做的事情，函数调用表达式都可以做

"""
# 1.用函数调用表达式给变量赋值
def func1():
    return "hello"
print(func1())

# 2.通过函数调用表达式使用相应的方法
def func2():
    return [1,2]
func2() #[1,2]
item = func2().append(3)
print(item)
# func2()=[1,2]
print(func2()[0])



3.#将函数调用表达式作为容器的元素，函数的参数，函数的返回值。


