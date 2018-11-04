#!/usr/bin/env python3

"""
Задание 5.3
Скрипт должен запрашивать у пользователя:

информацию о режиме интерфейса (access/trunk),
пример текста запроса: 'Enter interface mode (access/trunk): '
номере интерфейса (тип и номер, вида Gi0/3)
пример текста запроса: 'Enter interface type and number: '
номер VLANа (для режима trunk будет вводиться список VLANов)
пример текста запроса: 'Enter vlan(s): '
В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться соответствующая конфигурация access или trunk (шаблоны команд находятся в списках access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if и циклов for/while.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_3.py
Enter interface mode (access/trunk): access
Enter interface type and number: Fa0/6
Enter vlan(s): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
Пример выполнения скрипта, при выборе режима trunk:

$ python task_5_3.py
Enter interface mode (access/trunk): trunk
Enter interface type and number: Fa0/7
Enter vlan(s): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
Начальное содержимое скрипта:

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']
"""

mode = input('Enter interface mode (access/trunk ):')
interface = input('Enter interface type and number:')
vlans = input ('Enter vlans(s):')

config_template = [
['switchport mode access',
 'switchport access vlan {}',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable'],
['switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk allowed vlan {}']
]

mode = mode.count('trunk')

print('\n' * 2)
print('interface {}'.format(interface))
print('\n'.join(config_template[mode]).format(vlans))

"""
./5.3.py 
Enter interface mode (access/trunk ):trunk
Enter interface type and number:Gi0/1
Enter vlans(s):100



interface Gi0/1
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 100




./5.3.py 
Enter interface mode (access/trunk ):access
Enter interface type and number:Gi0/2
Enter vlans(s):200



interface Gi0/2
switchport mode access
switchport access vlan 200
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""
