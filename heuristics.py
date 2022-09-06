import cube as cb
import numpy as np
import algorithms as al


def colors(node):
    total = 0
    for i in range(0, 6):
        middle_color = node.cube[i][(cb.n_row - 1) // 2][(cb.n_row - 1) // 2] // 100
        total += np.count_nonzero(node.cube[i] == middle_color)
    return ((cb.n_row * cb.n_row) * 6 - total)


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
    return ((cb.n_row * cb.n_row) * 6 - total)


def manhattanDistance(node):
    heuristic = 0
    for face in cb.faces:
        target = face[0] * 100 + face[1] * 10 + face[2]
        cell_value = node.cube[face[0]][face[1]][face[2]]
        if cell_value != target:
            heuristic += manhBfs(node, cell_value)
    return heuristic // 8


# cuantos rotacion se necesita para que la celda target quede en el lugar correcto
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
        if new_level == 6:
            return new_level + 10

        state = node.cube
        for axis in range(0, 3):
            for row in range(0, cb.n_row):
                for dire in range(0, 2):
                    # descartó las rotaciones que no son necesarias
                    if row == cb.n_row // 2:
                        continue
                    if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
                        continue  # es el movimento que hace que vuelva al estado anterior

                    # roto el cubo
                    new_state = cb.rotate(state, axis, row, dire)

                    # checkeo si es solucion
                    if new_state[_color][_row][_col] == target:
                        return new_level

                    # obtengo el hash del nuevo estado
                    node_hash = cb.get_hash(new_state)

                    # sino, llamo a add para que guarde el nodo
                    algorithm.add(new_state, new_level, (axis, row, dire), node_hash)