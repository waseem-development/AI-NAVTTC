import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1, 2, 3, 4,])

G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1)
])

print(G.nodes())
print(G.edges())

print(G.nodes())
print(G.edges())

print(G.degree())
print(nx.degree_centrality(G))

nx.draw(G, with_labels=True)
plt.show()

