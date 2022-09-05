from collections import deque
from queue import PriorityQueue
from dataclasses import dataclass


@dataclass(order=True)
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
            return True
        return False

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
            return True
        return False

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
        self.list.put((0, fist_node))
        self.heuristic = heuristic

    def add(self, aux_cube, level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            node = Node(aux_cube, level, settings)
            h_value = self.heuristic(node)
            self.list.put(((level + h_value), node))
            return True
        return False

    def get_next(self):
        return self.list.get()[1]

    def isEmpty(self):
        return self.list.empty()


# Igual que AStar pero la prioridad del priority queue solo se ve afectada por la herisitca
class Greedy:
    def __init__(self, fist_node, heuristic):
        self.list = PriorityQueue()
        self.visited = set()
        self.list.put((0, fist_node))
        self.heuristic = heuristic

    def add(self, aux_cube, level, settings, node_hash):
        if node_hash not in self.visited:
            self.visited.add(node_hash)
            node = Node(aux_cube, level, settings)
            h_value = self.heuristic(node)
            self.list.put((h_value, node))
            return True
        return False

    def get_next(self):
        return self.list.get()[1]

    def isEmpty(self):
        return self.list.empty()
