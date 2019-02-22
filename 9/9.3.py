#!/usr/bin/env python3
"""Задание 9.3
Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает два объекта:
словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}
словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
 {'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17]}
Функция ожидает в качестве аргумента имя конфигурационного файла.
Проверить работу функции на примере файла config_sw1.txt
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config):
    with open(config, 'r') as file:
            access_config = {}
            trunk_config = {}
            for line in file:
                if line.find('FastEthernet') != -1:
                    interface = line.split()[-1]
                elif line.find('access vlan') != -1:
                    access_vlan = line.split()[-1]
                    access_config[interface] = access_vlan
                elif line.find('trunk allowed vlan') != -1:
                    trunk_vlan = line.split()[-1]
                    trunk_config[interface] = trunk_vlan
                else:
                    pass
            print('access interfaces: \n', access_config)
            print('trunk interfaces: \n', trunk_config)
    return access_config, trunk_config
get_int_vlan_map('config_sw1.txt')
"""
In [49]: get_int_vlan_map('config_sw1.txt')                                                                          
access interfaces: 
 {'FastEthernet0/0': '10', 'FastEthernet0/2': '20', 'FastEthernet1/0': '20', 'FastEthernet1/1': '30'}
trunk interfaces: 
 {'FastEthernet0/1': '100,200', 'FastEthernet0/3': '100,300', 'FastEthernet1/2': '400,500'}
Out[49]: 
({'FastEthernet0/0': '10',
  'FastEthernet0/2': '20',
  'FastEthernet1/0': '20',
  'FastEthernet1/1': '30'},
 {'FastEthernet0/1': '100,200',
  'FastEthernet0/3': '100,300',
  'FastEthernet1/2': '400,500'})

In [50]: access_config                                                                                               
Out[50]: 
{'FastEthernet0/0': '10',
 'FastEthernet0/2': '20',
 'FastEthernet1/0': '20',
 'FastEthernet1/1': '30'}

In [51]: trunk_config                                                                                                
Out[51]: 
{'FastEthernet0/1': '100,200',
 'FastEthernet0/3': '100,300',
 'FastEthernet1/2': '400,500'}
"""