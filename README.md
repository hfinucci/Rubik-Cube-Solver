# TP1 Lado A: Rubik Cube Solver

## Integrantes:
* Cupitó, Felipe
* De Luca, Juan Manuel
* Finucci Roca, Hernán
* Kim, Azul
* Konfederak, Sol

## Consgina:
Implementacion de un motor de busqueda de soluciones de un Cubo Rubik de caras de NxN.


Este programa permite resolver este cubo mediante estos metodos de busqueda no informados:
- BPA
- BPP 
- BPPV

También lo puede resolver mediante estos metodos de busqueda informados:
- Greedy
- A*

También se implementaron 3 heuristicas para resolver el este problema

## Instalación
Para poder correr el proyecto es necesario tener instalado:
* Python 3
* NumPy

Para instalar las librerías:
```
pip install numpy
pip install matplotlib
```

## Ejecución

Se debe entra al archivo main.py y dentro de la funcion algorithms(num) se debe descomentar alguna de las soguientes lines para selecionar 
el metodo de busqueda deciado

```
    #algorithm = al.Dfs(f_node)
    algorithm = al.Bfs(f_node)
    # algorithm = al.Greedy(f_node, heu.colors)
    # algorithm = al.Greedy(f_node, heu.cubes)
    # algorithm = al.Greedy(f_node, heu.manhattanDistance)
    # algorithm = al.AStar(f_node, heu.colors)
    # algorithm = al.AStar(f_node, heu.cubes)
    # algorithm = al.AStar(f_node, heu.manhattanDistance)
```
Luego para ejecutar el algoritmo:
```
python3 main.py
```
o
```
python main.py