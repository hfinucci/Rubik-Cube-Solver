import cube as cb
import numpy as np
import algorithms as al


def colors(node):
    total = 0
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
                aux = node.cube[i][row][col]
                _col = aux % 10
                aux //= 10
                _row = aux % 10
                color = aux // 10
                if color == middle_num and _col == col and _row == row:
                    total += 1
    return 27 - total

def manhattan(node):
    for i in range(0, 6):
        middle_num = node.cube[i][(cb.n_row - 1) // 2][(cb.n_row - 1) // 2] // 100
        for row in range(0, cb.n_row):
            for col in range(0, cb.n_row):
                aux = node.cube[i][row][col]
                _col = aux % 10
                aux //= 10
                _row = aux % 10
                color = aux // 10
                distance = abs(_row - row) + abs(_col - col) + calculate_distance()
    return distance

def manhattanDistance(node):
    heuristic = 0
    for color in range(0, 6):
        for row in range(0, cb.n_row):
            for col in range(0, cb.n_row):
                target = color*100 + row*10 + col
                celda = node.cube[color][row][col]
                if celda != target:
                    target = node.cube[color][row][col]
                    heuristic += manhBfs(node, target)
    return (54 - heuristic) / 20


def manhBfs(node, target):
    algorithm = al.Bfs(node)

    aux = target
    _col = aux % 10
    aux //= 10
    _row = aux % 10
    _color = aux // 10

    while not algorithm.isEmpty():
        # busco el siguiente nodo
        node = algorithm.get_next()

        new_level = node.level + 1

        state = node.cube

        for axis in range(0, 3):
            for row in range(0, cb.n_row):
                for dire in range(0, 2):
                    # roto el cubo
                    if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
                        continue  # es el movimento que hace que vuelva al estado anterior

                    new_state = cb.rotate(state, axis, row, dire)
                    if new_state[_color][_row][_col] == target:
                        return new_level

                    # checkeo si es solucion
                    node_hash = cb.get_hash(new_state)

                    # sino, llamo a add para que guarde el nodo
                    algorithm.add(new_state, new_level, (axis, row, dire), node_hash)
