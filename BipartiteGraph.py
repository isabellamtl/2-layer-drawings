from draw import draw_bipartite_graph

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


