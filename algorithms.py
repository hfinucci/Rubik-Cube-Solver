
from collections import deque
from constants import *





def dfs(cube):

    visited = dict()
    stack = deque()
 
    visited[cube.get_current_state()] = True
    # visited.append(cube.get_current_state())
    stack.append(cube)

    while (stack):
        current_node = stack.pop()

        if (current_node.is_done()):
            print("TERMINE")
            print(current_node.cube)
            exit()

        for i in range(0, cube.n):
            evaluate_node(visited, stack, current_node.rotate_x_axis(i, RIGHT))
            evaluate_node(visited, stack, current_node.rotate_x_axis(i, LEFT))
            evaluate_node(visited, stack, current_node.rotate_y_axis(i, RIGHT))
            evaluate_node(visited, stack, current_node.rotate_y_axis(i, LEFT))
            evaluate_node(visited, stack, current_node.rotate_z_axis(i, RIGHT))
            evaluate_node(visited, stack, current_node.rotate_z_axis(i, LEFT))
    
def evaluate_node(visited, stack, cube):
    hash_value = cube.get_current_state()
    if ((hash_value not in visited) and (not cube.is_done())):
        stack.append(cube)
        visited[hash_value] = True
        # print(visited)
    elif(hash_value in visited):
        pass
        # print(visited)
    elif (cube.is_done()):
        print('SOLUCION') # Que pasa si el cubo esta termiando?
        print(cube.cube)
        exit()