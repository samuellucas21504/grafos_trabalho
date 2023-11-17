from itertools import count
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

        # Pega o primeiro nó do grafo
        node = nodes.pop()
        # Lista que armazena a mst
        frontier = []
        # Visitados
        visited = {node}

        # pega os vértices e respectivos pesos conectados ao primeiro nó
        for destination_node, weight_dict in graph.adj[node].items():
            # pega o valor do peso no dicionario
            edge_weight = weight_dict.get(weight_key, 1)

            optic_fiber_price = edge_weight * CONSTANTS.OPTIC_FIBER_PRICE_PER_METER.value

            # adiciona em frontier o peso, o passo,
            # o nó atual, o nó de destino e o dicionário de peso
            heappush(frontier, (edge_weight, next(c), node, destination_node, weight_dict, optic_fiber_price))

        # enquanto houver nós e dados na tupla frontier, continuar
        while nodes and frontier:
            # separa o int peso, o passo (descartado), o nó atual, o nó de destino, o dict
            # de peso e o preco da fibra optica
            weight_value, _, node, destination_node, weight_dict, optic_fiber_price = heappop(frontier)

            # Se o nó destino estiver em visitados e nao estiver nos nós não
            # visitados ignora
            if destination_node in visited or destination_node not in nodes:
                continue

            # Adiciona o nó atual, o nó destino e o peso do vértice
            yield node, destination_node, weight_dict, {CONSTANTS.OPTIC_FIBER_KEY.value: optic_fiber_price}

            # Adiciona nó destino aos visitados
            visited.add(destination_node)
            # Retira esse nó da lista dos nós iniciais
            nodes.discard(destination_node)

            # Analisa os nós adjacentes desse nó adiciona
            for node, edge_weights in graph.adj[destination_node].items():
                # Verifica se o nó está na lista de visitados, se estiver ignora
                if node in visited:
                    continue

                # Pega valor do peso
                edge_weight = edge_weights.get(weight_key, 1)
                optic_fiber_price = edge_weight * CONSTANTS.OPTIC_FIBER_PRICE_PER_METER.value

                # Adiciona em frontier
                heappush(frontier, (edge_weight, next(c), destination_node, node, edge_weights, optic_fiber_price))

    @staticmethod
    def kruskal(graph: nx.Graph):
        # Utilizamos de um DisjointedSet (UnionFind) para armazenar tuplas
        # que não são iguais
        union_find = UnionFind()
        # Separamos os vértices e mantemos os pesos
        edges = graph.edges(data=True)
        # Utilizamos da chave 'weight' que é a padrão do networkX (caso utilizada outra,
        # tem que mudar também na criacao do grafo
        weight_key = 'weight'
        # vértices com peso
        weighted_edges = []

        # para cada vértice nas vértices
        for e in edges:
            # pega o dicionário de peso
            weight_dict = e[-1]
            # pega o valor do dicionário
            weight = weight_dict.get(weight_key, 1)
            # adiciona o valor do peso no começo da tupla, para classificação futura
            edge = (weight,) + e
            # adiciona esse na lista de vértices abertos
            weighted_edges.append(edge)

        # ordena a lista de vértices abertos
        # Como o primeiro valor da tupla é o peso, eles serão ordenados por peso
        sorted_edges = sorted(weighted_edges, key=itemgetter(0))

        del weighted_edges

        # passa por todos os vértices, ordenados por peso
        for weight, current_node, destiny_node, weight_dict in sorted_edges:
            # verifica se o disjointed já conectou o nó atual e o nó de destino
            if union_find[current_node] != union_find[destiny_node]:
                optic_fiber_price = weight * CONSTANTS.OPTIC_FIBER_PRICE_PER_METER.value

                # retorna o nó atual, o nó destino e o dicionário de peso
                yield current_node, destiny_node, weight_dict, {CONSTANTS.OPTIC_FIBER_KEY.value: optic_fiber_price}

                # faz a união de sets do nó atual com o nó destino
                union_find.union(current_node, destiny_node)
