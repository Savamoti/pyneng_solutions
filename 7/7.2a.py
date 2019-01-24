#!/usr/bin/env python3
"""
Задание 7.2a
Сделать копию скрипта задания 7.2.

Дополнить скрипт:

Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
"""
from sys import argv
text = argv[1:]
text = ''.join(text)
ignore = ['duplex', 'alias', 'Current configuration', '!']
with open(text, 'r') as file:
    for line in file:
        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1 and line.find(ignore[3]) is -1:
            print(line.strip('\n'))

"""
11:24 $ ./7.2a.py config_sw1.txt

version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet0/2
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet1/0
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all
end
"""