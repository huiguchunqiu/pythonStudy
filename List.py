#!/usr/bin/python3

list1 = ['physics', 'chemistry', 1293, 322]

print(list1)
del list1[2]
print(list1)

# 一些操作符

print(len(list1))
print(list1 + [3, 4, 5, 5])

print(['hi!'] * 4)
print(3 in [3, 2, 3, 1])
for x in [1, 2, 3]:
    print(x)

L = ['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])

# 函数
list1 = [1, 3, 5, 1]
list2 = [2, 2, 1]
seq = (3, 2, 2)
print(len(list1))
print(max(list1))
print(min(list1))
print(list(seq))
list1.append(3)
print(list1)
print(list2.count(2))
list1.extend(list2)
print(list1)
print(list1.index(3))
list2.insert(2, (2, 3))
print(list2)
list2.pop()
print(list2)
list1.remove(1)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)
list3 = [11, 4, 12, 31, 9, 12, 2, 8, 16]
list3.sort()
print(list3)
list4 = ['facebook', 'Taobao', 'google']
list4.sort()
print(list4)
