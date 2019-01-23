#!/usr/bin/env python3

"""
Задание 6.1a
Сделать копию скрипта задания 6.1.

Дополнить скрипт:

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
состоит из 4 чисел разделенных точкой,
каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение:

'Incorrect IPv4 address'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес(например 10.0.1.1): ')
znak = ip.count('.')
if znak != 3:
    print('Incorrect IPv4 address, add 3 dots between')
else:
    "проверка на наличие цифр в октетах"
    ip = ip.strip().split('.')
    int1 = ip[0].isdigit()
    int2 = ip[1].isdigit()
    int3 = ip[2].isdigit()
    int4 = ip[3].isdigit()
    if int1 is not True and int2 is not True and int3 is not True and int4 is not True:
        print('Incorrect IPv4 address, use only numbers')
    else:
        "проверка на разрешённый диапазон цифр(0-255) в октетах"
        oktet1 = int(ip[0])
        oktet2 = int(ip[1])
        oktet3 = int(ip[2])
        oktet4 = int(ip[3])
        allowed_range = list(range(0, 256))
        if oktet1 not in allowed_range or oktet2 not in allowed_range or oktet3 not in allowed_range or oktet4 not in allowed_range:
            print('Incorrect IPv4 address, allowed only 0-255 range')
        else:
            "ну и основная проверка, на тип IP-адреса"
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
11:31 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): fsdkfhsdiufhsdiufh
Incorrect IPv4 address, add 3 dots between
11:31 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): sdfsdf.sdfsdfsdfsd.df.sdfsdf
Incorrect IPv4 address, use only numbers
11:32 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): sdfsdfsdfsdfsdf...
Incorrect IPv4 address, use only numbers
11:32 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): 234234234.234.235236236.234.1
Incorrect IPv4 address, add 3 dots between
11:33 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): 300.5000.6234235.15
Incorrect IPv4 address, allowed only 0-255 range
11:33 $ ./6.1a.py 
Введите IP-адрес(например 10.0.1.1): 192.168.1.1
This is unicast IP
"""