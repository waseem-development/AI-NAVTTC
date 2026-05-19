# Create a list of vertices
# Note: Whatever data structure you are using, in that each element must have a pointer with it
# Source
#  ____
# | 1 | --> | 2 | ptr | --> | 4 | ptr |
# ____
# | 2 | --> | 1 | ptr | --> | 4 | ptr |
# ____
# | 3 | --> | 4 | ptr | --> | 5 | ptr |
# ____
# | 4 | --> | 1 | ptr | --> | 3 | ptr | --> | 5 | ptr |
# ____
# | 5 | --> | 3 | ptr | --> | 5 | ptr |
# ____

# So here number of elements may vary. 
# It means that if we have source = 1, then the rest of the linkedlist will tell us the destination means if we start from vertex 1 then toward which nodes we can go to directly (not indirectly)
# WE need to make a array pointers 
# In python we can make a dictionary (key-value pair)
# Drawback: Task is a bit time consuming to code
# Drawback: Memory is not wasted but if numbr of edges is higher then it will use a lot of memory
# Benefit: This works dynamically

# Create a list of vertices
# Note: Whatever data structure you are using, in that each element must have a pointer with it
# Source
#  ____
# | 1 | --> | 2 | ptr | --> | 4 | ptr |
# ____
# | 2 | --> | 1 | ptr | --> | 4 | ptr |
# ____
# | 3 | --> | 4 | ptr | --> | 5 | ptr |
# ____
# | 4 | --> | 1 | ptr | --> | 3 | ptr | --> | 5 | ptr |
# ____
# | 5 | --> | 3 | ptr | --> | 5 | ptr |
# ____

# So here number of elements may vary. 
# It means that if we have source = 1, then the rest of the linkedlist will tell us the destination means if we start from vertex 1 then toward which nodes we can go to directly (not indirectly)
# WE need to make a array pointers 
# In python we can make a dictionary (key-value pair)
# Drawback: Task is a bit time consuming to code
# Drawback: Memory is not wasted but if numbr of edges is higher then it will use a lot of memory
# Benefit: This works dynamically

# =========================
# Graph using Adjacency List
# =========================

class Graph:
    def __init__(self):
        # Dictionary to store graph
        # Key = vertex, Value = list of neighbors
        self.adj_list = {}

    # ----------------- Add Vertex -----------------
    def add_vertex(self, vertex):
        # Add vertex only if it doesn't already exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print("Vertex already exists")

    # ----------------- Add Edge -----------------
    def add_edge(self, src, dest):
        # Ensure both vertices exist
        self.add_vertex(src)
        self.add_vertex(dest)

        # Add edge (undirected → both directions)
        if dest not in self.adj_list[src]:
            self.adj_list[src].append(dest)
        
        if src not in self.adj_list[dest]:
            self.adj_list[dest].append(src)

    # ----------------- Remove Edge -----------------
    def remove_edge(self, src, dest):
        # Check if both vertices exist
        if src in self.adj_list and dest in self.adj_list:
            
            # Remove dest from src
            if dest in self.adj_list[src]:
                self.adj_list[src].remove(dest)

            # Remove src from dest (undirected graph)
            if src in self.adj_list[dest]:
                self.adj_list[dest].remove(src)
        else:
            print("One or both vertices not found")

    # ----------------- Remove Vertex -----------------
    def remove_vertex(self, vertex):
        # Check if vertex exists
        if vertex not in self.adj_list:
            print("Vertex does not exist")
            return

        # Remove this vertex from all other adjacency lists
        for vertex in self.adj_list:
            if vertex in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vertex)

        # Finally delete the vertex
        del self.adj_list[vertex]

    # ----------------- Print Graph -----------------
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} --> {self.adj_list[vertex]}")


# =========================
# Testing the Graph
# =========================

G = Graph()

# Add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(3, 5)
G.add_edge(4, 5)

print("Graph after adding edges:")
G.print_graph()

print("\n-----------------------\n")

# Remove an edge
G.remove_edge(1, 3)
print("Graph after removing edge (1,3):")
G.print_graph()

print("\n-----------------------\n")

# Remove a vertex
G.remove_vertex(2)
print("Graph after removing vertex 2:")
G.print_graph()