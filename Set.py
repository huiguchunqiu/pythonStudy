#!/usr/bin/python3
b = set('sqwsddassasdasacasanamesi试试是的是的22单独')
a = {'orange', 'banana', 'apple'}
c = set('abcdefg')
print(b)
print(a)
print(c - b)
print(c | b)
print(c & b)
print(c ^ b)

s = {'s', 'c'}
s.add('x')
print(s)
s.update(['sd', 2])
s.update({'age': 12}, ('s2d', 's32'))
print(s)
s.remove('x')
print(s)
s.discard('ssdd2')

print(s)
s.discard('sd')
print(s)
s.pop()
print(s)
print(len(s))
print('ss' in s)
b = s.copy()
s.clear()
print(s)
print(b)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z, x)
x.difference_update(y)
print(x)

a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}
c = {'f', 'g', 'c'}
result = a.intersection(b, c)
print(result)
a.intersection_update(b, c)
print(a, b, c)
print(b.isdisjoint(c))
print(a.issubset(c))
print(a.issuperset(c))
print(c.issuperset(a))
print(b.symmetric_difference(c))
b.symmetric_difference_update(c)
print(b)

