#!/usr/bin/python3
print("hello, Python!")
a = 0
print(a)
kile = 'smile'
tine = 'add'

print(kile + '222' + tine)

given_name = "Luffy"
middle_names = 'D'
family_name = "Monkey"

name_length = len(given_name + middle_names + family_name)
name_character_limit = 15
print(name_length <= name_character_limit)

'''
注释
'''
"""
这是注释
"""
# 这是注释
# ”“”

# 类型转化

8
8.0
True
'hello'

print(type(8))
print(type(8.0))
print(type(True))
print(type('hello'))

print(float(8))
print(int(8.0), int(8.4))

print(bool(8), bool(True), bool(0), bool(-1), bool('hello'))

print(int(True), int(False), str(True), float(True))

print(int('92'), float('3'))

# print(int('33132ss'))

# 字符串方法

# len 长度
print(len('hello world'))
# type 类型
print(type('8'))
# islower()
Mom_side = 'Tom is a good boy'
print(Mom_side.islower())

print(Mom_side.count('o'))

print('miss'.capitalize())

print(Mom_side.find('233'))

print(Mom_side.index('is'))

print(Mom_side.isalnum())
print('222'.isalnum(), 'sdk'.isalnum())

coming = 1

print(coming)

coming = 2

print(coming)

del coming

print('十六点222sss'.islower())
print('十六点222sss2分色法 3DG2 '.islower())
print('HELLO world'.islower())
print('hello soo 23中'.islower())

print('322'.isnumeric())
print('23ss'.isnumeric())
print('23s sds'.isspace())
print(' '.isspace())
str1 = '1..'
sms = ('a', 'b', 'c')
print(str1.join(sms))
sqs = ['2', '2', 'sw']
print(str1.join(sqs))


a = input('input:')

print(a)


i = 2
while i < 100:
    j = 2
    while j <= i / j:
        if not (i % j):
            break
        j = j + 1
    if j > i / j:
        print(i, ' 是素数')
    i = i + 1
print("Good bye!")


