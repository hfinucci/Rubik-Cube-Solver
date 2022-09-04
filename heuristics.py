import cube as cb
import numpy as np

a = 0
b = 0
c = 0


def colors(node):
    total = 0
    global a, b, c
    for i in range(0, 6):
        middle_num = node.cube[i][(cb.n_row - 1) // 2][(cb.n_row - 1) // 2]
        total += np.count_nonzero(node.cube[i] == middle_num)
    return (cb.n_row * cb.n_row) * 6 - total


def cubes(node):
    total = 0
    for i in range(0, 6):
        middle_num = node.cube[i][(cb.n_row - 1) // 2][(cb.n_row - 1) // 2] // 100
        for row in range(0, cb.n_row):
            for col in range(0, cb.n_row):
                # print(node.cube)
                # print(node.cube[i][row][col])
                aux = node.cube[i][row][col]
                _col = aux % 10
                aux //= 10
                _row = aux % 10
                color = aux // 10
                # print("color :" + str(color))
                # print("row :" + str(row) + " _row :" + str(_row) )
                # print("col :" + str(col) + " _col :" + str(_col))
                # print("-------------------")
                if color == middle_num and _col == col and _row == row:
                    total += 1
    return 27 - total


def deeper(node):
    return 0
