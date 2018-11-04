#!/usr/bin/env python3

"""
Задание 5.2a
Переделать скрипт из задания 5.2 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:

$ python task_5_2a.py
Enter device name: r1
Enter parameter name: ios
15.4
Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if.

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}
"""

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

device_name = input('Enter device name(r1/r2/sw1):').lower()
parameter_name = input('Enter parameter name (ios,model,vendor,location,ip):').lower()

print(london_co[device_name].get(parameter_name,'Такого параметра нет'))

"""
./5.2d.py 
Enter device name(r1/r2/sw1):sw1
Enter parameter name (ios,model,vendor,location,ip)):VENDOR
Cisco
"""
