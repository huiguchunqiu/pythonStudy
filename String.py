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


# a = input('input:')

# print(a)


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

word = 'hello word'
print(word[2])

print(word[1])

str2 = "python example...wow!!!"
print(str2)
str3 = str2.ljust(50, 's')   # 填充字符必须为单字符
print(str3)

str2 = 'PyThon ExamPle ... WoW!!!'
str3 = str2.lower()
print(str3)

str4 = '   python example'
str5 = str4.lstrip()
str6 = str4.lstrip('   py')
print(str4, str5, str6)

in_tab = 'a,e,i,o,u'
out_tab = '102030405'

tran_tab = str.maketrans(in_tab, out_tab)

str7 = 'this is string example....wow!!!'
print(str7.translate(tran_tab))
str8 = 'this is abc lalala'
str9 = 'this-is-abc-lalala!!!'
print('max is ' + max(str8), ";  min is  " + min(str9))

str1 = 'www.thefool.club'
print(str1.partition('.'))

str2 = 'this is string example...wow!!!'
print(str2.replace('is', 'was', 1))

str3 = 'this is really a string example.'

substr = 'is'
print(str3.rfind(substr))
print(str3.rindex(substr))
print(str3.rindex('xa'))
print(str3.index('a'))
print(str3.rjust(50, 's'))
print(str1.rpartition('.'))
str4 = '   this is string example!!!   d   8989'
print(str4.rstrip('89'))
str3 = 'al slid\nssdd sddd \\\s\tsd '
str5 = 'google#baidu#taobao'
print(str5.split('#'), str5.split('#', 1), str3.split())

str6 = 'sid\n\sds\rsssd\ns\tssee\n\t'
print(str6.splitlines(), str6.splitlines(True))

str7 = '   lsdi ss  '
print(str7.strip())

str8 = 'Made in china'

print(str8.swapcase())

print(str8.title())

print(str8.upper())
print(str8.zfill(30))
