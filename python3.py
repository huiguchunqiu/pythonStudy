#!/usr/bin/python3
# 文件名：using_sys.py
import support
import sys
print('命令行参数如下：')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

support.print_func('wxy')
dir(sys)

print('{a}:{b}'.format(a='ww', b='cc'))

f = open('./tmp/foo.txt', 'w')

f.write('Python 是一个非常好的语言。\n是的，的确非常好！\nhahah')
f.close()
