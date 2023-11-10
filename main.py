import time

from src.graph_reader import GraphReader
from src.algorithms import Algorithms
from src.graph_drawer import GraphDrawer

# Le o arquivo e o adiciona em um grafo networkx
graph = GraphReader.read_file(path='./input/grafo.txt')

GraphDrawer.draw(graph)

print('ALGORITMO PRIMS - MINIMUM SPANNING TREE')
t = time.process_time()
print(sorted(Algorithms.prims(graph)))
elapsed_time = time.process_time() - t

print('Tempo Gasto pelo algoritmo prims =', elapsed_time, 's\nComplexidade = O(log(n))\n\n')

print('ALGORITMO KRUSKAL - MINIMUM SPANNING TREE')
t = time.process_time()
print(sorted(Algorithms.Kruskal(graph)))
elapsed_time = time.process_time() - t

print('Tempo Gasto pelo algoritmo kruskal =', elapsed_time, 's\nComplexidade = O(log(n))')
