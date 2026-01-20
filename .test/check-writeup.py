
import sys
import hashlib

passed = set()

for line in sys.stdin:
    line = line.strip()

    part = line[2:].strip().lower()

    if line.startswith('1.'):

        d = ' '.join(part.split())
        h = hashlib.sha1(d.encode('utf-8')).hexdigest()

        if h == '0329ca04b9d15778448c2905a17e9f798af5dd09' or \
           h == '98b4065ad46d23f66cc26fc33703b720fd5a8b15':
            passed.add(1)
        else:
            print('writeup.txt: 1. incorrect')
    elif line.startswith('2.'):
        d = part.replace('0x', '')
        h = hashlib.sha1(d.encode('utf-8')).hexdigest()
        if h == 'f2c52ba54cc62d8f408c15cc338290817e4a8d75':
            passed.add(2)
        else:
            print('writeup.txt: 2. incorrect')

if len(passed) == 2:
    print('Passed all tests')
else:
    print('Error: missed tests')
