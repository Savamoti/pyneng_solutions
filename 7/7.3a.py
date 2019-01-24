#!/usr/bin/env python3
"""
Задание 7.3a
Сделать копию скрипта задания 7.3

Дополнить скрипт:

Отсортировать вывод по номеру VLAN
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
with open('CAM_table.txt', 'r') as start:
    lists = [] 
    for line in start: 
        if line.count('.') is 2: 
            a = line.strip('\n').split() 
            a.pop(-2) 
            lists.append(a) 
    lists.sort()
    for l in lists:
        print(l[0] + '    ' + l[1] + '   ' + l[2])
"""
09:26 $ ./7.3.py 
100    01bb.c580.7000   Gi0/1
200    0a4b.c380.7000   Gi0/2
300    a2ab.c5a0.7000   Gi0/3
100    0a1b.1c80.7000   Gi0/4
500    02b1.3c80.7000   Gi0/5
200    1a4b.c580.7000   Gi0/6
300    0a1b.5c80.7000   Gi0/7
"""