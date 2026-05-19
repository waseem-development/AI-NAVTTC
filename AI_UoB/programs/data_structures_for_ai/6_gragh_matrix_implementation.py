# Graph: 
# A = {1, 2, 3, 4, 5}  ==> Set each of this digit is the element of set and has 5 element
# B = {(1,2), (2,4), (3,6)} ==> 3 elements (ordered pairs)
# Now if we want to make a graph from B then we will represent each of these like this:
# 1 = (1,2)
# 2 = (2,4)
# 3 = (3,6)
# Now when we make its graph, it will be 1->2->3->1 
# Where - are the edges and 1,2,3 etc are vertices (vertex: Singular)
# But if we want to go from 1->3 then we will make a new edge because these edges are uni-directional

# --------------------- Types of Graph ---------------------
# 1) Undirected Graph
# 2) Directed Graph
# 3) Weighted Graph

# Memory Representation of Graph:
# 1) Matrix Representation
# 2) List Representation
# C = {(1,2), (2,3), (1,4)} i.e. 1->4,1->2->3->2
# We always make a square matrix where rows are sources and columns are destination
# If u have 4 vertices then it'll be 4x4 matrix, if u have 3 vertices then it'll be 3x3 matrix, u have 5 vertices then it'll be 5x5 matrix
#      1      2      3     4
#    ___________________________
# 1 |     |      |      |      |
# 2 |     |      |      |      |
# 3 |     |      |      |      |
# 4 |     |      |      |      |
#   ___________________________

# So by default we will put zero in each of these
#      1       2       3         4
#    _______________________________
# 1 |   0  |   0   |   0   |    0   |
# 2 |   0  |   0   |   0  |     0   |
# 3 |   0  |   0   |   0   |    0   |
# 4 |   0  |   0   |   0   |    0   |
#   _______________________________
# If we have 0 then it means there are no edges and if we have 1 then it means that edge is present

# Now for undirected graph:
#       1       2      3       4
#    _______________________________
# 1 |   0  |   1   |   0   |    1   |
# 2 |   1  |   0   |   1   |    0   |  
# 3 |   0  |   1   |   0   |    0   |
# 4 |   1  |   0   |   0   |    0   |
#   _______________________________   ===> Means we can go from 2->3 and 3->2

# Now for Undirected Graph is Symmetric Matrix

# Now for directed graph:
#       1       2      3       4
#    _______________________________
# 1 |   0  |   1   |   0   |    1   |
# 2 |   0  |   0   |   0   |    0   |  
# 3 |   0  |   1   |   0   |    0   |
# 4 |   0  |   0   |   0   |    0   |
#   _______________________________   

# Now for weighted graph: for example distance between 1->2 3 KM then 
#       1       2      3       4
#    _________________________________
# 1 |   0  |   3   |   0   |    10   |
# 2 |   0  |   0   |   0   |    0    |  
# 3 |   0  |   5   |   0   |    0    |
# 4 |   0  |   0   |   0   |    0    |
#   __________________________________   

# In our matrix vertical 1,2,3,4 etc are source and horizontal 1,2,3,4 are destination!
# mat[1][2] ==> 1 is source and 2 is destination and = 1 means make an edge between them
# mat[2][1] = 1
# mat[2][3] = 5 ==> weighted graph
# mat[2][3] = 0 ==> Edge deleted
# Benefit of Matrix Representation: This method is easier to code
# Disadvantage: Memory Wastage: Because all the 0's consume space too
# Dense Graph: When 1's are bigger ==> Use Matrix Representation
# Sparse Graph: When 1's are smaller ==> Do not use Matrix Representation

class Graph:
    def __init__(self, vertex):
        # Create a 2D adjacency matrix filled with 0s
        # ----------------------------------------------------------
        # Step 1:
        # [0] * vertex
        # If vertex = 4:
        # [0] * 4  -->  [0, 0, 0, 0]
        #
        # This creates ONE row containing 4 zeros.
        #
        # ----------------------------------------------------------
        # Step 2:
        # for x in range(vertex)
        # If vertex = 4:
        # range(4) --> 0,1,2,3
        #
        # The loop runs 4 times.
        #
        # ----------------------------------------------------------
        # Step 3:
        # Each iteration creates a NEW row:
        #
        # Iteration 1 --> [0,0,0,0]
        # Iteration 2 --> [0,0,0,0]
        # Iteration 3 --> [0,0,0,0]
        # Iteration 4 --> [0,0,0,0]
        #
        # Final Matrix:
        #
        # [
        #   [0,0,0,0],
        #   [0,0,0,0],
        #   [0,0,0,0],
        #   [0,0,0,0]
        # ]
        #
        # ----------------------------------------------------------
        # Why do we use list comprehension?
        #
        # Because each row becomes an independent list.
        #
        # WRONG WAY:
        # [[0]*vertex]*vertex
        #
        # Problem:
        # All rows point to SAME memory location.
        #
        # So changing one row changes all rows.
        #
        # Example:
        # mat[0][1] = 1
        #
        # WRONG OUTPUT:
        # [
        #   [0,1,0,0],
        #   [0,1,0,0],
        #   [0,1,0,0],
        #   [0,1,0,0]
        # ]
        #
        # This happens because rows are shared.
        #
        # ----------------------------------------------------------
        # CORRECT WAY:
        # [[0]*vertex for x in range(vertex)]
        #
        # Creates separate independent rows.
        #
        # Time Complexity: O(V²)
        # Space Complexity: O(V²)
        # where V = number of vertices
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):  # if we have weight and then in below lines inside the body of if block we will do = weight instead of = 1
        if ((0 <= src < self.size) and (0 <= dest < self.size)):
            # Boundary check: ensure both src and dest are valid indices
            # 0 <= src < self.size  --> src must not be negative and must not exceed matrix size
            # 0 <= dest < self.size --> dest must not be negative and must not exceed matrix size
            # If either is invalid, we skip everything below to avoid IndexError
    
            self.mat[src][dest] = 1  # Set edge from src --> dest (forward direction)
            self.mat[dest][src] = 1  # Set edge from dest --> src (backward direction)
                             # Both lines together make it an UNDIRECTED graph
                             # (two-way road: if 1->3 exists, 3->1 also exists)
        else:
            print("Invalid Edge")

    def remove_edge(self, src, dest):  
        # Check if indices are valid
        if ((0 <= src < self.size) and (0 <= dest < self.size)):
            
            # Remove edge in both directions (undirected graph)
            self.mat[src][dest] = 0
            self.mat[dest][src] = 0

        else:
            print("Invalid Edge")
            
    def print_graph(self):
        for row in self.mat:
            print(' '.join(map(str, row)))

G = Graph(5)
G.add_edge(0,1)
G.print_graph()
print("\n*********************\n")
G.add_edge(0,2)
G.print_graph()
print("\n*********************\n")
G.add_edge(1,3)
G.print_graph()
print("\n*********************\n")
G.add_edge(2,4)
G.print_graph()
print("\n*********************\n")
G.add_edge(3,4)
G.print_graph()
print("\n*********************\n")
G.add_edge(2,3)
G.print_graph()
print("\n*********************\n")
G.remove_edge(2,3)
G.print_graph()
print("\n*********************\n")