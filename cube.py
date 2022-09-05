import random
import time
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

faces = ((Z_FACE, 0, 0), (Z_FACE, 0, 1), (Z_FACE, 0, 2), (Z_FACE, 1, 0),
         (Z_FACE, 1, 2), (Z_FACE, 2, 0), (Z_FACE, 2, 1), (Z_FACE, 2, 2),

         (Z_OPP_FACE, 0, 0), (Z_OPP_FACE, 0, 1), (Z_OPP_FACE, 0, 2), (Z_OPP_FACE, 1, 0),
         (Z_OPP_FACE, 1, 2), (Z_OPP_FACE, 2, 0), (Z_OPP_FACE, 2, 1), (Z_OPP_FACE, 2, 2),

         (Y_FACE, 1, 0), (Y_FACE, 1, 2), (Y_OPP_FACE, 1, 0), (Y_OPP_FACE, 1, 2))


def init_cube(n):
    global n_row, init_hash
    n_row = n
    new_cube = np.zeros((FACES_NUM, n, n), dtype=np.int16)  # numpy.int8
    for i in range(0, 6):
        for row in range(0, n):
            for col in range(0, n):
                new_cube[i][row][col] = i * 100 + row * 10 + col

    init_hash = get_hash(new_cube)

    return np.copy(new_cube)


# devulve una copia con el estado, no permite rota el centro de la cara
def rotate(cube, axis, row, direction):
    if row == n_row // 2:
        return cube
    cube_copy = np.copy(cube)
    if axis == X_AXIS:
        return rotate_x_axis(cube_copy, row, direction)
    elif axis == Y_AXIS:
        return rotate_y_axis(cube_copy, row, direction)
    elif axis == Z_AXIS:
        return rotate_z_axis(cube_copy, row, direction)


# Rotates faces 0->1->2->3->0 if RIGHT
def rotate_x_axis(cube, row, direction):
    opp_n = n_row - 1 - row
    if direction == LEFT:
        aux = np.array(cube[Y_OPP_FACE][opp_n, :])
        cube[Y_OPP_FACE][opp_n, :] = cube[Z_OPP_FACE][:, row]
        cube[Z_OPP_FACE][:, row] = cube[Y_FACE][row, :]
        cube[Y_FACE][row, :] = cube[Z_FACE][:, opp_n]
        cube[Z_FACE][:, opp_n] = aux
    elif direction == RIGHT:
        aux = np.array(cube[Z_FACE][:, opp_n])
        cube[Z_FACE][:, opp_n] = cube[Y_FACE][row, :]
        cube[Y_FACE][row, :] = cube[Z_OPP_FACE][:, row]
        cube[Z_OPP_FACE][:, row] = cube[Y_OPP_FACE][opp_n, :]
        cube[Y_OPP_FACE][opp_n, :] = aux
    if row == 0:
        if direction == RIGHT:
            cube[X_FACE] = np.rot90(cube[X_FACE], axes=(1, 0))
        else:
            cube[X_FACE] = np.rot90(cube[X_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == RIGHT:
            cube[X_OPP_FACE] = np.rot90(cube[X_OPP_FACE], axes=(1, 0))
        else:
            cube[X_OPP_FACE] = np.rot90(cube[X_OPP_FACE], axes=(0, 1))

    return cube


# Rotates 0->4->2->5->0 if UP
def rotate_y_axis(cube, row, direction):
    if direction == RIGHT:
        aux = np.array(cube[X_OPP_FACE][row, :])
        cube[X_OPP_FACE][row, :] = cube[Z_OPP_FACE][row, :]
        cube[Z_OPP_FACE][row, :] = cube[X_FACE][row, :]
        cube[X_FACE][row, :] = cube[Z_FACE][row, :]
        cube[Z_FACE][row, :] = aux
    elif direction == LEFT:
        aux = np.array(cube[Z_FACE][row, :])
        cube[Z_FACE][row, :] = cube[X_FACE][row, :]
        cube[X_FACE][row, :] = cube[Z_OPP_FACE][row, :]
        cube[Z_OPP_FACE][row, :] = cube[X_OPP_FACE][row, :]
        cube[X_OPP_FACE][row, :] = aux
    if row == 0:
        if direction == LEFT:
            cube[Y_OPP_FACE] = np.rot90(cube[Y_OPP_FACE], axes=(1, 0))
        else:
            cube[Y_OPP_FACE] = np.rot90(cube[Y_OPP_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == LEFT:
            cube[Y_FACE] = np.rot90(cube[Y_FACE], axes=(0, 1))
        else:
            cube[Y_FACE] = np.rot90(cube[Y_FACE], axes=(1, 0))

    return cube


def rotate_z_axis(cube, row, direction):
    if direction == RIGHT:
        aux = np.array(cube[Y_FACE][:, row])
        cube[Y_FACE][:, row] = cube[X_FACE][:, row]
        cube[X_FACE][:, row] = cube[Y_OPP_FACE][:, row]
        cube[Y_OPP_FACE][:, row] = cube[X_OPP_FACE][:, row]
        cube[X_OPP_FACE][:, row] = aux

    elif direction == LEFT:
        aux = np.array(cube[X_OPP_FACE][:, row])
        cube[X_OPP_FACE][:, row] = cube[Y_OPP_FACE][:, row]
        cube[Y_OPP_FACE][:, row] = cube[X_FACE][:, row]
        cube[X_FACE][:, row] = cube[Y_FACE][:, row]
        cube[Y_FACE][:, row] = aux
    if row == 0:
        if direction == RIGHT:
            cube[Z_FACE] = np.rot90(cube[Z_FACE], axes=(1, 0))
        else:
            cube[Z_FACE] = np.rot90(cube[Z_FACE], axes=(0, 1))
    if row == n_row - 1:
        if direction == RIGHT:
            cube[Z_OPP_FACE] = np.rot90(cube[Z_OPP_FACE], axes=(0, 1))
        else:
            cube[Z_OPP_FACE] = np.rot90(cube[Z_OPP_FACE], axes=(1, 0))

    return cube


def get_hash(cube: np):
    return hash(cube.tostring())


def is_done(state):
    global init_hash
    return state == init_hash


def mix_up(cube, num):
    cube_copy = np.copy(cube)
    for x in range(num):
        row = random.randint(0, n_row - 1)
        direction = random.randint(0, 1)
        axis = random.randint(0, 2)
        cube_copy = rotate(cube_copy, axis, row, direction)
    return cube_copy
