import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph() # Undirected Graphs
# Gdi = nx.DiGraph() # Directed Graph
# MuG = nx.MultiGraph() # Multi-Undirected Graph
# MdiG = nx.DiMultiGraph() # Multi-directed Graph

# G.add_edge(1, 2) # Create an edge from 1->2
# G.add_edge(2, 3) # Create an edge from 2->3
# G.add_edge(3, 4, weight=0.9) # Weighted Graph
# G.add_edge("A", "B")
# G.add_edge("B", "B")
# G.add_edge("B", "C")
# G.add_node("C")
# G.add_node(print)
# G.add_edge("C", 1)
# G.add_edge(1, print)
# Visualize the Graph
# nx.draw_spring(G, with_labels=True)
# plt.show()



edge_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 8), (8, 9), (9, 4)]
# G = nx.from_edgelist(edge_list)
# G = nx.Graph(edge_list)
G = nx.Graph()
G.add_edges_from(edge_list)
nx.draw_spring(G, with_labels=True)
plt.show()