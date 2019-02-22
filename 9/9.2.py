#!/usr/bin/env python3
"""
Задание 9.2
Создать функцию, которая генерирует конфигурацию для trunk-портов.

Параметр trunk - это словарь trunk-портов.

Словарь trunk имеет такой формат (тестовый словарь trunk_dict уже создан):

{ 'FastEthernet0/1':[10,20],
  'FastEthernet0/2':[11,30],
  'FastEthernet0/4':[17] }
Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_template.

В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов для которых необходимо сгенерировать конфигурацию.

    Возвращает список всех команд, которые были сгенерированы на основе шаблона
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
    lists = []
    trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk native vlan 999',
                  'switchport trunk allowed vlan'] 
    for inter, vlan in trunk.items():  
        lists.append('interface {}'.format(inter))
        for template in trunk_template:
          if template.endswith('allowed vlan'):
              vlan = [str(num) for num in vlan]
              vlan = ','.join(vlan)
              lists.append(template + ' {}'.format(vlan))
          else:
              lists.append(template)
    print(lists)
    return lists

trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

generate_trunk_config(trunk_dict)
"""
In [8]: generate_trunk_config(trunk_dict)
['interface FastEthernet0/1', 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 10,20,30', 'interface FastEthernet0/2', 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 11,30', 'interface FastEthernet0/4', 'switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk native vlan 999', 'switchport trunk allowed vlan 17']
Out[8]:
['interface FastEthernet0/1',
 'switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 10,20,30',
 'interface FastEthernet0/2',
 'switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 11,30',
 'interface FastEthernet0/4',
 'switchport trunk encapsulation dot1q',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 17']
 """