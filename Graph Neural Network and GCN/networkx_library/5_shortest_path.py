import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1, 2), (3, 4), (4, 5), (5, 6), (6, 7), (2, 8), (8, 9), (9, 4)]
G = nx.Graph()
G.add_edges_from(edge_list)

print(nx.shortest_path(G, 2, 4))

nx.draw_planar(G, with_labels=True)
plt.show()