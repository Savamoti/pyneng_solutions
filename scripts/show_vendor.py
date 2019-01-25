#!/usr/bin/env python3
"""
Скрипт написан после прочтения 7 главы "Работы с файлами".
Надо скачать базу маков "wget http://standards-oui.ieee.org/oui/oui.txt".
Скрипту нужен аргумент, mac-address в любом виде.
"""
from sys import argv
mac = argv[1:]
mac = ''.join(mac).replace(':', '').replace('.', '').replace('-', '').upper()
text = mac[0:6]
print('\n','Hexadecimal: ', mac[0:2] + ':' + mac[2:4] + ':' + mac[4:6] + ':' + mac[6:8] + ':' + mac[8:10] + ':' + mac[10:12],
'\n','Bit-reversed: ', mac[0:2] + '-' + mac[2:4] + '-' + mac[4:6] + '-' + mac[6:8] + '-' + mac[8:10] + '-' + mac[10:12],
'\n','Dot Notation: ', mac[0:4] + '.' + mac[4:8] + '.' + mac[8:12])
with open('oui.txt', 'r') as start:
    for line in start:
        if line.count(text) == 1:
            _,_,_,*last = line.split()
            last = ' '.join(last)
            print('\n',last,'\n')
            break

"""
09:38 $ ./find_mac.py 00:25:22:32:3d:3e

 Hexadecimal:  00:25:22:32:3D:3E 
 Bit-reversed:  00-25-22-32-3D-3E 
 Dot Notation:  0025.2232.3D3E

 ASRock Incorporation 

"""