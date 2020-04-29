#!/usr/bin/python3


def hello():
    print("hello World!")


hello()


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")

w = 4
h = 5
print("width =", w, " height =", h, " area=", area(w, h))


def print_me(str1):
    print(str1)
    return


print_me('我要调用用户自定义函数')
print_me('再次调用同一函数')


def change_int(a):
    a = 10


b = 2
change_int(b)
print(b)


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值：", mylist)


def printme(str):
    print(str)
    return


printme(str='wxy')


def printinfo(name, age):
    print("名字：", name)
    print("年龄：", age)
    return


printinfo(age=10, name='wxy')


def printinfo2(name, age=8):
    print('名字：', name)
    print('年龄：', age)
    return


printinfo2('wxy', 10)
printinfo2('wxy')


def printinfo3( arg1, *vartuple):
    print('输出：')
    print(arg1)
    print(vartuple)
    return


printinfo3(70, 89, 'xxx')


def printinfo4(arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo4(10)
printinfo4(70, 40, 20)


def printinfo5(arg1, **vardict):
    print('输出：')
    print(arg1)
    print(vardict)


printinfo5(1, b=2, c=3)


def f(a, b1, *, c1, d1):
    return a + b1 + c1 + d1


print(f(1, 2, c1=3, d1=4))

sum = lambda arg1, arg2: arg1 + arg2

print("相加后的值为：", sum(10, 20))
print("相加后的值为：", sum(20, 20))
