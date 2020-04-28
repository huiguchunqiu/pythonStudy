#!/usr/bin/python3

# Fibonacci series: 斐波那契额数列

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

i = 256*256
print(i)

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

var1 = 100
if var1:
    print('1 - if 表达式条件为true')
    print(var1)

var2 = 0
if var2:
    print('2 - if 表达式条件为true')
    print(var2)
print('good bye!')

age = int(input('请输入你家狗狗的年龄：'))
print('')
if age <= 0:
    print("你是在逗我吧！")
elif age == 1:
    print('相当于 14 岁的人。')
elif age == 2:
    print('相当于 22 岁的人。')
elif age > 2:
    human = 22 + (age - 2)*5
    print('对应人类年龄：', human)
# 退出提示
input('点击 enter 键退出')

number = 7
guess = -1
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜你，你猜对了")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

num = int(input("输入一个数字："))
if num%2 == 0:
    if num%3 == 0:
        print("你输的数字可以整除2和3")
    else:
        print('你输的数字可以整除2，不可以整除3')
else:
    if num%3 == 0:
        print("你输的数字可以整除3，不可以整除2")
    else:
        print("你输的数字不能整除2 和 3")

'''
var = 1
while var == 1:
    num = int(input('输入一个数字：'))
    print('你输入的数字是：', num)
print("good bye")
'''
count = 0
while count < 5:
    print(count, ' 小于 5')
    count = count + 1
else:
    print(count, ' 大于或等于5 ')

sites = ['baidu', 'google', 'runoob', 'taobao']
for site in sites:
    if site == 'runoob':
        print('菜鸟')
        break
    print('循环数据 ' + site)
else:
    print('没有循环数据！')
print('完成循环！')

for i in range(5):
    print(i)

for i in range(4,10,3):
    print(i)

a = ['google', 'baidu', 'runoob', 'taobao', 'qq']
for i in range(len(a)):
    print(i, a[i])

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

n = 7
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)

