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
import subprocess
import argparse
from task_12_1 import check_ip_addresses
import ipaddress
from tabulate import tabulate

def count_integer(a, b):
    """
    This function counts the number of objects between variables a and b.
    """
    x = 0
    status = True
    while status:
        if a == b:
            x = x + 1
            status = False
        else:
            a = a + 1
            x = x + 1
    return x

def print_with_tabulate(yes, no):
    """
    Function requires two list, print them with tabulate.
    """
    dic = {}
    dic['Reachable'] = yes
    dic['Unreachable'] = no
    print(tabulate(dic, headers = 'keys'))

if __name__ == "__main__":
    #parser
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('ip_list', action='store', help='Enter ip-address-list just like: 192.168.1.1-10 or 192.168.1.1-192.168.1.10 or 192.168.1.1')
    args = parser.parse_args()
    yes = []
    no = []
    columns = ['Reachable', 'Unreachable']
    if '-' in args.ip_list:
        lists1, lists2 = args.ip_list.split('-')
        lis1 = int(lists1.split('.')[-1])
        lis2 = int(lists2.split('.')[-1])
        start = ipaddress.ip_address(lists1)
        x = count_integer(lis1, lis2)
        for line in range(x):
            status = check_ip_addresses(start)
            if status:
                yes.append(start)
                start = start + 1
            else:
                no.append(start)
                start = start + 1
    else:
        status = check_ip_addresses(args.ip_list)
        start = ipaddress.ip_address(args.ip_list)
        if status:
            yes.append(start)
        else:
            no.append(start)
    print_with_tabulate(yes, no)
"""
17:58 $ ./task_12_3.py 192.168.1.1-3
I'm ping 192.168.1.1 right now, wait.
I'm ping 192.168.1.2 right now, wait.
I'm ping 192.168.1.3 right now, wait.
Reachable    Unreachable
-----------  -------------
192.168.1.1  192.168.1.2
             192.168.1.3
"""