#!/usr/bin/python3


class MyClass:
    i = 12345
    """一个简单的类"""
    def f(self):
        return 'hello world'


x = MyClass()

print(x.i)
print(x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


y = Complex(3.0, -4.5)
print(y.r, y.i)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁 " % (self.name, self.age))


p = people('wxy', 8, 33)
p.speak()


class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('wxy', 8, 23, 2)
s.speak()


class speaker():
    topic = ""
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s, 我是一个演说家，我演讲的主体是 %s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Tim', 25, 80, 4, "python")
test.speak()


class Parent:
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):
    def myMethod(self):
        print('调用子类方法')


c = Child()
c.myMethod()
super(Child, c).myMethod()


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d,%d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)

print(v1 + v2)
