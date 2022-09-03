import cube as cb
import numpy as np

a = 0
b = 0
c = 0

def colors(node):
    total = 0
    global a,b,c
    for i in range(0,6):
        middle_num = node.cube[i][(cb.n_row-1)//2][(cb.n_row-1)//2]
        total += np.count_nonzero(node.cube[i] == middle_num)
    return (cb.n_row * cb.n_row) * 6 - total

