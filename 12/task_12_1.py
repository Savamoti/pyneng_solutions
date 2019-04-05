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
import multiprocessing
from multiprocessing import Process

def check_ip_addresse(ip, queues):
    """
    Function requires IP and class Queue. Ping IP and put result in queues object.
    """
    command = subprocess.run('ping -c 3 {}'.format(ip), shell=True, stdout=subprocess.DEVNULL)
    if command.returncode == 0:
        print('Yeah,', ip, 'is alive.')
        status = True
    else:
        print('Oh noo,', ip, 'is dead.')
        status = False
    queues.put((status, ip))
def ping_ip_list(ip_list):
    """
    Function requires list of strings like IP.
    """
    queues = multiprocessing.Queue()
    procs = []
    result = {True:[], False:[]}

    for ip in ip_list:
        p = Process(target=check_ip_addresse, args=(ip, queues))
        procs.append(p)
        p.start()

    for p in procs:
        p.join()

    for p in procs:
        key, value = queues.get()
        result[key].append(value)
    return result
if __name__ == '__main__':
    ip_lists = ['192.168.1.1', '192.168.1.100', '8.8.8.8', '1.1.1.1']
    print(ping_ip_list(ip_lists))

"""
21:31 $ ./task_12_1.py
Yeah, 192.168.1.1 is alive.
Yeah, 8.8.8.8 is alive.
Yeah, 1.1.1.1 is alive.
Oh noo, 192.168.1.100 is dead.
{True: ['192.168.1.1', '8.8.8.8', '1.1.1.1'], False: ['192.168.1.100']}
 """