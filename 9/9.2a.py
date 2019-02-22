#!/usr/bin/env python3
"""
Задание 9.2a
Сделать копию скрипта задания 9.2
Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
ключи: имена интерфейсов, вида 'FastEthernet0/1'
значения: список команд, который надо выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_dict.
Ограничение: Все задания надо выполнять используя только пройденные темы.
def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }
"""
def generate_trunk_config(trunk):
    trunk_template = ['switchport trunk encapsulation dot1q',
              'switchport mode trunk',
              'switchport trunk native vlan 999',
              'switchport trunk allowed vlan'] 
    dicall = {}
    for inter, vlan in trunk.items():
        dicall[inter] = []
        for template in trunk_template:
            if template.endswith('allowed vlan'):
                vlan = [str(num) for num in vlan]
                vlan = ','.join(vlan)
                dicall[inter].append(template + ' {}'.format(vlan))
            else:
                dicall[inter].append(template)
    print(dicall)
    return(dicall)
trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_dict)
"""
In [2]: generate_trunk_config(trunk_dict)                                                                            
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 10,20,30'], 'FastEthernet0/2': ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 11,30'], 'FastEthernet0/4': ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 17']}
Out[2]: 
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
  'switchport mode trunk',
  'switchport trunk native vlan 999',
  'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport trunk encapsulation dot1q',
  'switchport mode trunk',
  'switchport trunk native vlan 999',
  'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport trunk encapsulation dot1q',
  'switchport mode trunk',
  'switchport trunk native vlan 999',
  'switchport trunk allowed vlan 17']}
"""