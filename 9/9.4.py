#!/usr/bin/env python3
"""
Задание 9.4
Создать функцию, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы вначале можно оставлять).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!', а также строки в которых содержатся слова из списка ignore.
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.
Ограничение: Все задания надо выполнять используя только пройденные темы.
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)
"""
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    return any(word in command for word in ignore)
def get_config(config):
    config_dict = {}
    with open(config, 'r') as file:
        for line in file:
            if ignore_command(line, ignore) or line.find('!') != -1:
                continue
            else:
                if line.startswith(' '):
                    slave = line.strip()
                    config_dict[main].append(slave)
                else:
                    main = line.strip()
                    config_dict[main] = []
    return config_dict
all = get_config('config_sw1.txt')
"""
In [101]: all                                                                                                        
Out[101]: 
{'version 15.0': [],
 'service timestamps debug datetime msec': [],
 'service timestamps log datetime msec': [],
 'no service password-encryption': [],
 'hostname sw1': [],
 'interface FastEthernet0/0': ['switchport mode access',
  'switchport access vlan 10'],
 'interface FastEthernet0/1': ['switchport trunk encapsulation dot1q',
  'switchport trunk allowed vlan 100,200',
  'switchport mode trunk'],
 'interface FastEthernet0/2': ['switchport mode access',
  'switchport access vlan 20'],
 'interface FastEthernet0/3': ['switchport trunk encapsulation dot1q',
  'switchport trunk allowed vlan 100,300',
  'switchport mode trunk'],
 'interface FastEthernet1/0': ['switchport mode access',
  'switchport access vlan 20'],
 'interface FastEthernet1/1': ['switchport mode access',
  'switchport access vlan 30'],
 'interface FastEthernet1/2': ['switchport trunk encapsulation dot1q',
  'switchport trunk allowed vlan 400,500',
  'switchport mode trunk'],
 'interface FastEthernet1/3': [],
 'interface Vlan100': ['ip address 10.0.100.1 255.255.255.0'],
 'line con 0': ['exec-timeout 0 0',
  'privilege level 15',
  'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all'],
 'end': []}
"""
"""
Не внимательно прочитал задание, не заметив уже готовую функцию ignore_command, начал лепить свою функцию:
ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
    for ig in ignore:
        if command.find(ig) != -1 or command.find('!') != -1:
            status = True
            break
        else:
            status = False
    return status
"""