"""
1.变量的作用域
变量能够在程序中使用的范围

2.全局变量
a.声明在函数或者类的外部的变量都是全局变量
b.从声明开始变量的作用域是从变量开始到py文件结束，任何位置都可以使用。

3.局部变量
a.声明在函数或者类的里面的变量都是局部变量
b.从变量声明开始到函数结束，任何位置都可以使用。

4.global
只能在函数中使用，用来在函数中声明一个全局变量
语法：
global 变量名
变量名 = 值

5.nonlocal
当需要在局部的局部中修改局部的变量的值，就使用nonlocal
nonlocal 变量名
变量名 = 值
"""
#==================全局变量================
a=10
for x in  range(10):
    y = 20
    print(x)
print(x,y)


def func1():
    print("函数中",a,x,y)


func1()

# ===============局部变量========================
def func2(num1,num2):
    print(num1,num2)
    aa=11

# print(num1) #NameError: name 'num1' is not defined


#================global=======================
#声明一个全局变量a1
a1 = 100
def test1():
    #声明一个局部变量a1
    # a1 =200
    # print()
    global  a1
    a1=200
    print("函数内",a1)


test1()
print("函数外",a1)


#===================== nonlocal==========================
def func1():
    a2 = "abc"
    def func2():
        nonlocal a2
        a2 ="python"
        print("a2:",a2)
        #a3的作用域在func2（）中，使用func1（）不能使用
        a3 =111
    func2()
    print("func1()中：",a2)
func1()


function =[]
for x in range(5):
    def func1(a):
        return  a*x
        function.append(func1)
t1 = function[0]
t2 = function[2]
print(t1(2),t2(2))
