#!/usr/bin/env python3
"""
Задание 7.2c
Переделать скрипт из задания 7.2b:

передавать как аргументы скрипту:
имя исходного файла конфигурации
имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации, в которых содержатся слова из списка ignore. И затем записать оставшиеся строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
"""
from sys import argv
text = argv[1:]
a = text[0]
b = text[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(a, 'r') as start, open(b, 'a') as end:
    for line in start:
        if line.find(ignore[0]) is -1 and line.find(ignore[1]) is -1 and line.find(ignore[2]) is -1:
            end.write(line)

"""
11:27 $ ./7.2c.py config_sw1.txt end.txt
11:27 $ cat end.txt 

!
! Last configuration change at 13:11:59 UTC Thu Feb 25 2016
!
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname sw1
!
!
!
!
! 
!
!
!
!
!
!
interface Ethernet0/0
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
!
interface Ethernet0/2
!         
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
!         
interface Ethernet1/0
!
interface Ethernet1/1
!
interface Ethernet1/2
!
interface Ethernet1/3
!
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
!
!
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all
!
"""