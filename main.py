import time

from src.constants import CONSTANTS
from src.graph_reader import GraphReader
from src.algorithms import Algorithms
from src.graph_drawer import GraphDrawer

# Le o arquivo e o adiciona em um grafo networkx
graph = GraphReader.read_file(path='./input/grafo.txt')

GraphDrawer.draw(graph)

print('ALGORITMO PRIMS - MINIMUM SPANNING TREE')
t = time.process_time()
prim_generator = sorted(Algorithms.prims(graph))
elapsed_time = time.process_time() - t
total_cost = 0

for tup in prim_generator:
    print(tup)
    total_cost += tup[-1].get(CONSTANTS.OPTIC_FIBER_KEY.value)

print(f'\nCusto total de fibra óptica: R$ {total_cost}')
print('Tempo Gasto pelo algoritmo prims =', elapsed_time, 's\nComplexidade = O(E * log(n))\n')

print('ALGORITMO KRUSKAL - MINIMUM SPANNING TREE')
t = time.process_time()
kruskal_generator = sorted(Algorithms.kruskal(graph))
elapsed_time = time.process_time() - t
total_cost = 0

for tup in kruskal_generator:
    print(tup)
    total_cost += tup[-1].get(CONSTANTS.OPTIC_FIBER_KEY.value)

print(f'\nCusto total de fibra óptica: R$ {total_cost}')
print('Tempo Gasto pelo algoritmo kruskal =', elapsed_time, 's\nComplexidade = O(E * log(n))')
