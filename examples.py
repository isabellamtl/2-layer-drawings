from sort import *
from facetest3 import *

class BipartiteGraph:
    def __init__(self, top_nodes, bottom_nodes, edges):
        self.top_nodes = top_nodes
        self.bottom_nodes = bottom_nodes
        self.edges = edges
        self.adjacency = self._build_adjacency()

    def _build_adjacency(self):
        adj = {node: [] for node in self.top_nodes + self.bottom_nodes}
        for u, v in self.edges:
            adj[u].append(v)
            adj[v].append(u)  # Für ungerichteten Graph
        return adj

    def neighbors(self, node):
        return self.adjacency.get(node, [])
    
    def _draw_graph(self,name):
        draw_bipartite_graph(self.top_nodes, self.bottom_nodes, self.edges, name)


"""
# Beispiel 1
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
graph1 = BipartiteGraph(top_nodes, bottom_nodes, edges)

graph1._draw_graph("graph1")
sort(graph1)._draw_graph("sorted_graph1")

# Beispiel 2
top_nodes2 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6','v_7']
bottom_nodes2 = ['w_1', 'w_2', 'w_3','w_4','w_5','w_6']
edges2 = [
    ('v_1','w_1'),
    ('v_2','w_4'),
    ('v_3','w_2'),
    ('v_4','w_1'),
    ('v_4','w_6'),
    ('v_5','w_5'),
    ('v_6','w_3'),
    ('v_7','w_6'),
]

graph2 = BipartiteGraph(top_nodes2, bottom_nodes2, edges2)
graph2._draw_graph("graph2")
sort(graph2)._draw_graph("sorted_graph2")

# Beispiel 4
top_nodes4 = ['v_1', 'v_2','v_0', 'v_3','v_4','v_5','v_6']
bottom_nodes4 = ['w_0','w_02','w_1', 'w_2', 'w_3']
edges4 = [
    ('v_1','w_1'),
    ('v_2','w_3'),
    ('v_3','w_2'),
    ('v_4','w_1'),
    ('v_5','w_2'),
    ('v_6','w_3')
]
graph4 = BipartiteGraph(top_nodes4, bottom_nodes4, edges4)
graph4._draw_graph("graph4")
sort(graph4)._draw_graph("sorted_graph4")


# Beispiel 5
top_nodes5 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6','v_7','v_8']  # v6 weg gemacht (verbunden mit w3)
bottom_nodes5 = ['w_1', 'w_2','w_4','w_3','w_5','w_6']  # w3 weggemacht
edges5 = [
    ('v_1','w_1'),
    ('v_1','w_4'),
    ('v_2','w_4'),
    ('v_3','w_2'),
    ('v_4','w_1'),
    ('v_4','w_6'),
    ('v_5','w_5'),
    ('v_6','w_3'),
    ('v_8','w_2'),
    ('v_7','w_6'),
    ('v_8','w_5')
]
graph5 = BipartiteGraph(top_nodes5, bottom_nodes5, edges5)
graph5._draw_graph("graph5")
sort(graph5)._draw_graph("sorted_graph5")

# Beispiel 4.5
top_nodes4_5 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6','v_7','v_8','v_9','v_10','v_11','v_12']  # v6 weg gemacht (verbunden mit w3)
bottom_nodes4_5 = ['w_1', 'w_2', 'w_3','w_5','w_4','w_6']  
edges4_5 = [
    ('v_1','w_1'),
    ('v_2','w_3'),
    ('v_3','w_2'),
    ('v_4','w_1'),
    ('v_5','w_2'),
    ('v_6','w_3'),
    ('v_7','w_5'),
    ('v_8','w_4'),
    ('v_9','w_6'),
    ('v_10','w_4'),
    ('v_11','w_5'),
    ('v_12','w_6')

]
graph4_5 = BipartiteGraph(top_nodes4_5, bottom_nodes4_5, edges4_5)
graph4_5._draw_graph("graph4_5")
sort(graph4_5)._draw_graph("sorted_graph4_5")
    
# Beispiel 3
#top_nodes3 = ['v1', 'v2', 'v3','v4','v5','v6']
#bottom_nodes3 = ['w1', 'w2']
#edges3 = [
#    ('v1','w1'),
  #  ('v2','w2'),
   # ('v3','w2'),
   # ('v4','w1'),
   # ('v5','w1'),
   # ('v6','w2')
#]
#graph3 = BipartiteGraph(top_nodes3, bottom_nodes3, edges3)
#graph3._draw_graph("graph3")
#sort(graph3)._draw_graph("sorted_graph3")


# Beispiel 6
top_nodes6 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6']
bottom_nodes6 = ['w_1', 'w_3','w_2']  
edges6 = [
    ('v_1','w_1'),
    ('v_2','w_3'),
    ('v_3','w_2'),
    ('v_4','w_2'),
    ('v_5','w_1'),
    ('v_6','w_3')
]
graph6 = BipartiteGraph(top_nodes6, bottom_nodes6, edges6)
graph6._draw_graph("graph6")
sort(graph6)._draw_graph("sorted_graph6")


# Beispiel 7 
top_nodes7 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6']
bottom_nodes7 = ['w_1', 'w_2']
edges7 = [
    ('v_1','w_2'),
    ('v_2','w_1'),
    ('v_3','w_1'),
    ('v_4','w_2'),
    ('v_5','w_2'),
    ('v_6','w_1')
]
graph7 = BipartiteGraph(top_nodes7, bottom_nodes7, edges7)
graph7._draw_graph("graph7")
sort(graph7)._draw_graph("sorted_graph7")

# Beispiel 8 
top_nodes8 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6', 'v_7']
bottom_nodes8 = ['w_1', 'w_2']
edges8 = [
    ('v_1','w_2'),
    ('v_2','w_1'),
    ('v_3','w_1'),
    ('v_4','w_2'),
    ('v_5','w_1'),
    ('v_6','w_2'),
    ('v_7','w_1')
]
graph8 = BipartiteGraph(top_nodes8, bottom_nodes8, edges8)
graph8._draw_graph("graph8")
sort(graph8)._draw_graph("sorted_graph8")

# Beispiel 9
top_nodes9 = ['v_1', 'v_2', 'v_3','v_4','v_5','v_6', 'v_7', 'v_8', 'v_9']
bottom_nodes9 = ['w_2', 'w_1', 'w_3']
edges9 = [
    ('v_1','w_2'),
    ('v_2','w_1'),
    ('v_3','w_1'),
    ('v_4','w_2'),
    ('v_5','w_3'),
    ('v_6','w_1'),
    ('v_7','w_3'),
    ('v_8','w_2'),
    ('v_9','w_3')
]
graph9 = BipartiteGraph(top_nodes9, bottom_nodes9, edges9)
graph9._draw_graph("graph9")
sort(graph9)._draw_graph("sorted_graph9")

# Beispiel 10
top_nodes10 = ['v_1', 'v_2', 'v_3','v_4','v_45','v_5','v_6', 'v_7', 'v_8', 'v_9']
bottom_nodes10 = ['w_2', 'w_1', 'w_3']
edges10 = [
    ('v_1','w_2'),
    ('v_2','w_1'),
    ('v_3','w_1'),
    ('v_4','w_2'),
    ('v_45','w_1'),
    ('v_5','w_3'),
    ('v_6','w_1'),
    ('v_7','w_3'),
    ('v_8','w_2'),
    ('v_9','w_3')
]
graph10 = BipartiteGraph(top_nodes10, bottom_nodes10, edges10)
graph10._draw_graph("graph10")
sort(graph10)._draw_graph("sorted_graph10")
"""

# --------- Beispiele ------------

# 1: Intervall überlappt nicht und 2 Intervalle überlappen (möglich)
top1 = ['v1', 'v2', 'v3','v4','v5','v6', 'v7', 'v8', 'v9', 'v10']
bottom1 = ['w2', 'w1', 'w3']
edge1 = [
    ('v1','w1'),
    ('v2','w1'),
    ('v3','w1'),
    ('v4','w1'),
    ('v4','w2'),
    ('v5','w2'),
    ('v6','w2'),
    ('v8','w2'),
    ('v5','w3'),
    ('v7','w3'),
    ('v9','w3'),
    ('v10','w3'),
]

beispiel1 = BipartiteGraph(top1, bottom1, edge1)
beispiel1._draw_graph("Beispiel1")
sort(beispiel1)._draw_graph("Beispiel1_sorted")
print("Graph 1:")
check_intervals3(beispiel1)._draw_graph("Beispiel1_final")
print("")