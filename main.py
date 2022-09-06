import cube as cb
import heuristics as heu
import algorithms as al
import time


def algorithms(f_cube, algorithm):
    # Creó el cubo
    # f_cube = cb.init_cube(3)

    # mezclo el cubo
    # f_cube = cb.mix_up(f_cube, num)

    # creo el nodo raiz
    f_node = al.Node(f_cube, 0, (-1, -1, -1))

    # creo el arbol
    # algorithm = al.Dfs(f_node)
    # algorithm = al.Bfs(f_node)
    # algorithm = al.AStar(f_node, heu.manhattanDistance)
    # algorithm = al.Greedy(f_node, heu.colors)

    explored = 0
    while not algorithm.isEmpty():
        start_node = time.perf_counter()

        # busco el siguiente nodo
        node: al.Node = algorithm.get_next()

        # actualizo los valorer
        new_level = node.level + 1

        # creeo todos los hijos
        state = node.cube
        for axis in range(0, 3):
            for row in range(0, cb.n_row):
                for dire in range(0, 2):
                    # descartó las rotaciones que no son necesarias
                    if row == cb.n_row // 2:
                        continue
                    if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
                        continue  # es el movimento que hace que vuelva al estado anterior

                    # roto el cubo
                    new_state = cb.rotate(state, axis, row, dire)

                    # obtengo el hash del nuevo estado
                    node_hash = cb.get_hash(new_state)

                    # checkeo si es solucion
                    if node_hash == cb.init_hash:
                        print("explorados: "+str(explored))
                        print("nivel: "+str(new_level))
                        return

                    # sino, llamo a add para que guarde el nodo

                    if algorithm.add(new_state, new_level, (axis, row, dire), node_hash):
                        explored += 1

f_cube = cb.init_cube(3)
f_cube = cb.mix_up(f_cube,8)
algorithm = []
names = []
f_node = al.Node(f_cube, 0, (-1, -1, -1))
algorithm.append(al.Bfs(f_node))
names.append("BFS")
# algorithm.append(al.Dfs(f_node))
# names.append("DFS")
algorithm.append(al.AStar(f_node, heu.manhattanDistance))
names.append("AStar con manhattan")
algorithm.append(al.AStar(f_node, heu.colors))
names.append("AStar con colors")
algorithm.append(al.AStar(f_node, heu.cubes))
names.append("AStar con cubes")
algorithm.append(al.Greedy(f_node, heu.manhattanDistance))
names.append("Greedy con manhattan")
# algorithm.append(al.Greedy(f_node, heu.colors))
# names.append("Greedy con colors")
# algorithm.append(al.Greedy(f_node, heu.cubes))
# names.append("Greedy con cubes")
for i in range(0,7):
    start = time.perf_counter()
    algorithms(f_cube, algorithm[i])
    end = time.perf_counter()
    print(names[i]+" tardo "+str(end-start))
    print("------------")
    