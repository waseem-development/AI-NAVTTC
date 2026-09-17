import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# G = nx.complete_graph(4)
G = nx.complete_graph(5)
nx.draw_spring(G, with_labels=True)
plt.show()