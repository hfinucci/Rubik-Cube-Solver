import random
from hashlib import sha1

import numpy as np

# Rotate X axis
LEFT = 0
RIGHT = 1

# Rotate Y axis
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

# Faces
FACES_NUM = 6

Z_FACE = 0
Y_FACE = 1
Z_OPP_FACE = 2
Y_OPP_FACE = 3
X_FACE = 4
X_OPP_FACE = 5

# Faces colors
BLUE = Z_FACE
RED = Y_OPP_FACE
GREEN = Z_OPP_FACE
YELLOW = X_OPP_FACE
WHITE = X_FACE
ORANGE = Y_FACE

n_row = 0
init_hash = 0


def init_cube(n):
    global n_row, init_hash
    n_row = n
    new_cube = np.zeros((FACES_NUM, n_row, n_row), dtype=np.int8)  # numpy.int8
    for i in range(0, 6):
        new_cube[i] = i

    init_hash = get_hash(new_cube)
    return np.copy(new_cube)


def rotate(cube, axis, row, direction):
    if axis == X_AXIS:
        return rotate_x_axis(cube, row, direction)
    elif axis == Y_AXIS:
        return rotate_y_axis(cube, row, direction)
    elif axis == Z_AXIS:
        return rotate_z_axis(cube, row, direction)


# Rotates faces 0->1->2->3->0 if RIGHT
def rotate_x_axis(cube, row, direction):
    cube_copy = np.copy(cube)
    opp_n = n_row - 1 - row
    if direction == LEFT:
        aux = np.array(cube_copy[Y_OPP_FACE][opp_n, :])
        cube_copy[Y_OPP_FACE][opp_n, :] = cube_copy[Z_OPP_FACE][:, row]
        cube_copy[Z_OPP_FACE][:, row] = cube_copy[Y_FACE][row, :]
        cube_copy[Y_FACE][row, :] = cube_copy[Z_FACE][:, opp_n]
        cube_copy[Z_FACE][:, opp_n] = aux
    elif direction == RIGHT:
        aux = np.array(cube_copy[Z_FACE][:, opp_n])
        cube_copy[Z_FACE][:, opp_n] = cube_copy[Y_FACE][row, :]
        cube_copy[Y_FACE][row, :] = cube_copy[Z_OPP_FACE][:, row]
        cube_copy[Z_OPP_FACE][:, row] = cube_copy[Y_OPP_FACE][opp_n, :]
        cube_copy[Y_OPP_FACE][opp_n, :] = aux
    if row == 0:
        if direction == RIGHT:
            cube_copy[X_FACE] = np.rot90(cube_copy[X_FACE], axes=(1, 0))
        else:
            cube_copy[X_FACE] = np.rot90(cube_copy[X_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == RIGHT:
            cube_copy[X_OPP_FACE] = np.rot90(cube_copy[X_OPP_FACE], axes=(1, 0))
        else:
            cube_copy[X_OPP_FACE] = np.rot90(cube_copy[X_OPP_FACE], axes=(0, 1))

    return cube_copy


# Rotates 0->4->2->5->0 if UP
def rotate_y_axis(cube, row, direction):
    cube_copy = np.copy(cube)
    if direction == RIGHT:
        aux = np.array(cube_copy[X_OPP_FACE][row, :])
        cube_copy[X_OPP_FACE][row, :] = cube_copy[Z_OPP_FACE][row, :]
        cube_copy[Z_OPP_FACE][row, :] = cube_copy[X_FACE][row, :]
        cube_copy[X_FACE][row, :] = cube_copy[Z_FACE][row, :]
        cube_copy[Z_FACE][row, :] = aux
    elif direction == LEFT:
        aux = np.array(cube_copy[Z_FACE][row, :])
        cube_copy[Z_FACE][row, :] = cube_copy[X_FACE][row, :]
        cube_copy[X_FACE][row, :] = cube_copy[Z_OPP_FACE][row, :]
        cube_copy[Z_OPP_FACE][row, :] = cube_copy[X_OPP_FACE][row, :]
        cube_copy[X_OPP_FACE][row, :] = aux
    if row == 0:
        if direction == LEFT:
            cube_copy[Y_OPP_FACE] = np.rot90(cube_copy[Y_OPP_FACE], axes=(1, 0))
        else:
            cube_copy[Y_OPP_FACE] = np.rot90(cube_copy[Y_OPP_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == LEFT:
            cube_copy[Y_FACE] = np.rot90(cube_copy[Y_FACE], axes=(0, 1))
        else:
            cube_copy[Y_FACE] = np.rot90(cube_copy[Y_FACE], axes=(1, 0))

    return cube_copy


def rotate_z_axis(cube, row, direction):
    cube_copy = np.copy(cube)
    if direction == RIGHT:
        aux = np.array(cube_copy[Y_FACE][:, row])
        cube_copy[Y_FACE][:, row] = cube_copy[X_FACE][:, row]
        cube_copy[X_FACE][:, row] = cube_copy[Y_OPP_FACE][:, row]
        cube_copy[Y_OPP_FACE][:, row] = cube_copy[X_OPP_FACE][:, row]
        cube_copy[X_OPP_FACE][:, row] = aux

    elif direction == LEFT:
        aux = np.array(cube_copy[X_OPP_FACE][:, row])
        cube_copy[X_OPP_FACE][:, row] = cube_copy[Y_OPP_FACE][:, row]
        cube_copy[Y_OPP_FACE][:, row] = cube_copy[X_FACE][:, row]
        cube_copy[X_FACE][:, row] = cube_copy[Y_FACE][:, row]
        cube_copy[Y_FACE][:, row] = aux
    if row == 0:
        if direction == RIGHT:
            cube_copy[Z_FACE] = np.rot90(cube_copy[Z_FACE], axes=(1, 0))
        else:
            cube_copy[Z_FACE] = np.rot90(cube_copy[Z_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == RIGHT:
            cube_copy[Z_OPP_FACE] = np.rot90(cube_copy[Z_OPP_FACE], axes=(0, 1))
        else:
            cube_copy[Z_OPP_FACE] = np.rot90(cube_copy[Z_OPP_FACE], axes=(1, 0))

    return cube_copy


def get_hash(cube: np):
    return hash(cube.tostring())



def is_done(state):
    return state == init_hash


def mix_up(cube, num):
    cube_copy = np.copy(cube)
    for x in range(num):
        row = random.randint(0, n_row - 1)
        direction = random.randint(0, 1)
        match random.randint(0, 2):
            case 0:
                cube_copy = rotate_x_axis(cube_copy, row, direction)
            case 1:
                cube_copy = rotate_y_axis(cube_copy, row, direction)
            case 2:
                cube_copy = rotate_z_axis(cube_copy, row, direction)

    return cube_copy


x = "13333333333333"


class Node:
    def __init__(self, cube, level, cost, rotate):
        self.cube = cube
        self.level = level
        self.rotate = rotate
        self.cost = cost


aux = np.zeros((FACES_NUM, 3, 3), dtype=np.int8)  # numpy.int8
node = Node(aux, 0, 1, (-1, -1, -1))

axis = 0
row = 22
dire = 1
if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
    print('sip')

"""""



for i in range(0, 6):
    aux[i] = i
start = time.perf_counter()
hash(str(str(aux[Z_FACE]) + str(aux[Y_FACE]) + str(aux[X_FACE])))
end = time.perf_counter()

print(end - start)


sha1(arr)

"""""
