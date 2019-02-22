#!/usr/bin/env python3
"""
Задание 9.1a
Сделать копию скрипта задания 9.1.

Дополнить скрипт:

ввести дополнительный параметр, который контролирует будет ли настроен port-security
имя параметра 'psecurity'
по умолчанию значение False
Проверить работу функции на примере словаря access_dict, с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_access_config(access):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17 }

    psecurity - контролирует нужна ли настройка Port Security. По умолчанию значение False
        - если значение True, то настройка выполняется с добавлением шаблона port_security
        - если значение False, то настройка не выполняется

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
    '''

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
"""
def generate_access_config(access, psecurity=False):
    lists = []
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                 'switchport port-security violation restrict',
                 'switchport port-security']
    for inter, vlan in access.items():
        lists.append('interface {}'.format(inter))
        for template in access_template:
            if template.endswith('access vlan'):
                lists.append(template + ' {}'.format(vlan))
            else:
                lists.append(template)
        for sec in port_security:
            if psecurity:
                lists.append(sec)
    return lists

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
lists = generate_access_config(access_dict)
print(lists)
"""
  Переменная по-умолчанию False:
In [49]: generate_access_config(access_dict)                                                                         
['interface FastEthernet0/12', 'switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/14', 'switchport mode access', 'switchport access vlan 11', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/16', 'switchport mode access', 'switchport access vlan 17', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'interface FastEthernet0/17', 'switchport mode access', 'switchport access vlan 150', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
Out[49]: 
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

  Переменная с True:
In [50]: generate_access_config(access_dict, psecurity=True)                                                         
['interface FastEthernet0/12', 'switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security', 'interface FastEthernet0/14', 'switchport mode access', 'switchport access vlan 11', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security', 'interface FastEthernet0/16', 'switchport mode access', 'switchport access vlan 17', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security', 'interface FastEthernet0/17', 'switchport mode access', 'switchport access vlan 150', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security']
Out[50]: 
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'switchport port-security maximum 2',
 'switchport port-security violation restrict',
 'switchport port-security',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'switchport port-security maximum 2',
 'switchport port-security violation restrict',
 'switchport port-security',
 'interface FastEthernet0/16',
 'switchport mode access',
 'switchport access vlan 17',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'switchport port-security maximum 2',
 'switchport port-security violation restrict',
 'switchport port-security',
 'interface FastEthernet0/17',
 'switchport mode access',
 'switchport access vlan 150',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'switchport port-security maximum 2',
 'switchport port-security violation restrict',
 'switchport port-security']
"""