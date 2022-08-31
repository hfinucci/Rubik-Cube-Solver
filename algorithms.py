import time
from collections import deque
from queue import PriorityQueue
import numpy as np
import cube as cb


class Node:
    def __init__(self, cube, level, rotate):
        self.cube = cube
        self.level = level
        self.rotate = rotate


class Dfs:
    def __init__(self, first_node):
        self.stack = deque()
        self.visited = set()
        self.stack.append(first_node)

    def add(self, aux_cube, new_level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            self.stack.append(Node(aux_cube, new_level, settings))

    def get_next(self):
        return self.stack.pop()

    def isEmpty(self):
        if self.stack:
            return False
        return True


class Bfs:
    def __init__(self, first_node):
        self.stack = deque()
        self.visited = set()
        self.stack.append(first_node)

    def add(self, aux_cube, level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            self.stack.append(Node(aux_cube, level, settings))

    def get_next(self):
        return self.stack.popleft()

    def isEmpty(self):
        if self.stack:
            return False
        return True


class AStar:
    def __init__(self, fist_node, heuristic):
        self.list = PriorityQueue()
        self.visited = set()
        self.list.append(fist_node)
        self.heuristic = heuristic

    def add(self, aux_cube, level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            node = Node(aux_cube, level, settings)
            h_value = self.heuristic(node)
            self.list.put((node.level + h_value, node))

    def get_next(self):
        return self.list.get()

    def isEmpty(self):
        return self.list.empty()
            

# Igual que AStar pero la prioridad del priority queue solo se ve afectada por la herisitca
class Greedy:
    def __init__(self, fist_node, heuristic):
        self.list = PriorityQueue()
        self.visited = set()
        self.list.append(fist_node)
        self.heuristic = heuristic

    def add(self, aux_cube, level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            node = Node(aux_cube, level, settings)
            h_value = self.heuristic(node)
            self.list.put((h_value, node))

    def get_next(self):
        return self.list.get()

    def isEmpty(self):
        return self.list.empty()


def rookie(num):
    print('rookie!')
    print(num)

def algorithms(num):
    # PRUEBA
    # Creó el cubo
    f_cube = cb.init_cube(3)

    # mezclo el cubo
    f_cube = cb.mix_up(f_cube, num)

    # creo el nodo raiz
    f_node = Node(f_cube, 0, (-1, -1, -1))

    print(f_node.cube)
    print("---------")
    # creo el arbol
    # algorithm = Dfs(f_node)
    algorithm = Bfs(f_node)

    # borrar --->
    deeper_level = 0
    x = list()
    size = 0
    # <---

    while not algorithm.isEmpty():
        # busco el siguiente nodo
        node: Node = algorithm.get_next()

        # actualizo los valorer
        new_level = node.level + 1

        # tester borrar --->
        """
        if new_level > deeper_level:
            deeper_level = new_level
            print("depper_level:" + str(deeper_level))
            
            if deeper_level == 6:
                end = time.perf_counter()
                return end - start
            """
        # <----

        # creeo todos los hijos
        current_cube = node.cube

        # borrar --->
        # start = time.perf_counter()
        # <---
        for axis in range(0, 3):
            for row in range(0, cb.n_row):
                for dire in range(0, 2):
                    # roto el cubo
                    if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
                        continue  # es el movimento que hace que vuelva al estado anterior

                    aux_cube = cb.rotate(current_cube, axis, row, dire)
                    # checkeo si es solucion
                    node_hash = cb.get_hash(aux_cube)

                    if node_hash == cb.init_hash:
                        print("solucion")
                        # end = time.perf_counter()
                        # print(end - start)
                        print(aux_cube)
                        exit()

                    # sino, llamo a add para que guarde el nodo
                    algorithm.add(aux_cube, new_level,(axis, row, dire), node_hash)


"""     # calcula en promedio cuánto tarda en procesar un node
        end = time.perf_counter()
        x.append(end - start)
        size += 1
        if size == 100000:
            print(sum(x) / len(x))
            x = list()
            size = 0
"""

algorithms(6)

"""
x = list()

for i in range(0, 10):
    x.append(algorithms())

print("termino")
print(x)
print(sum(x) / len(x))




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
    elif (hash_value in visited):
        pass
        # print(visited)
    elif (cube.is_done()):
        print('SOLUCION')  # Que pasa si el cubo esta termiando?
        print(cube.cube)
        exit()
"""""
