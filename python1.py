#!/usr/bin/python3

list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))
for x in it:
    print(x, end=' ')

print('end')

import sys

list2 = [1, 2, 3, 4]
it = iter(list2)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


print('sss')


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            n = self.a
            self.a += 1
            return n
        else:
            raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)
for x in myIter:
    print(x)
print('sds')


def jidan(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1


f = jidan(10)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()



