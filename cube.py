import random
import numpy as np
from constants import *


class Cube:
    def __init__(self, n):
        self.cube = np.zeros((6, n, n), dtype=int)  # numpy.int8
        self.n = n

        for i in range(0, 6):
            self.cube[i] = i

        self.init_hash = hash(str(self.cube))
        self.current_hash = self.init_hash

    # Rotates faces 0->1->2->3->0 if RIGHT
    def rotate_x_axis(self, row, direction):
        opposite = self.n - 1 - row
        if direction == LEFT:
            aux = np.array(self.cube[YELLOW][opposite, :])
            self.cube[YELLOW][opposite, :] = self.cube[GREEN][:, row]
            self.cube[GREEN][:, row] = self.cube[RED][row, :]
            self.cube[RED][row, :] = self.cube[BLUE][:, opposite]
            self.cube[BLUE][:, opposite] = aux
        elif direction == RIGHT:
            aux = np.array(self.cube[BLUE][:, opposite])
            self.cube[BLUE][:, opposite] = self.cube[RED][row, :]
            self.cube[RED][row, :] = self.cube[GREEN][:, row]
            self.cube[GREEN][:, row] = self.cube[YELLOW][opposite, :]
            self.cube[YELLOW][opposite, :] = aux
        if row == 0:
            if direction == RIGHT:
                self.cube[WHITE] = np.rot90(self.cube[WHITE], axes=(1, 0))
            else:
                self.cube[WHITE] = np.rot90(self.cube[WHITE], axes=(0, 1))
        if row == self.n - 1:
            if direction == RIGHT:
                self.cube[ORANGE] = np.rot90(self.cube[ORANGE], axes=(1, 0))
            else:
                self.cube[ORANGE] = np.rot90(self.cube[ORANGE], axes=(0, 1))

        self.current_hash = hash(str(self.cube))
        return self.current_hash

    # Rotates 0->4->2->5->0 if UP
    def rotate_y_axis(self, row, direction):
        if direction == RIGHT:
            aux = np.array(self.cube[5][row, :])
            self.cube[5][row, :] = self.cube[2][row, :]
            self.cube[2][row, :] = self.cube[4][row, :]
            self.cube[4][row, :] = self.cube[0][row, :]
            self.cube[0][row, :] = aux
        elif direction == LEFT:
            aux = np.array(self.cube[0][row, :])
            self.cube[0][row, :] = self.cube[4][row, :]
            self.cube[4][row, :] = self.cube[2][row, :]
            self.cube[2][row, :] = self.cube[5][row, :]
            self.cube[5][row, :] = aux
        if row == 0:
            if direction == LEFT:
                self.cube[YELLOW] = np.rot90(self.cube[YELLOW], axes=(1, 0))
            else:
                self.cube[YELLOW] = np.rot90(self.cube[YELLOW], axes=(0, 1))
        if row == self.n - 1:
            if direction == LEFT:
                self.cube[RED] = np.rot90(self.cube[RED], axes=(0, 1))
            else:
                self.cube[RED] = np.rot90(self.cube[RED], axes=(1, 0))

        self.current_hash = hash(str(self.cube))
        return self.current_hash

    def rotate_z_axis(self, row, direction):
        if direction == RIGHT:
            aux = np.array(self.cube[1][:, row])
            self.cube[1][:, row] = self.cube[4][:, row]
            self.cube[4][:, row] = self.cube[3][:, row]
            self.cube[3][:, row] = self.cube[5][:, row]
            self.cube[5][:, row] = aux

        elif direction == LEFT:
            aux = np.array(self.cube[5][:, row])
            self.cube[5][:, row] = self.cube[3][:, row]
            self.cube[3][:, row] = self.cube[4][:, row]
            self.cube[4][:, row] = self.cube[1][:, row]
            self.cube[1][:, row] = aux
        if row == 0:
            if direction == RIGHT:
                self.cube[BLUE] = np.rot90(self.cube[BLUE], axes=(1, 0))
            else:
                self.cube[BLUE] = np.rot90(self.cube[BLUE], axes=(0, 1))
        if row == self.n - 1:
            if direction == RIGHT:
                self.cube[GREEN] = np.rot90(self.cube[GREEN], axes=(0, 1))
            else:
                self.cube[GREEN] = np.rot90(self.cube[GREEN], axes=(1, 0))

        self.current_hash = hash(str(self.cube))
        return self.current_hash

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
                    self.rotate_x_axis(row, direction)
                case 1:
                    self.rotate_y_axis(row, direction)
                case 2:
                    self.rotate_z_axis(row, direction)

        self.current_hash = hash(str(self.cube))
        return self.current_hash


cube = Cube(3)
print("el primer estado")
print(cube.get_current_state())
cube.rotate_x_axis(0, RIGHT)
cube.rotate_y_axis(0, RIGHT)
cube.rotate_z_axis(0, RIGHT)
print(cube.get_current_state())
cube.rotate_z_axis(0, LEFT)
cube.rotate_y_axis(0, LEFT)
cube.rotate_x_axis(0, LEFT)
print(cube.get_current_state())

if cube.is_done():
    print("ok")
else:
    print("mal")
