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
import multiprocessing
from multiprocessing import Process
from task_12_1 import check_ip_addresse
from task_12_1 import ping_ip_list


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

    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument('ip', action='store', help='Enter ip-address-list just like: 192.168.1.1-10 or 192.168.1.1-192.168.1.10 or 192.168.1.1')
    args = parser.parse_args()

    ip_list = []
    if '-' in args.ip:
        ip_str, ip_str2 = args.ip.split('-')
        last_oktet = int(ip_str.split('.')[-1])
        last_oktet2 = int(ip_str2.split('.')[-1])
        x = count_integer(last_oktet, last_oktet2)
        ip_str = ip_str.split('.')
        ip_int = [int(i) for i in ip_str]

        for i in range(x):
            ip_str = [str(i) for i in ip_int]
            ip_str = '.'.join(ip_str)
            ip_list.append(ip_str)
            ip_int[-1] = ip_int[-1] + 1

        print(ping_ip_list(ip_list))
    else:
        result = {True: [], False: []}
        command = subprocess.run('ping -c 3 {}'.format(args.ip), shell=True, stdout=subprocess.DEVNULL)
        if command.returncode == 0:
            print('Yeah,', args.ip, 'is alive')
            result[True].append()
        else:
            print('Oh noo,'. args.ip, 'is dead')

"""
21:53 $ ./task_12_2.py 192.168.1.100-120
Yeah, 192.168.1.101 is alive.
Yeah, 192.168.1.105 is alive.
Oh noo, 192.168.1.102 is dead.
Oh noo, 192.168.1.100 is dead.
Oh noo, 192.168.1.104 is dead.
Oh noo, 192.168.1.108 is dead.
Oh noo, 192.168.1.107 is dead.
Oh noo, 192.168.1.106 is dead.
Oh noo, 192.168.1.103 is dead.
Oh noo, 192.168.1.109 is dead.
Oh noo, 192.168.1.114 is dead.
Oh noo, 192.168.1.110 is dead.
Oh noo, 192.168.1.111 is dead.
Oh noo, 192.168.1.112 is dead.
Oh noo, 192.168.1.113 is dead.
Oh noo, 192.168.1.115 is dead.
Oh noo, 192.168.1.118 is dead.
Oh noo, 192.168.1.120 is dead.
Oh noo, 192.168.1.116 is dead.
Oh noo, 192.168.1.117 is dead.
Oh noo, 192.168.1.119 is dead.
{True: ['192.168.1.101', '192.168.1.105'], False: ['192.168.1.102', '192.168.1.109', '192.168.1.104', '192.168.1.108', '192.168.1.106', '192.168.1.107', '192.168.1.103', '192.168.1.100', '192.168.1.112', '192.168.1.113', '192.168.1.114', '192.168.1.110', '192.168.1.111', '192.168.1.117', '192.168.1.118', '192.168.1.119', '192.168.1.116', '192.168.1.115', '192.168.1.120']}
 """