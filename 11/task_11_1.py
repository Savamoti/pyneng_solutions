#!/usr/bin/env python3
"""Задание 11.1
Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors.
Функция ожидает, как аргумент, вывод команды одной строкой (а не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.
Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0
Функция должна вернуть такой словарь:
{('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
 ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def parse_cdp_neighbors(show):
    with open(show) as file:
        show = file.read()
        q = {}
        show = show.split('\n')
        for line in show:
            main = []
            second = []
            if line.find('>') != -1:
                main_machine = line[:line.find('>')]
            elif line.find('Eth') != -1:
                second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                main.append(main_machine)
                second.append(second_machine)
                main_interface = main_eth + main_inter
                second_interface = second_eth + second_inter
                main.append(main_interface)
                second.append(second_interface)
                main_tuple = tuple(main)
                second_tuple = tuple(second)
                q[main_tuple] = second_tuple
    return q
if __name__ == "__main__":
    q = parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')
    print(q)

"""
13:04 $ ./task_11_1.py 
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'), ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'), ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
"""