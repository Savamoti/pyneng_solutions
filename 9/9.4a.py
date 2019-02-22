#!/usr/bin/env python3
"""
Задание 9.4a
Задача такая же, как и задании 9.4. Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл. В нём есть разделы с большей вложенностью, например, разделы:

interface Ethernet0/3.100

router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности. При этом, не привязываясь к конкретным разделам. Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:

то команды верхнего уровня будут ключами словаря,

а команды подуровней - списками

Если уровня вложенности три:

самый вложенный уровень должен быть списком,

а остальные - словарями.

На примере interface Ethernet0/3.100

{'interface Ethernet0/3.100':{
                    'encapsulation dot1Q 100':[],
                    'xconnect 10.2.2.2 12100 encapsulation mpls':
                        ['backup peer 10.4.4.4 14100',
                         'backup delay 1 1']}}
Ограничение: Все задания надо выполнять используя только пройденные темы.

ignore = ['duplex', 'alias', 'Current configuration']
​
def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
​
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
​
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
​
    '''
    return any(word in command for word in ignore)
"""
ignore = ['duplex', 'alias', 'Current configuration']
def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
​
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
​
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
​
    '''
    return any(word in command for word in ignore)
def get_config(config): 
    config_dict = {}
    lvl_dict = {}
    lvl1_list = []
    fell = None
    with open(config, 'r') as file: 
        for line in file: 
            value = [] 
            if check_ignore(line, ignore) or line.find('!') != -1: 
                continue 
            else: 
                if line[0] == ' ' and line[1] != ' ':
                    lvl1 = line.strip()
                    lvl1_list.append(lvl1)
                    config_dict[main].append(lvl1)
                elif line[0] == ' ' and line[1] == ' ':
                    lvl2 = line.strip()
                    if fel == None:
                        for i in lvl1_list:
                            lvl_dict[i] = []
                        config_dict[main] = lvl_dict
                    config_dict[main][lvl1].append(lvl2)
                    fel = 'blackhall'
                else: 
                    main = line.strip() 
                    config_dict[main] = value
                    fel = None
                    lvl1_list = []
                    lvl_dict = {}
    return config_dict 
 
all = get_config('config_r1.txt')
print(all)
"""
14:38 $ ./9.4a.py 
{'version 15.2': [], 'no service timestamps debug uptime': [], 'no service timestamps log uptime': [], 'no service password-encryption': [], 'hostname PE_r1': [], 'boot-start-marker': [], 'boot-end-marker': [], 'logging buffered 50000': [], 'no aaa new-model': [], 'mmi polling-interval 60': [], 'no mmi auto-configure': [], 'no mmi pvc': [], 'mmi snmp-timeout 180': [], 'ip auth-proxy max-login-attempts 5': [], 'ip admission max-login-attempts 5': [], 'no ip domain lookup': [], 'ip cef': [], 'no ipv6 cef': [], 'multilink bundle-name authenticated': [], 'mpls label range 1000 1999': [], 'mpls label protocol ldp': [], 'mpls ldp explicit-null': [], 'mpls ldp discovery targeted-hello accept': [], 'mpls traffic-eng tunnels': [], 'xconnect logging redundancy': [], 'interface Loopback0': ['ip address 10.1.1.1 255.255.255.255'], 'interface Tunnel0': ['ip unnumbered Loopback0', 'tunnel mode mpls traffic-eng', 'tunnel destination 10.2.2.2', 'tunnel mpls traffic-eng priority 7 7', 'tunnel mpls traffic-eng bandwidth 5000', 'tunnel mpls traffic-eng path-option 10 dynamic', 'no routing dynamic'], 'interface Ethernet0/0': ['description To PE_r3 Ethernet0/0', 'bandwidth 100000', 'ip address 10.0.13.1 255.255.255.0', 'mpls traffic-eng tunnels', 'ip rsvp bandwidth 100000 10000'], 'interface Ethernet0/1': ['no ip address'], 'interface Ethernet0/2': ['description To P_r9 Ethernet0/2', 'ip address 10.0.19.1 255.255.255.0', 'mpls traffic-eng tunnels', 'ip rsvp bandwidth'], 'interface Ethernet0/3': ['description To sw1 Ethernet0/3', 'no ip address'], 'interface Ethernet0/3.100': {'encapsulation dot1Q 100': [], 'xconnect 10.2.2.2 12100 encapsulation mpls': ['backup peer 10.4.4.4 14100', 'backup delay 1 1']}, 'interface Ethernet1/0': ['no ip address', 'shutdown'], 'router ospf 1': ['mpls ldp autoconfig area 0', 'mpls traffic-eng router-id Loopback0', 'mpls traffic-eng area 0', 'network 10.0.0.0 0.255.255.255 area 0'], 'router bgp 100': {'bgp log-neighbor-changes': [], 'bgp bestpath igp-metric ignore': [], 'neighbor 10.2.2.2 remote-as 100': [], 'neighbor 10.2.2.2 update-source Loopback0': [], 'neighbor 10.2.2.2 next-hop-self': [], 'neighbor 10.4.4.4 remote-as 40': [], 'address-family vpnv4': ['neighbor 10.2.2.2 activate', 'neighbor 10.2.2.2 send-community both', 'exit-address-family']}, 'ip forward-protocol nd': [], 'no ip http server': [], 'no ip http secure-server': [], 'ip route 10.2.2.2 255.255.255.255 Tunnel0': [], 'ip access-list standard LDP': ['deny   10.0.0.0 0.0.255.255', 'permit 10.0.0.0 0.255.255.255'], 'ip prefix-list TEST seq 5 permit 10.6.6.6/32': [], 'mpls ldp router-id Loopback0 force': [], 'control-plane': [], 'line con 0': ['exec-timeout 0 0', 'privilege level 15', 'logging synchronous'], 'line aux 0': [], 'line vty 0 4': ['login', 'transport input all'], 'event manager applet update-int-desc': ['event neighbor-discovery interface regexp .*Ethernet.* cdp add', 'action 1.0 cli command "enable"', 'action 2.0 cli command "config t"', 'action 3.0 cli command "interface $_nd_local_intf_name"', 'action 4.0 cli command "description To $_nd_cdp_entry_name $_nd_port_id"', 'action 5.0 syslog msg "Description for $_nd_local_intf_name changed to $_nd_cdp_entry_name $_nd_port_id"', 'action 6.0 cli command "end"', 'action 7.0 cli command "exit"'], 'end': []}

In [99]: all                                                                                                         
Out[99]: 
{'version 15.2': [],
 'no service timestamps debug uptime': [],
 'no service timestamps log uptime': [],
 'no service password-encryption': [],
 'hostname PE_r1': [],
 'boot-start-marker': [],
 'boot-end-marker': [],
 'logging buffered 50000': [],
 'no aaa new-model': [],
 'mmi polling-interval 60': [],
 'no mmi auto-configure': [],
 'no mmi pvc': [],
 'mmi snmp-timeout 180': [],
 'ip auth-proxy max-login-attempts 5': [],
 'ip admission max-login-attempts 5': [],
 'no ip domain lookup': [],
 'ip cef': [],
 'no ipv6 cef': [],
 'multilink bundle-name authenticated': [],
 'mpls label range 1000 1999': [],
 'mpls label protocol ldp': [],
 'mpls ldp explicit-null': [],
 'mpls ldp discovery targeted-hello accept': [],
 'mpls traffic-eng tunnels': [],
 'xconnect logging redundancy': [],
 'interface Loopback0': ['ip address 10.1.1.1 255.255.255.255'],
 'interface Tunnel0': ['ip unnumbered Loopback0',
  'tunnel mode mpls traffic-eng',
  'tunnel destination 10.2.2.2',
  'tunnel mpls traffic-eng priority 7 7',
  'tunnel mpls traffic-eng bandwidth 5000',
  'tunnel mpls traffic-eng path-option 10 dynamic',
  'no routing dynamic'],
 'interface Ethernet0/0': ['description To PE_r3 Ethernet0/0',
  'bandwidth 100000',
  'ip address 10.0.13.1 255.255.255.0',
  'mpls traffic-eng tunnels',
  'ip rsvp bandwidth 100000 10000'],
 'interface Ethernet0/1': ['no ip address'],
 'interface Ethernet0/2': ['description To P_r9 Ethernet0/2',
  'ip address 10.0.19.1 255.255.255.0',
  'mpls traffic-eng tunnels',
  'ip rsvp bandwidth'],
 'interface Ethernet0/3': ['description To sw1 Ethernet0/3', 'no ip address'],
 'interface Ethernet0/3.100': {'encapsulation dot1Q 100': [],
  'xconnect 10.2.2.2 12100 encapsulation mpls': ['backup peer 10.4.4.4 14100',
   'backup delay 1 1']},
 'interface Ethernet1/0': ['no ip address', 'shutdown'],
 'router ospf 1': ['mpls ldp autoconfig area 0',
  'mpls traffic-eng router-id Loopback0',
  'mpls traffic-eng area 0',
  'network 10.0.0.0 0.255.255.255 area 0'],
 'router bgp 100': {'bgp log-neighbor-changes': [],
  'bgp bestpath igp-metric ignore': [],
  'neighbor 10.2.2.2 remote-as 100': [],
  'neighbor 10.2.2.2 update-source Loopback0': [],
  'neighbor 10.2.2.2 next-hop-self': [],
  'neighbor 10.4.4.4 remote-as 40': [],
  'address-family vpnv4': ['neighbor 10.2.2.2 activate',
   'neighbor 10.2.2.2 send-community both',
   'exit-address-family']},
 'ip forward-protocol nd': [],
 'no ip http server': [],
 'no ip http secure-server': [],
 'ip route 10.2.2.2 255.255.255.255 Tunnel0': [],
 'ip access-list standard LDP': ['deny   10.0.0.0 0.0.255.255',
  'permit 10.0.0.0 0.255.255.255'],
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32': [],
 'mpls ldp router-id Loopback0 force': [],
 'control-plane': [],
 'line con 0': ['exec-timeout 0 0',
  'privilege level 15',
  'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all'],
 'event manager applet update-int-desc': ['event neighbor-discovery interface regexp .*Ethernet.* cdp add',
  'action 1.0 cli command "enable"',
  'action 2.0 cli command "config t"',
  'action 3.0 cli command "interface $_nd_local_intf_name"',
  'action 4.0 cli command "description To $_nd_cdp_entry_name $_nd_port_id"',
  'action 5.0 syslog msg "Description for $_nd_local_intf_name changed to $_nd_cdp_entry_name $_nd_port_id"',
  'action 6.0 cli command "end"',
  'action 7.0 cli command "exit"'],
 'end': []}
"""