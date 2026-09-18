import networkx as nx
import matplotlib.pyplot as plt

# edge_list = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]

# G = nx.Graph()
# G.add_edges_from(edge_list)

# print(dict(G.degree)[2])

# nx.draw_spring(G, with_labels=True)
# plt.show()

edge_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
G = nx.DiGraph()
G.add_edges_from(edge_list)

print(dict(G.in_degree)[3])
print(dict(G.out_degree)[3])
print(dict(G.degree)[3])

nx.draw_spring(G, with_labels=True)
plt.show()