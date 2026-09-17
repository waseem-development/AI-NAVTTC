import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


edge_list = [
    (1, 2), (2, 3), (3, 4),
    (4, 5), (5, 6), (6, 7),
    (2, 8), (8, 9), (9, 4)
]


# --------------------------------------------------
# Create Graph from Edge List
# --------------------------------------------------

# G = nx.Graph()
# G.add_edges_from(edge_list)

# A = nx.adjacency_matrix(G)

# print(A)           # Sparse representation of adjacency matrix
# print(A.toarray()) # Convert sparse matrix to normal NumPy array


# --------------------------------------------------
# Create Graph from NumPy Adjacency Matrix
# --------------------------------------------------

G = nx.from_numpy_array(np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 0, 0]
]))


# --------------------------------------------------
# Different Graph Drawing / Layout Functions
# --------------------------------------------------

# 1. SPRING LAYOUT
# Simulates physical forces:
#   - Connected nodes attract each other
#   - Unconnected nodes repel each other
# Produces a natural-looking graph.
#
# Good general-purpose layout.
#
# nx.draw_spring(G, with_labels=True)


# 2. CIRCULAR LAYOUT
# Places all nodes around a circle.
#
# Useful when you want a simple and symmetric visualization.
#
# nx.draw_circular(G, with_labels=True)


# 3. SHELL LAYOUT
# Places nodes in one or more concentric circles (shells).
#
# Useful for hierarchical or layered-looking graphs.
#
# nx.draw_shell(G, with_labels=True)


# 4. SPECTRAL LAYOUT
# Positions nodes using eigenvectors of the graph's
# Laplacian matrix.
#
# Nodes that are structurally related tend to appear
# closer together.
#
# Often useful for analyzing graph structure.
#
# nx.draw_spectral(G, with_labels=True)


# 5. PLANAR LAYOUT
# Attempts to draw the graph without edges crossing.
#
# Only works if the graph is planar.
# A planar graph can be drawn on a 2D plane without
# any two edges crossing.
#
# nx.draw_planar(G, with_labels=True)


# 6. RANDOM LAYOUT
# Places every node at a random position.
#
# The result can look different every time you run it.
# Mainly useful for testing or demonstrating layouts,
# NOT for understanding graph structure.
#
nx.draw_random(G, with_labels=True)


plt.show()