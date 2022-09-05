import cube as cb
import heuristics as heu
import algorithms as al
import time

def algorithms(num):
    # Creó el cubo
    f_cube = cb.init_cube(3)

    # mezclo el cubo
    f_cube = cb.mix_up(f_cube, num)

    # creo el nodo raiz
    f_node = al.Node(f_cube, 0, (-1, -1, -1))

    # creo el arbol
    # algorithm = al.Dfs(f_node)
    # algorithm = al.Bfs(f_node)
    algorithm = al.AStar(f_node, heu.manhattanDistance)
    #algorithm = al.Greedy(f_node, heu.manhattanDistance)


    while not algorithm.isEmpty():
        # busco el siguiente nodo
        node: al.Node = algorithm.get_next()

        # actualizo los valorer
        new_level = node.level + 1
        print(new_level)

        # creeo todos los hijos
        state = node.cube
        for axis in range(0, 3):
            for row in range(0, cb.n_row):
                for dire in range(0, 2):
                    # roto el cubo
                    if axis == node.rotate[0] and row == node.rotate[1] and dire == (node.rotate[2] + 1) % 2:
                        continue  # es el movimento que hace que vuelva al estado anterior

                    new_state = cb.rotate(state, axis, row, dire)
                    # checkeo si es solucion
                    node_hash = cb.get_hash(new_state)

                    if node_hash == cb.init_hash:
                        print("solucion")
                        print(new_state)
                        exit()

                    # sino, llamo a add para que guarde el nodo
                    algorithm.add(new_state, new_level, (axis, row, dire), node_hash)



start = time.perf_counter()
algorithms(5)
end = time.perf_counter()
print(end - start)
