#!/usr/bin/env python3
"""
Задание 11.2a
Для выполнения этого задания, должен быть установлен graphviz:
apt-get install graphviz
И модуль python для работы с graphviz:
pip install graphviz
С помощью функции parse_cdp_neighbors из задания 11.1 и функции draw_topology из файла draw_network_graph.py, сгенерировать топологию, которая соответствует выводу команды sh cdp neighbor из файлов:
sh_cdp_n_sw1.txt
sh_cdp_n_r1.txt
sh_cdp_n_r2.txt
sh_cdp_n_r3.txt
Не копировать код функций parse_cdp_neighbors и draw_topology.
В итоге, должен быть сгенерировано изображение топологии. Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg

При этом:
Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
Расположение устройств на схеме может быть другим
Соединения должны соответствовать схеме
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import *
q1 = parse_cdp_neighbors('sh_cdp_n_r1.txt')
q2 = parse_cdp_neighbors('sh_cdp_n_r2.txt')
q3 = parse_cdp_neighbors('sh_cdp_n_r3.txt')
q4 = parse_cdp_neighbors('sh_cdp_n_sw1.txt')
q = {}
q.update(q1)
q.update(q2)
q.update(q3)
q.update(q4)

s = {} 
lists = [] 
 
for key, value in q.items(): 
    dic_buffer = {} 
    key_str = ''.join(list(key)) 
    value_str = ''.join(list(value)) 
    if key_str not in ''.join(lists) or value_str not in ''.join(lists):
        lists.append(key_str) 
        lists.append(value_str) 
        s[key] = value
    else:
        pass
draw_topology(s)

"""
13:02 $ python task_11_2a.py 
Graph saved in img/topology.svg
"""