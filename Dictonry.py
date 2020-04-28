#!/usr/bin/python3

dict1 = {
    'alice': '2341',
    'beth': '9102',
    'cecil': '3258'
}

print(dict1, dict1['alice'])

dict1['name'] = 'wxy'
dict1['age'] = 8
print(dict1)

del dict1['name']
print(dict1)
dict1.clear()
print(dict1)
del dict1
# print(dict1)
seq = ('name', 'age', 'sex')
dict2 = dict.fromkeys(seq)
print(dict2)
dict1 = {
    'alice': '2341',
    'beth': '9102',
    'cecil': '3258',
    'age': 8
}
print(dict1.get('age'), print(dict1.get('liss')))

print('age' in dict1)

print(dict1.items())
for x, y in dict1.items():
    print(x, y)
print(dict1.keys())
print(dict1.values())
print(dict1.setdefault('sss'))
dict1.update(dict2)
print(dict1)
dict1.pop('sss')
print(dict1)
dict1.popitem()
print(dict1)
