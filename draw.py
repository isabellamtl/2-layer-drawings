import matplotlib.pyplot as plt
import networkx as nx

# Zeichnet einen bipartiten Graphen mit gegebenen Knoten und Kanten
def draw_bipartite_graph(top, bottom, edge, name):
    G = nx.Graph()
    G.add_nodes_from(top, bipartite=0)
    G.add_nodes_from(bottom, bipartite=1)
    G.add_edges_from(edge)

    pos = {}
    # Positioniere die Knoten in zwei Schichten, Abstand der Knoten anpassen
    for i, node in enumerate(top):
        pos[node] = (i, 1)  # obere Schicht
    for i, node in enumerate(bottom):
        pos[node] = (i, 0)  # untere Schicht
    
    # Plot, Größe der Knoten und der Abbildung anpassen
    plt.figure(figsize=(8, 4))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightgray', edge_color='black')
    plt.axis('off')
    plt.savefig(f"{name}.png")


