#!/usr/bin/env python3

"""
Задание 5.3a
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:

для access: 'Enter VLAN number:'
для trunk: 'Enter allowed VLANs:'
Ограничение: Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if и циклов for/while.

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

mode = mode.count('trunk')

modes = [
['Enter VLAN number:'],
['Enter allowed VLANs:']
]

vlans = input (' '.join(modes[mode]))

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

print('\n' * 2)
print('interface {}'.format(interface))
print('\n'.join(config_template[mode]).format(vlans))

"""
./5.3a.py 
Enter interface mode (access/trunk ):access
Enter interface type and number:Fa0/1
Enter VLAN number:99



interface Fa0/1
switchport mode access
switchport access vlan 99
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable


./5.3a.py 
Enter interface mode (access/trunk ):trunk
Enter interface type and number:Fa0/2
Enter allowed VLANs:199-201



interface Fa0/2
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 199-201

"""
