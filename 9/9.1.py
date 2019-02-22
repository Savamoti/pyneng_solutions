#!/usr/bin/env python3
"""
Задание 9.1
Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает, как аргумент, словарь access-портов, вида:

{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17,
 'FastEthernet0/17':150}
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_template.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]
Проверить работу функции на примере словаря access_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access
    с конфигурацией на основе шаблона
    '''
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']


access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
"""
def generate_access_config(access):
    lists = []
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))
        for template in access_template:
            if template.endswith('access vlan'):
                lists.append(template + ' {}'.format(vlan))
            else:
                lists.append(template)
    return lists

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
lists = generate_access_config(access_dict)
print(lists)
"""
In [54]: generate_access_config(access_dict)                                                                         
['interface FastEthernet0/12', 'switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/14', 'switchport mode access', 'switchport access vlan 11', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/16', 'switchport mode access', 'switchport access vlan 17', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/17', 'switchport mode access', 'switchport access vlan 150', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
Out[54]: 
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/16',
 'switchport mode access',
 'switchport access vlan 17',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/17',
 'switchport mode access',
 'switchport access vlan 150',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable']
"""
