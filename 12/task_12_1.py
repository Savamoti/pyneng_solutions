#!/usr/bin/env python3
"""
Задание 12.1
Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.
Функция ожидает как аргумент список IP-адресов. И возвращает два списка:
список доступных IP-адресов
список недоступных IP-адресов
Для проверки доступности IP-адреса, используйте ping. Адрес считается доступным, если на три ICMP-запроса пришли три ответа.
"""
import subprocess
import argparse

def check_ip_addresses(ip):
    """
    Ping IP and return status (True == returncoode 0 or False == returncode 1)
    """
    print("I'm ping {} right now, wait.".format(ip))
    status = subprocess.run('ping -c 3 {}'.format(ip), shell=True, stdout=subprocess.DEVNULL)
    if status.returncode == 0:
        return True
    else:
        return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Ping script')

    parser.add_argument('spisok', action='store', help='Put there name of ip list file')
    args = parser.parse_args()
    yes = []
    no = []
    with open(args.spisok) as file:
        for line in file:
            line = line.strip()
            if check_ip_addresses(line) == True:
                yes.append(line)
            else:
                no.append(line)
    print('Available address list: ',yes)
    print('Unavailable address list: ', no)
"""
17:54 $ ./task_12_1.py ip-list.txt 
I'm ping 8.8.8.8 right now, wait.
I'm ping 192.168.1.190 right now, wait.
I'm ping 8.8.4.4 right now, wait.
I'm ping 1.1.1.1 right now, wait.
I'm ping 192.168.1.191 right now, wait.
I'm ping 192.168.1.192 right now, wait.
Available address list:  ['8.8.8.8', '8.8.4.4', '1.1.1.1']
Unavailable address list:  ['192.168.1.190', '192.168.1.191', '192.168.1.192']
"""