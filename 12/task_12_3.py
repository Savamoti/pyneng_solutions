#!/usr/bin/env python3
"""
Задание 12.3
Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:

список доступных IP-адресов

список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
Функция не должна изменять списки, которые передавны ей как аргументы. То есть, до выполнения функции и после списки должны выглядеть одинаково.

"""
from tabulate import tabulate

#create two lists
yes = ['192.168.1.{}'.format(i) for i in range(1,10)]
no = ['192.168.9.{}'.format(i) for i in range(1,5)]
def ip_table(list1, list2):
    """
    The function requires two lists, and print them with tabulate
    """
    q = {'Available': [], 'Unavailable': []}
    for i in yes:
        q['Available'].append(i)
    for i in no:
        q['Unavailable'].append(i)
    print(tabulate(q, headers='keys'))

ip_table(yes, no)

"""
22:23 $ ./task_12_3.py
Available    Unavailable
-----------  -------------
192.168.1.1  192.168.9.1
192.168.1.2  192.168.9.2
192.168.1.3  192.168.9.3
192.168.1.4  192.168.9.4
192.168.1.5
192.168.1.6
192.168.1.7
192.168.1.8
192.168.1.9
"""