import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import scipy as sp

master_list = []
xvalue = []
yvalue = []
zvalue = []
set_number_here = 1000000

def regular_collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        return result

def find_all_collatz(number):
    tuples = []
    tuples.append((number, regular_collatz(number)))
    tuples.append((number, 2*number))
    xvalue.append(number)
    yvalue.append(regular_collatz(number))
    if (number-1) % 3 == 0:
        tuples.append((number, (number - 1) // 3))
        zvalue.append((number - 1) // 3)
    else:
        zvalue.append(0)
    return tuples

for number_amount_you_want_to_run_for in range(2, set_number_here + 1):
    master_list.extend(find_all_collatz(number_amount_you_want_to_run_for))

G = nx.DiGraph()
G.add_edges_from(master_list)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='r', node_size=1)
nx.draw_networkx_edges(G, pos, arrows=True)
nx.draw_networkx_labels(G, pos, font_size=8, font_color='k', labels={n: str(n) for n in G.nodes()})

plt.show()