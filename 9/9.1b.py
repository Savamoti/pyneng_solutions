#!/usr/bin/env python3
"""
Задание 9.1b
Сделать копию скрипта задания 9.1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:

ключи: имена интерфейсов, вида 'FastEthernet0/12'
значения: список команд, который надо выполнить на этом интерфейсе:
    ['switchport mode access',
     'switchport access vlan 10',
     'switchport nonegotiate',
     'spanning-tree portfast',
     'spanning-tree bpduguard enable']
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

    Функция возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
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
    access_template = ['switchport mode access',
                   'switchport access vlan',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    finish = {}
    for inter, vlan in access.items():
        finish[inter]=[]
        for config in access_template:
            if config.endswith('access vlan'):
                finish[inter].append(config + ' {}'.format(vlan))
            else:
                finish[inter].append(config)
        for security in port_security:
            if psecurity:
                finish[inter].append(security)
    print(finish)
    return finish

access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }
                
generate_access_config(access_dict, psecurity=True)

"""
    psecurity по-умолчанию False
In [5]: generate_access_config(access_dict)
{'FastEthernet0/12': ['switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable'], 'FastEthernet0/14': ['switchport mode access', 'switchport access vlan 11', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable'], 'FastEthernet0/16': ['switchport mode access', 'switchport access vlan 17', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable'], 'FastEthernet0/17': ['switchport mode access', 'switchport access vlan 150', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']}
Out[5]:
{'FastEthernet0/12': ['switchport mode access',
  'switchport access vlan 10',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable'],
 'FastEthernet0/14': ['switchport mode access',
  'switchport access vlan 11',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable'],
 'FastEthernet0/16': ['switchport mode access',
  'switchport access vlan 17',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable'],
 'FastEthernet0/17': ['switchport mode access',
  'switchport access vlan 150',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable']}

    psecurity True
In [6]: generate_access_config(access_dict, psecurity=True)
{'FastEthernet0/12': ['switchport mode access', 'switchport access vlan 10', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security'], 'FastEthernet0/14': ['switchport mode access', 'switchport access vlan 11', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security'], 'FastEthernet0/16': ['switchport mode access', 'switchport access vlan 17', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security'], 'FastEthernet0/17': ['switchport mode access', 'switchport access vlan 150', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable', 'switchport port-security maximum 2', 'switchport port-security violation restrict', 'switchport port-security']}
Out[6]:
{'FastEthernet0/12': ['switchport mode access',
  'switchport access vlan 10',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable',
  'switchport port-security maximum 2',
  'switchport port-security violation restrict',
  'switchport port-security'],
 'FastEthernet0/14': ['switchport mode access',
  'switchport access vlan 11',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable',
  'switchport port-security maximum 2',
  'switchport port-security violation restrict',
  'switchport port-security'],
 'FastEthernet0/16': ['switchport mode access',
  'switchport access vlan 17',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable',
  'switchport port-security maximum 2',
  'switchport port-security violation restrict',
  'switchport port-security'],
 'FastEthernet0/17': ['switchport mode access',
  'switchport access vlan 150',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable',
  'switchport port-security maximum 2',
  'switchport port-security violation restrict',
  'switchport port-security']}

"""