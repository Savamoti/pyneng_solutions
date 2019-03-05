#!/usr/bin/env python3

"""
Задание 11.2
Для выполнения этого задания, должен быть установлен graphviz:
apt-get install graphviz
И модуль python для работы с graphviz:
pip install graphviz
С помощью функции parse_cdp_neighbors из задания 11.1 и функции draw_topology из файла draw_network_graph.py, сгенерировать топологию, которая соответствует выводу команды sh cdp neighbor в файле sw1_sh_cdp_neighbors.txt
Не копировать код функций parse_cdp_neighbors и draw_topology.
В итоге, должен быть сгенерировано изображение топологии. Результат должен выглядеть так же, как схема в файле task_11_2_topology.svg

При этом:
Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
Расположение устройств на схеме может быть другим
Соединения должны соответствовать схеме
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from task_11_1 import parse_cdp_neighbors
from draw_network_graph import *
q = parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')
draw_topology(q)

"""
(pyneng) ✔ ~/git/pyneng_solutions/11 [master|…1]
14:30 $ ./task_11_2.py
Graph saved in img/topology.svg
"""
