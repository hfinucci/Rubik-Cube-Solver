import copy
import random
import numpy as np
from algorithms import dfs
from constants import *


def my_hash(text: str):
    aux_hash = 0
    for ch in text:
        aux_hash = (aux_hash * 281 ^ ord(ch) * 997) & 0xFFFFFFFF
    return aux_hash


class Cube:
    def __init__(self, n):
        self.cube = np.zeros((6, n, n), dtype=int)  # numpy.int8
        self.n = n

        for i in range(0, 6):
            self.cube[i] = i

        self.init_hash = my_hash(str(self.cube))
        self.current_hash = self.init_hash

    # Rotates faces 0->1->2->3->0 if RIGHT
    def rotate_x_axis(self, row, direction):
        cube_copy = copy.deepcopy(self)
        opposite = cube_copy.n - 1 - row
        if direction == LEFT:
            aux = np.array(cube_copy.cube[YELLOW][opposite, :])
            cube_copy.cube[YELLOW][opposite, :] = cube_copy.cube[GREEN][:, row]
            cube_copy.cube[GREEN][:, row] = cube_copy.cube[RED][row, :]
            cube_copy.cube[RED][row, :] = cube_copy.cube[BLUE][:, opposite]
            cube_copy.cube[BLUE][:, opposite] = aux
        elif direction == RIGHT:
            aux = np.array(cube_copy.cube[BLUE][:, opposite])
            cube_copy.cube[BLUE][:, opposite] = cube_copy.cube[RED][row, :]
            cube_copy.cube[RED][row, :] = cube_copy.cube[GREEN][:, row]
            cube_copy.cube[GREEN][:, row] = cube_copy.cube[YELLOW][opposite, :]
            cube_copy.cube[YELLOW][opposite, :] = aux
        if row == 0:
            if direction == RIGHT:
                cube_copy.cube[WHITE] = np.rot90(cube_copy.cube[WHITE], axes=(1, 0))
            else:
                cube_copy.cube[WHITE] = np.rot90(cube_copy.cube[WHITE], axes=(0, 1))
        if row == cube_copy.n - 1:
            if direction == RIGHT:
                cube_copy.cube[ORANGE] = np.rot90(cube_copy.cube[ORANGE], axes=(1, 0))
            else:
                cube_copy.cube[ORANGE] = np.rot90(cube_copy.cube[ORANGE], axes=(0, 1))

        cube_copy.current_hash = hash(str(cube_copy.cube))
        return cube_copy

    # Rotates 0->4->2->5->0 if UP
    def rotate_y_axis(self, row, direction):
        cube_copy = copy.deepcopy(self)
        if direction == RIGHT:
            aux = np.array(cube_copy.cube[5][row, :])
            cube_copy.cube[5][row, :] = cube_copy.cube[2][row, :]
            cube_copy.cube[2][row, :] = cube_copy.cube[4][row, :]
            cube_copy.cube[4][row, :] = cube_copy.cube[0][row, :]
            cube_copy.cube[0][row, :] = aux
        elif direction == LEFT:
            aux = np.array(cube_copy.cube[0][row, :])
            cube_copy.cube[0][row, :] = cube_copy.cube[4][row, :]
            cube_copy.cube[4][row, :] = cube_copy.cube[2][row, :]
            cube_copy.cube[2][row, :] = cube_copy.cube[5][row, :]
            cube_copy.cube[5][row, :] = aux
        if row == 0:
            if direction == LEFT:
                cube_copy.cube[YELLOW] = np.rot90(cube_copy.cube[YELLOW], axes=(1, 0))
            else:
                cube_copy.cube[YELLOW] = np.rot90(cube_copy.cube[YELLOW], axes=(0, 1))
        if row == cube_copy.n - 1:
            if direction == LEFT:
                cube_copy.cube[RED] = np.rot90(cube_copy.cube[RED], axes=(0, 1))
            else:
                cube_copy.cube[RED] = np.rot90(cube_copy.cube[RED], axes=(1, 0))

        cube_copy.current_hash = hash(str(cube_copy.cube))
        return cube_copy

    def rotate_z_axis(self, row, direction):
        cube_copy = copy.deepcopy(self)
        if direction == RIGHT:
            aux = np.array(cube_copy.cube[1][:, row])
            cube_copy.cube[1][:, row] = cube_copy.cube[4][:, row]
            cube_copy.cube[4][:, row] = cube_copy.cube[3][:, row]
            cube_copy.cube[3][:, row] = cube_copy.cube[5][:, row]
            cube_copy.cube[5][:, row] = aux

        elif direction == LEFT:
            aux = np.array(cube_copy.cube[5][:, row])
            cube_copy.cube[5][:, row] = cube_copy.cube[3][:, row]
            cube_copy.cube[3][:, row] = cube_copy.cube[4][:, row]
            cube_copy.cube[4][:, row] = cube_copy.cube[1][:, row]
            cube_copy.cube[1][:, row] = aux
        if row == 0:
            if direction == RIGHT:
                cube_copy.cube[BLUE] = np.rot90(cube_copy.cube[BLUE], axes=(1, 0))
            else:
                cube_copy.cube[BLUE] = np.rot90(cube_copy.cube[BLUE], axes=(0, 1))
        if row == cube_copy.n - 1:
            if direction == RIGHT:
                cube_copy.cube[GREEN] = np.rot90(cube_copy.cube[GREEN], axes=(0, 1))
            else:
                cube_copy.cube[GREEN] = np.rot90(cube_copy.cube[GREEN], axes=(1, 0))

        cube_copy.current_hash = my_hash(str(cube_copy.cube))
        return cube_copy

    def is_done(self):
        return self.init_hash == self.current_hash

    def get_current_state(self):
        return self.current_hash

    def mix_up(self, num):
        for x in range(num):
            row = random.randint(0, self.n - 1)
            direction = random.randint(0, 1)
            match random.randint(0, 2):
                case 0:
                    self = self.rotate_x_axis(row, direction)
                case 1:
                    self = self.rotate_y_axis(row, direction)
                case 2:
                    self = self.rotate_z_axis(row, direction)

        self.current_hash = hash(str(self.cube))
        return self


cube = Cube(2)
cube = cube.mix_up(5)

print(cube.cube)

dfs(cube)