import copy
import random
import numpy as np
from algorithms import dfs
from constants import *

FACES_NUM = 6
Z_FACE = 0
Y_FACE = 1
X_FACE = 2
Z_OPP_FACE = 3
Y_OPP_FACE = 4
X_OPP_FACE = 5

n_col = 0
init_hash = 0


def init_cube(n):
    global n_col, init_hash
    n_col = n
    new_cube = np.zeros((FACES_NUM, n_col, n_col), dtype=int)  # numpy.int8
    for i in range(0, 6):
        new_cube[i] = i
    init_hash = get_current_state(new_cube)
    return np.copy(new_cube)


# Rotates faces 0->1->2->3->0 if RIGHT
def rotate_x_axis(cube, row, direction):
    cube_copy = copy.deepcopy(cube)
    opp_n = n_col - 1 - row
    if direction == LEFT:
        aux = np.array(cube_copy[Z_OPP_FACE][opp_n, :])
        cube_copy[Z_OPP_FACE][opp_n, :] = cube_copy[X_FACE][:, row]
        cube_copy[X_FACE][:, row] = cube_copy[Y_FACE][row, :]
        cube_copy[Y_FACE][row, :] = cube_copy[Z_FACE][:, opp_n]
        cube_copy[Z_FACE][:, opp_n] = aux
    elif direction == RIGHT:
        aux = np.array(cube_copy[Z_FACE][:, opp_n])
        cube_copy[Z_FACE][:, opp_n] = cube_copy[Y_FACE][row, :]
        cube_copy[Y_FACE][row, :] = cube_copy[X_FACE][:, row]
        cube_copy[X_FACE][:, row] = cube_copy[Z_OPP_FACE][opp_n, :]
        cube_copy[Z_OPP_FACE][opp_n, :] = aux
    if row == 0:
        if direction == RIGHT:
            cube_copy[Y_OPP_FACE] = np.rot90(cube_copy[Y_OPP_FACE], axes=(1, 0))
        else:
            cube_copy[Y_OPP_FACE] = np.rot90(cube_copy[Y_OPP_FACE], axes=(0, 1))
    if row == n_col - 1:
        if direction == RIGHT:
            cube_copy[X_OPP_FACE] = np.rot90(cube_copy[X_OPP_FACE], axes=(1, 0))
        else:
            cube_copy[X_OPP_FACE] = np.rot90(cube_copy[X_OPP_FACE], axes=(0, 1))

    return cube_copy


# Rotates 0->4->2->5->0 if UP
def rotate_y_axis(cube, row, direction):
    cube_copy = copy.deepcopy(cube)
    if direction == RIGHT:
        aux = np.array(cube_copy[X_OPP_FACE][row, :])
        cube_copy[X_OPP_FACE][row, :] = cube_copy[Z_FACE][row, :]
        cube_copy[Z_FACE][row, :] = cube_copy[Y_OPP_FACE][row, :]
        cube_copy[Y_OPP_FACE][row, :] = cube_copy[Z_FACE][row, :]
        cube_copy[Z_FACE][row, :] = aux
    elif direction == LEFT:
        aux = np.array(cube_copy[Z_FACE][row, :])
        cube_copy[Z_FACE][row, :] = cube_copy[Y_OPP_FACE][row, :]
        cube_copy[Y_OPP_FACE][row, :] = cube_copy[Z_FACE][row, :]
        cube_copy[Z_FACE][row, :] = cube_copy[X_OPP_FACE][row, :]
        cube_copy[X_OPP_FACE][row, :] = aux
    if row == 0:
        if direction == LEFT:
            cube_copy[Z_OPP_FACE] = np.rot90(cube_copy[Z_OPP_FACE], axes=(1, 0))
        else:
            cube_copy[Z_OPP_FACE] = np.rot90(cube_copy[Z_OPP_FACE], axes=(0, 1))
    if row == n_col - 1:
        if direction == LEFT:
            cube_copy[Y_FACE] = np.rot90(cube_copy[Y_FACE], axes=(0, 1))
        else:
            cube_copy[Y_FACE] = np.rot90(cube_copy[Y_FACE], axes=(1, 0))

    return cube_copy


def rotate_z_axis(cube, row, direction):
    cube_copy = copy.deepcopy(cube)
    if direction == RIGHT:
        aux = np.array(cube_copy[Y_FACE][:, row])
        cube_copy[Y_FACE][:, row] = cube_copy[Y_OPP_FACE][:, row]
        cube_copy[Y_OPP_FACE][:, row] = cube_copy[Z_OPP_FACE][:, row]
        cube_copy[Z_OPP_FACE][:, row] = cube_copy[X_OPP_FACE][:, row]
        cube_copy[X_OPP_FACE][:, row] = aux

    elif direction == LEFT:
        aux = np.array(cube_copy[X_OPP_FACE][:, row])
        cube_copy[X_OPP_FACE][:, row] = cube_copy[Z_OPP_FACE][:, row]
        cube_copy[Z_OPP_FACE][:, row] = cube_copy[Y_OPP_FACE][:, row]
        cube_copy[Y_OPP_FACE][:, row] = cube_copy[Y_FACE][:, row]
        cube_copy[Y_FACE][:, row] = aux
    if row == 0:
        if direction == RIGHT:
            cube_copy[Z_FACE] = np.rot90(cube_copy[Z_FACE], axes=(1, 0))
        else:
            cube_copy[Z_FACE] = np.rot90(cube_copy[Z_FACE], axes=(0, 1))
    if row == n_col - 1:
        if direction == RIGHT:
            cube_copy[X_FACE] = np.rot90(cube_copy[X_FACE], axes=(0, 1))
        else:
            cube_copy[X_FACE] = np.rot90(cube_copy[X_FACE], axes=(1, 0))

    return cube_copy


def get_current_state(cube):
    return hash(str(cube))


def is_done(state):
    return state == init_hash


def mix_up(cube, num):
    cube_copy = copy.deepcopy(cube)
    for x in range(num):
        row = random.randint(0, n_col - 1)
        direction = random.randint(0, 1)
        match random.randint(0, 2):
            case 0:
                cube_copy = rotate_x_axis(cube_copy, row, direction)
            case 1:
                cube_copy = rotate_y_axis(cube_copy, row, direction)
            case 2:
                cube_copy = rotate_z_axis(cube_copy, row, direction)

    return cube_copy
