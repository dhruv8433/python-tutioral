class Graph:
    def __init__(self):
        self.adj_list = {}  # Dictionary to hold the adjacency list

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        # Add the edge u -> v and v -> u (undirected graph)
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]

    def print_graph(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

# Create graph and add vertices and edges
graph = Graph()

for v in ['A', 'B', 'C', 'D']:
    graph.add_vertex(v)

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.print_graph()
