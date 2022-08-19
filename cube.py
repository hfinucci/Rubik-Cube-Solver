import random
import numpy as np

from constants import *

class Cube:
    def __init__(self, n):
        self.cube = np.zeros((6, n, n), dtype=int)

        for i in range(0,6):
            self.cube[i] = i


    # Rotates faces 1->2->3->4->1
    def RotateXAxis(self, row, direction):
        if (direction == RIGHT):
            aux = np.array(self.cube[3][row, :])
            self.cube[3][row, :] = self.cube[2][row, :]
            self.cube[2][row, :] = self.cube[1][row, :]
            self.cube[1][row, :] = self.cube[0][row, :]        
            self.cube[0][row, :] = aux
        elif (direction == LEFT):
            aux = np.array(self.cube[0][row, :])
            self.cube[0][row, :] = self.cube[1][row, :]
            self.cube[1][row, :] = self.cube[2][row, :]
            self.cube[2][row, :] = self.cube[3][row, :]        
            self.cube[3][row, :] = aux


    def RotateYAxis(self, col, direction):
        pass


    def RotateZAxis():
        pass


    def isDone():
        pass

cube = Cube(3)

print(cube.cube)



