import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def ist_bipartit_und_grad_2(adj_matrix):
    n = len(adj_matrix)
    # Grad überprüfen
    for i in range(n):
        if sum(adj_matrix[i]) != 2:
            raise ValueError(f"Knoten {i} hat Grad {sum(adj_matrix[i])} (≠ 2)")

    # Bipartit-Test mit BFS
    layer = [-1] * n  # -1 = nicht besucht, 0 und 1 = Layer
    for start in range(n):
        if layer[start] == -1:
            queue = [start]
            layer[start] = 0
            while queue:
                node = queue.pop(0)
                for nachbar, verbunden in enumerate(adj_matrix[node]):
                    if verbunden:
                        if layer[nachbar] == -1:
                            layer[nachbar] = 1 - layer[node]
                            queue.append(nachbar)
                        elif layer[nachbar] == layer[node]:
                            raise ValueError("Graph ist nicht bipartit")
    return layer

def baue_2layer_zeichnung(adj_matrix, layer):
    n = len(adj_matrix)
    besucht = [False] * n
    pos = {}
    layer0_x = 0
    layer1_x = 0
    G = nx.Graph()
    
    for start in range(n):
        if besucht[start]:
            continue
        pfad = [] # Starte neuen Pfad einer Zusammenhangskomponente
        current = start
        prev = -1
        # Konstruiere Pfad
        while not besucht[current]:
            besucht[current] = True
            pfad.append(current)
            nachbarn = [i for i, v in enumerate(adj_matrix[current]) if v and i != prev]
            if not nachbarn:
                break
            prev = current
            current = nachbarn[0]
        
        # Platziere Pfad in Layer 0 und 1
        x = max(layer0_x, layer1_x) # Pfade werden nebeneinander gezeichnet
        for idx, node in enumerate(pfad):
            if layer[node] == 0:
                pos[node] = (x, 0)
                x += 1
                layer0_x = x
            else:
                pos[node] = (x, -1)
                x += 1
                layer1_x = x

        # Kanten hinzufügen
        for i in range(len(pfad)):
            for j in range(i + 1, len(pfad)):
                if adj_matrix[pfad[i]][pfad[j]]:
                    G.add_edge(pfad[i], pfad[j])

    return G, pos


# Graph auf 2 Layer zeichnen
def zeichne_graph(G, pos, dateiname="drawing.png"):
    plt.figure(figsize=(10, 4))
    nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="black", node_size=1000)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(dateiname, dpi=300)


# Beispiele
adj_matrix1 = [
    [0,1,1,0,0,0],  
    [1,0,0,1,0,0],  
    [1,0,0,0,1,0],  
    [0,1,0,0,0,1],  
    [0,0,1,0,0,1],  
    [0,0,0,1,1,0]   
]

adj_matrix2 = [
    [0,1,0,0,0,0,1,0,0,0,0,0],  
    [1,0,0,0,0,0,0,0,0,0,0,1],   
    [0,0,0,1,0,0,0,0,0,0,0,1],  
    [0,0,1,0,1,0,0,0,0,0,0,0],  
    [0,0,0,1,0,1,0,0,0,0,0,0], 
    [0,0,0,0,1,0,1,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,1,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,0]  
]

# nicht Grad 2 überall
adj_matrix3 = [
    [0,1,1,1,0,0],  
    [1,0,0,1,0,0], 
    [1,0,1,0,1,0],  
    [0,1,0,0,0,1],  
    [0,1,1,0,1,1],  
    [0,0,0,1,1,0]
]

# nicht bipartit
adj_matrix4 = [
    [0,1,0,1],  
    [1,0,0,1],  
    [1,0,0,1],  
    [1,1,0,0]  
]

# Beispiel zum Testen einsetzen
adj_matrix = np.array(adj_matrix2)

try:
    layer = ist_bipartit_und_grad_2(adj_matrix)
    G, pos = baue_2layer_zeichnung(adj_matrix, layer)
    zeichne_graph(G, pos)
except ValueError as e:
    print("Fehler:", e)
