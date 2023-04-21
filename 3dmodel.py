import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

master_list = []
xvalue = []
yvalue = []
zvalue = []
set_number_here = 100

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

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot3D(xvalue, yvalue, zvalue, 'green')

plt.show()
