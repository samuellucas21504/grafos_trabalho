import networkx as nx


class GraphReader:
    @staticmethod
    def read_file(path) -> nx.Graph:
        file = open(path, "r")
        graph = nx.Graph()

        for line in file:
            node, edges = line.split('-')

            node = normalize_string(node)
            edges = normalize_string(edges)

            graph.add_node(node_for_adding=int(node))

            edges = edges.split(';')

            for edge in edges:
                edge, weight = edge.split(',')
                edge = normalize_string(edge)
                weight = normalize_string(weight)

                graph.add_edge(int(node), int(edge), weight=int(weight))

        return graph


def normalize_string_array(string_array: list[str]):
    new_array = []
    for n in string_array:
        new_array.append(normalize_string(n))

    return new_array


def normalize_string(string: str):
    return string.strip()
