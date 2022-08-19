import random
import numpy as np

from constants import *

class Cube:
    def __init__(self, n):
        self.cube = np.zeros((6, n, n), dtype=int)

        for i in range(0,6):
            self.cube[i] = i


    # Rotates faces 0->1->2->3->0 if RIGHT
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

    # Rotates 0->4->2->5->0 if UP
    def RotateYAxis(self, col, direction):
        if (direction == UP):
            aux = np.array(self.cube[5][:, col])
            self.cube[5][:, col] = self.cube[2][:, col]
            self.cube[2][:, col] = self.cube[4][:, col]
            self.cube[4][:, col] = self.cube[0][:, col]        
            self.cube[0][:, col] = aux
        elif (direction == DOWN):
            aux = np.array(self.cube[0][:, col])
            self.cube[0][:, col] = self.cube[4][:, col]
            self.cube[4][:, col] = self.cube[2][:, col]
            self.cube[2][:, col] = self.cube[5][:, col]        
            self.cube[5][:, col] = aux

    def RotateZAxis(self, face, direction):
        if (direction == CLOCKWISE):
            self.cube[face] = np.rot90(self.cube[face], axes=(1,0))
            
        elif (direction == ANTI_CLOCKWISE):
            self.cube[face] = np.rot90(self.cube[face])

    def isDone():
        pass




cube = Cube(3)
cube.RotateXAxis(0,RIGHT)
cube.RotateYAxis(1, DOWN)
cube.RotateZAxis(1, CLOCKWISE)

print(cube.cube)



