#!/usr/bin/env python3
"""
Задание 7.1
Аналогично заданию 4.6 обработать строки из файла ospf.txt и вывести информацию по каждой в таком виде:

Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('ospf.txt', 'r') as text:
    ospf = text.readlines()
    for lines in ospf:
        lines = lines.strip().split()
        protocol = lines[0].replace('O', 'OSPF')
        prefix = lines[1]
        ad = lines[2].strip('[]')
        hop = lines[4].strip(',')
        update = lines[5].strip(',')
        interface = lines[6]
        ospf_route = """
        Protocol:             {0:18}
        Prefix:               {1:18}
        AD/Metric:            {2:18}
        Next-Hop:             {3:18}
        Last update:          {4:18}
        Outbound Interface:   {5:18}
        """
        print(ospf_route.format(protocol,prefix,ad,hop,update,interface))

"""
11:22 $ ./7.1.py 

        Protocol:             OSPF              
        Prefix:               10.0.24.0/24      
        AD/Metric:            110/41            
        Next-Hop:             10.0.13.3         
        Last update:          3d18h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.28.0/24      
        AD/Metric:            110/31            
        Next-Hop:             10.0.13.3         
        Last update:          3d20h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.37.0/24      
        AD/Metric:            110/11            
        Next-Hop:             10.0.13.3         
        Last update:          3d20h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.41.0/24      
        AD/Metric:            110/51            
        Next-Hop:             10.0.13.3         
        Last update:          3d20h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.78.0/24      
        AD/Metric:            110/21            
        Next-Hop:             10.0.13.3         
        Last update:          3d20h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.79.0/24      
        AD/Metric:            110/20            
        Next-Hop:             10.0.19.9         
        Last update:          4d02h             
        Outbound Interface:   FastEthernet0/2   
        

        Protocol:             OSPF              
        Prefix:               10.0.81.0/24      
        AD/Metric:            110/41            
        Next-Hop:             10.0.13.3         
        Last update:          3d20h             
        Outbound Interface:   FastEthernet0/0   
        

        Protocol:             OSPF              
        Prefix:               10.0.91.0/24      
        AD/Metric:            110/60            
        Next-Hop:             10.0.19.9         
        Last update:          3d19h             
        Outbound Interface:   FastEthernet0/2   
"""
