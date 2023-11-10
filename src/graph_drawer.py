import networkx as nx
import matplotlib.pyplot as plt

class GraphDrawer:
    @staticmethod
    def draw(graph: nx.Graph):
        # Adiciona uma seed para reproduzir sempre o mesmo grafo
        pos = nx.spring_layout(graph, seed=7)

        # Desenha os nós
        nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='#809fff')

        # Desenha os vértices
        nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, width=3, edge_color='#33ccff', style='dashed')

        # Desenha os textos referentes aos grafos
        nx.draw_networkx_labels(graph, pos, font_size=20, font_family='sans-serif', font_color='w')

        # Desenha os textos referentes aos pesos do vértice
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels)

        # Plota e mostra em tela
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig("./output/graph.jpg")

        plt.show()