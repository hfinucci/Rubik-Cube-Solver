import random
import numpy as np

BLUE = 0
RED = 1
GREEN = 2
YELLOW = 3
WHITE = 4
ORANGE = 5

LEFT = 0
RIGHT = 1

class Cube:

    def __init__(self, n):
        self.face0 = np.full((n,n), BLUE)
        self.face1 = np.full((n,n), RED)
        self.face2 = np.full((n,n), GREEN)
        self.face3 = np.full((n,n), YELLOW)
        self.face4 = np.full((n,n), WHITE)
        self.face5 = np.full((n,n), ORANGE)

    # Rotates faces 1->2->3->4->1
    def RotateXAxis(self, col, direction):
        aux = np.array(self.face3[col])
        self.face3[col] = self.face2[col]
        self.face2[col] = self.face1[col]
        self.face1[col] = self.face0[col]
        self.face0[col] = aux

    def RotateYAxis():
        pass
    
    def RotateZAxis():
        pass

    def isDone():
        pass

cube = Cube(3)

cube.RotateXAxis(0, RIGHT)

print(cube.face0)
print(cube.face1)
print(cube.face2)
print(cube.face3)
print(cube.face4)
print(cube.face5)

cube.RotateXAxis(0, RIGHT)



