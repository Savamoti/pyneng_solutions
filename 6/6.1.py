#!/usr/bin/env python3

"""
Задание 6.1
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1.
Определить какому классу принадлежит IP-адрес.
В зависимости от класса адреса, вывести на стандартный поток вывода:
'unicast' - если IP-адрес принадлежит классу A, B или C
'multicast' - если IP-адрес принадлежит классу D
'local broadcast' - если IP-адрес равен 255.255.255.255
'unassigned' - если IP-адрес равен 0.0.0.0
'unused' - во всех остальных случаях
Подсказка по классам (диапазон значений первого байта в десятичном формате):

A: 1-127
B: 128-191
C: 192-223
D: 224-239
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес(например 10.0.1.1): ')
ip = ip.strip().split('.')
oktet1 = int(ip[0])
oktet2 = int(ip[1])
oktet3 = int(ip[2])
oktet4 = int(ip[3])

unicast = list(range(1, 224))
multicast = list(range(224, 240))
broadcast = [255,255,255,255]
unassigned = [0,0,0,0]

if oktet1 in unicast:
    print('This is unicast IP')
elif oktet1 in multicast:
    print('This is multicast')
elif oktet1 in broadcast and oktet2 in broadcast and oktet3 in broadcast and oktet4 in broadcast:
    print('This is broadcast IP')
elif oktet1  in unassigned and oktet2 in unassigned and oktet3 in unassigned and oktet4 in unassigned:
    print('This is unassigned IP')
else:
    print('This is unused IP')

"""
12:14 $ ./6.1.py 
Введите IP-адрес(например 10.0.1.1): 192.168.0.1
This is unicast IP
12:14 $ ./6.1.py 
Введите IP-адрес(например 10.0.1.1): 239.0.0.0
This is multicast
12:14 $ ./6.1.py 
Введите IP-адрес(например 10.0.1.1): 255.255.255.255
This is broadcast IP
12:14 $ ./6.1.py 
Введите IP-адрес(например 10.0.1.1): 0.0.0.0
This is unassigned IP
12:14 $ ./6.1.py 
Введите IP-адрес(например 10.0.1.1): 0.255.255.255
This is unused IP
"""
