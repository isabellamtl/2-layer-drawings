import matplotlib.pyplot as plt
import networkx as nx


# Beispiel 

top_nodes = ['v_1', 'v_2', 'v_3', 'v_5']
bottom_nodes = ['w_4', 'w_2', 'w_3', 'w_1', 'w_5']
edges = [
    ('v_1', 'w_1'),
    ('v_1', 'w_2'),
    ('v_1', 'w_3'),
    ('v_2', 'w_2'),
    ('v_3', 'w_1'),
    ('v_3', 'w_2'),
    ('v_5', 'w_4'),
    ('v_5', 'w_5')
]

adj_list2 = {
    'v1': ['w1', 'w2'],
    'v2': ['w2'],
    'v3': ['w1', 'w2']
}

adj_list = {
    'v1': ['w1', 'w2', 'w3'],
    'v2': ['w2'],
    'v3': ['w1', 'w2'],
    'v5': ['w4', 'w5'],
}




# Knoten in zwei Mengen aufteilen
#top_nodes = list(adj_list.keys())
#bottom_nodes = list({w for ws in adj_list.values() for w in ws})




# Kanten hinzufügen
#for u in adj_list:
 #   for v in adj_list[u]:
 #       G.add_edge(u, v)

def draw_bipartite_graph(top, bottom, edge, name):
    G = nx.Graph()
    G.add_nodes_from(top, bipartite=0)
    G.add_nodes_from(bottom, bipartite=1)
    G.add_edges_from(edge)

    pos = {}
    # Positioniere die Knoten in zwei Schichten
    for i, node in enumerate(top):
        pos[node] = (i, 1)  # obere Schicht
    for i, node in enumerate(bottom):
        pos[node] = (i, 0)  # untere Schicht
    
    # Plot
    plt.figure(figsize=(8, 4))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgray', edge_color='black')
    plt.axis('off')
    plt.savefig(f"{name}.png")


# draw_bipartite_graph(top_nodes, bottom_nodes, edges , "graph1")