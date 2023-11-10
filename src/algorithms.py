from itertools import count
from math import ceil
from operator import itemgetter

import networkx as nx
from heapq import heappop, heappush

from networkx.utils import UnionFind

from src.constants import CONSTANTS


class Algorithms:

    @staticmethod
    def prims(graph: nx.Graph):
        # Chave que é usada para pegar o valor do peso no dicionario
        weight_key = 'weight'

        nodes = set(graph)
        c = count()

        while nodes:
            # Pega o primeiro nó do grafo
            current_node = nodes.pop()
            # Lista que armazena a mst
            frontier = []
            # Visitados
            visited = {current_node}

            # pega os vértices e respectivos pesos conectados a um nó
            for edge, weight_dict in graph.adj[current_node].items():
                # pega o valor do peso no dicionario
                wt = weight_dict.get(weight_key, 1)
                optic_fiber_price = ceil(wt * CONSTANTS.OPTIC_FIBER_PRICE_PER_METER.value)

                # adiciona na lista o peso, o próximo nó a ser validado,
                # o nó atual, o nó de destino e o dicionário de peso
                heappush(frontier, (wt, next(c), current_node, edge, weight_dict, optic_fiber_price))

            # passa por todos os nós e por todos os pontos da lista de vértices
            while nodes and frontier:
                # separa o int peso, o próximo nó, o nó atual, o nó de destino, o dict
                # de peso e o preco da fibra optica
                W, _, current_node, edge, weight_dict, optic_fiber_price = heappop(frontier)

                # Se o nó destino estiver em visitados e nao estiver nos nós não
                # visitados ignora
                if edge in visited or edge not in nodes:
                    continue
                # Adiciona o nó atual, o nó destino e o peso do vértice
                yield current_node, edge, weight_dict, {'optic_fiber_price': f'R$ {optic_fiber_price}'}

                # Adiciona nó destino aos visitados
                visited.add(edge)
                # Retira esse nó da lista dos não visitados
                nodes.discard(edge)

                # Passa por todos os vértices do nó
                for n2, d2 in graph.adj[edge].items():
                    # Verifica se o nó está na lista de visitados, se estiver ignora
                    if n2 in visited:
                        continue

                    # Pega valor do peso
                    new_weight = d2.get(weight_key, 1)

                    # Adiciona na lista
                    heappush(frontier, (new_weight, next(c), edge, n2, d2, optic_fiber_price))

    @staticmethod
    def Kruskal(graph: nx.Graph):
        # Como estamos utilizando o networkX, temos que usar o UnionFind() para
        # armazenar as sub arvores
        subtrees = UnionFind()
        # Separamos os vértices e mantemos os pesos
        edges = graph.edges(data=True)
        # Utilizamos da chave 'weight' que é a padrão do networkX (caso utilizada outra,
        # tem que mudar também na criacao do grafo
        weight_key = 'weight'
        # vértices incluídas
        included_edges = []
        # vértices abertas
        open_edges = []

        # para cada vértice nas vértices
        for e in edges:
            # pega o dicionário de peso
            weight_dict = e[-1]
            # pega o valor do dicionário
            weight = weight_dict.get(weight_key, 1)
            # adiciona o valor do peso no começo da tupla, para classificação futura
            edge = (weight,) + e
            # adiciona esse na lista de vértices abertos
            open_edges.append(edge)

        # ordena a lista de vértices abertos
        # Como o primeiro valor da tupla é o peso, eles serão ordenados por peso
        sorted_open_edges = sorted(open_edges, key=itemgetter(0))

        # adiciona todas as listas recursivamente e deleta suas referencias
        # mantem apenas os nós ordenados(sorted_edges)
        included_edges.extend(sorted_open_edges)
        sorted_edges = included_edges
        del open_edges, sorted_open_edges, included_edges

        # passa por todos os nós ordenados
        for weight, current_node, destiny_node, weight_dict in sorted_edges:
            # verifica se a sub árvore do nó atual é diferente do da sub árvore do
            # nó destino
            if subtrees[current_node] != subtrees[destiny_node]:
                optic_fiber_price = weight * CONSTANTS.OPTIC_FIBER_PRICE_PER_METER.value

                # retorna o nó atual, o nó destino e o dicionário de peso
                yield current_node, destiny_node, weight_dict, {'optic_fiber_price': f'R${optic_fiber_price}'}

                # faz a união da subárvore do nó atual com o nó destino
                subtrees.union(current_node, destiny_node)
