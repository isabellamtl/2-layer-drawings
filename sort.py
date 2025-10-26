from BipartiteGraph import *
from collections import defaultdict

def sort(graph):
    top_index = {node: i for i, node in enumerate(graph.top_nodes)}

    # Zuordnung: bottom_node → Liste von Top-Node-Indizes
    bottom_to_top_indices = defaultdict(list)
    for u, v in graph.edges:
        if u in top_index:  # u = top_node
            bottom_to_top_indices[v].append(top_index[u])
        elif v in top_index:  # v = top_node
            bottom_to_top_indices[u].append(top_index[v])

    # Berechne Durchschnittsindex
    bottom_avg_index = {
        b: sum(indices) / len(indices)
        for b, indices in bottom_to_top_indices.items()
    }

    sorted_bottom_nodes = sorted(graph.bottom_nodes, key=lambda b: bottom_avg_index.get(b, float('inf')))

    sorted_graph = BipartiteGraph(graph.top_nodes, sorted_bottom_nodes, graph.edges)
    return sorted_graph

