# 📌 Q1. Write a class Graph to implement adjacency matrix representation of a simple undirected graph
class Graph:

    # 📌 Q2. Constructor to initialize vertex_count and adjacency matrix
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        
        # Creating a 2D matrix (list of lists) filled with 0s
        # Each cell [i][j] represents the presence (or absence) of an edge between vertex i and vertex j
        self.adj_matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    # 📌 Q3. Add an edge with optional weight (default is 1)
    def add_edge(self, u, v, weight=1):
        # For an undirected graph, update both [u][v] and [v][u]
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight

    # 📌 Q4. Remove an edge between vertex u and v
    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    # 📌 Q5. Check whether two vertices are connected (has an edge)
    def has_edge(self, u, v):
        return self.adj_matrix[u][v] != 0

    # 📌 Q6. Print the adjacency matrix
    def print_adj_matrix(self):
        print("🔗 Adjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

# 🧪 Creating a graph with 3 vertices
g = Graph(3)

# ➕ Adding edges
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)

# 🔍 Checking connectivity
print("(0, 1) has edge:", g.has_edge(0, 1))  # True
print("(0, 2) has edge:", g.has_edge(0, 2))  # True
print("(0, 0) has edge:", g.has_edge(0, 0))  # False (no self loop added)

# 🖨️ Printing adjacency matrix
print("\nBefore removing any edge:")
g.print_adj_matrix()

# ➖ Removing an edge
g.remove_edge(0, 1)

# 🖨️ Printing matrix again after removal
print("\nAfter removing edge (0, 1):")
g.print_adj_matrix()


## -------------
## Documentation:

"""
📄 Documentation: Adjacency Matrix Graph Implementation

✅ Graph Type: Simple, Undirected Graph
✅ Representation: Adjacency Matrix

🔧 Class: Graph
- Used to represent a graph using a 2D matrix.
- Each cell (i, j) in the matrix stores the weight of the edge between vertex i and j.
- Since it's undirected, matrix[i][j] = matrix[j][i].

🧱 Methods:

1. __init__(vertex_count):
   - Initializes the graph with a given number of vertices.
   - Creates a vertex_count x vertex_count matrix filled with 0s.

2. add_edge(u, v, weight=1):
   - Adds an edge between vertex u and v with an optional weight (default is 1).
   - Since it's undirected, sets both adj_matrix[u][v] and adj_matrix[v][u].

3. remove_edge(u, v):
   - Removes the edge between vertex u and v by setting corresponding matrix cells to 0.

4. has_edge(u, v):
   - Returns True if an edge exists between u and v (i.e., matrix value is not 0).

5. print_adj_matrix():
   - Prints the adjacency matrix in a readable format.

🧪 Example Use Case:

    g = Graph(3)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)

    g.print_adj_matrix()
    g.remove_edge(0, 1)
    g.print_adj_matrix()

📌 Adjacency Matrix is ideal when:
- The graph is dense (many edges)
- Constant-time edge checks are needed

🧠 Time Complexity:
- add_edge, remove_edge, has_edge → O(1)
- Space Complexity → O(V^2) where V = number of vertices
"""
