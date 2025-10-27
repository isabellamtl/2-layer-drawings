from draw import draw_bipartite_graph

class BipartiteGraph:
    def __init__(self, top_nodes, bottom_nodes, edges):
        self.top_nodes = top_nodes
        self.bottom_nodes = bottom_nodes
        self.edges = edges
      
    # Tausche zwei Bottom-Nodes basierend auf ihren Indizes
    def swap_bottom_nodes(self, index1, index2):    
        self.bottom_nodes[index1], self.bottom_nodes[index2] = self.bottom_nodes[index2], self.bottom_nodes[index1]
        return self

    # Zeichne den Graphen
    def _draw_graph(self,name):
        draw_bipartite_graph(self.top_nodes, self.bottom_nodes, self.edges, name)


