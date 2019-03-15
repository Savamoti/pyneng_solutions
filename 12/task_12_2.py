#!/usr/bin/env python3
"""
Задание 12.2
Функция check_ip_addresses из задания 12.1 принимает только список адресов, но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.
Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.
Функция ожидает как аргумент список IP-адресов.
IP-адреса могут быть в формате:
10.1.1.1
10.1.1.1-10.1.1.10
10.1.1.1-10
Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазона включая последний.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
Функция возвращает два списка:
список доступных IP-адресов
список недоступных IP-адресов
Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1.
"""
import subprocess
import argparse
from task_12_1 import check_ip_addresses
import ipaddress

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

if __name__ == "__main__":
    #parser
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('ip_list', action='store', help='Enter ip-address-list just like: 192.168.1.1-10 or 192.168.1.1-192.168.1.10 or 192.168.1.1')
    args = parser.parse_args()
    yes = []
    no = []

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
    print('Available address list: ',yes)
    print('Unavailable address list: ', no)
"""
17:56 $ ./task_12_2.py 192.168.1.1-3
I'm ping 192.168.1.1 right now, wait.
I'm ping 192.168.1.2 right now, wait.
I'm ping 192.168.1.3 right now, wait.
Available address list:  [IPv4Address('192.168.1.1')]
Unavailable address list:  [IPv4Address('192.168.1.2'), IPv4Address('192.168.1.3')]
"""