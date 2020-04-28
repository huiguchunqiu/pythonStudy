#!/usr/bin/python3

tup1 = (1, 2, 3, 4, 5)
tup2 = ('physics', 'chemistry', 1997, 2007)

print(tup1[0], tup2[1:3])

tup4 = (122, 22)

tup3 = tup1 + tup4
print(tup3)

del tup4
# print(tup4)

for x in tup1:
    print(x)

list1 = [2, 3, 4, 'sss']

print(tuple(list1))
