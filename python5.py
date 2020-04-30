#!/usr/bin/python3
import os
import shutil
import glob
import sys
import re
import math
import random
from urllib.request import urlopen
from datetime import date
import zlib
myUrl = os.getcwd()
print(myUrl)
# os.system('mkdir today')
# dir(os)
# help(os)

shutil.copyfile('HelloPython.py', 'hellopysw.py')
# shutil.move('./today/12.txt', 'ssss')
print(glob.glob('*.py'))
print(sys.argv)
sys.stderr.write('Warning, log file not found starting a new one\n')

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print(math.cos(math.pi/4))
print(math.log(1024, 2))

w = random.choice(['apple', 'pear', 'banana'])
print(w)
print(random.random())
print(random.randrange(6))


# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)


now = date.today()
print(now)
now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')
print(now)

birthday = date(2010, 2, 23)
age = now - birthday
print(age.days)

s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))


