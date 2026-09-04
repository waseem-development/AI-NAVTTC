"""
============================================
20 EXAMPLES: GRAPH LABELING TECHNIQUES
============================================
Complete guide to adding labels to NetworkX graphs
"""

import matplotlib
matplotlib.use('TkAgg')

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

print("=" * 70)
print("20 EXAMPLES: GRAPH LABELING TECHNIQUES")
print("=" * 70)



# ============================================
# EXAMPLE 1: Simple Node Labels (Default)
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 1: Simple Node Labels")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph
2. Draw with default labels
3. Labels are node numbers
"""

G1 = nx.cycle_graph(8)

plt.figure(figsize=(8, 6))
nx.draw(G1, 
        with_labels=True,           # Show labels
        node_color='lightblue',
        node_size=500,
        font_size=14,               # Label font size
        font_weight='bold',         # Bold labels
        font_color='darkblue')      # Label color
plt.title("Example 1: Default Node Labels (Numbers)")
plt.show(block=True)

print("✅ Example 1 completed")

# ============================================
# EXAMPLE 2: Custom Node Labels
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 2: Custom Node Labels")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph
2. Define custom labels
3. Apply custom labels
"""

G2 = nx.Graph()
G2.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Create custom labels
custom_labels = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D'
}

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G2, seed=42)

# Draw graph without labels first
nx.draw(G2, pos, node_color='lightgreen', node_size=500)

# Add custom labels
nx.draw_networkx_labels(G2, pos, labels=custom_labels, 
                        font_size=16, font_weight='bold', font_color='darkgreen')

plt.title("Example 2: Custom Node Labels")
plt.show(block=True)

print("✅ Example 2 completed")

# ============================================
# EXAMPLE 3: Different Label Positions
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 3: Label Positions")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph
2. Position labels above nodes
3. Different alignment
"""

G3 = nx.star_graph(5)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G3, seed=42)

# Draw nodes and edges
nx.draw_networkx_nodes(G3, pos, node_color='lightcoral', node_size=500)
nx.draw_networkx_edges(G3, pos)

# Add labels with offset (above nodes)
labels = {node: f'N{node}' for node in G3.nodes()}
label_pos = {node: (x, y + 0.05) for node, (x, y) in pos.items()}
nx.draw_networkx_labels(G3, label_pos, labels=labels, font_size=12)

plt.title("Example 3: Labels Above Nodes")
plt.show(block=True)

print("✅ Example 3 completed")

# ============================================
# EXAMPLE 4: Edge Labels (Weights)
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 4: Edge Labels (Weights)")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph with weights
2. Extract edge labels
3. Display edge labels
"""

G4 = nx.Graph()
G4.add_weighted_edges_from([
    (1, 2, 5),
    (2, 3, 3),
    (3, 4, 7),
    (4, 1, 2),
    (1, 3, 4)
])

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G4, seed=42)

# Draw graph
nx.draw(G4, pos, with_labels=True, node_color='lightblue', 
        node_size=500, font_size=14)

# Add edge labels (weights)
edge_labels = nx.get_edge_attributes(G4, 'weight')
nx.draw_networkx_edge_labels(G4, pos, edge_labels=edge_labels, 
                            font_size=12, font_color='red')

plt.title("Example 4: Edge Labels (Weights)")
plt.show(block=True)

print("✅ Example 4 completed")

# ============================================
# EXAMPLE 5: Custom Edge Labels
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 5: Custom Edge Labels")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph
2. Define custom edge labels
3. Display custom labels
"""

G5 = nx.Graph()
G5.add_edges_from([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('D', 'A')
])

# Custom edge labels
custom_edge_labels = {
    ('A', 'B'): 'Friend',
    ('B', 'C'): 'Colleague',
    ('C', 'D'): 'Family',
    ('D', 'A'): 'Neighbor'
}

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G5, seed=42)

nx.draw(G5, pos, with_labels=True, node_color='lightgreen', 
        node_size=500, font_size=14, font_weight='bold')

nx.draw_networkx_edge_labels(G5, pos, edge_labels=custom_edge_labels,
                            font_size=11, font_color='blue')

plt.title("Example 5: Custom Edge Labels")
plt.show(block=True)

print("✅ Example 5 completed")

# ============================================
# EXAMPLE 6: Node Labels with Attributes
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 6: Node Labels with Attributes")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph with node attributes
2. Create labels from attributes
3. Display attribute labels
"""

G6 = nx.Graph()
# Add nodes with attributes
G6.add_node(1, name='Alice', age=25)
G6.add_node(2, name='Bob', age=30)
G6.add_node(3, name='Charlie', age=35)
G6.add_node(4, name='Diana', age=28)
G6.add_edges_from([(1,2), (2,3), (3,4), (4,1)])

# Create labels from attributes
node_labels = {node: f"{G6.nodes[node]['name']}\n({G6.nodes[node]['age']})" 
               for node in G6.nodes()}

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G6, seed=42)

nx.draw(G6, pos, node_color='lightcoral', node_size=800)
nx.draw_networkx_labels(G6, pos, labels=node_labels, font_size=10)

plt.title("Example 6: Node Labels with Attributes")
plt.show(block=True)

print("✅ Example 6 completed")

# ============================================
# EXAMPLE 7: Combined Node and Edge Labels
# ============================================

print("\n" + "=" * 60)
print("EXAMPLE 7: Combined Node and Edge Labels")
print("=" * 60)

"""
STEP BY STEP:
1. Create graph with weights
2. Add both node and edge labels
"""

G7 = nx.Graph()
G7.add_nodes_from(['A', 'B', 'C', 'D'])
G7.add_weighted_edges_from([
    ('A', 'B', 5),
    ('B', 'C', 3),
    ('C', 'D', 7),
    ('D', 'A', 2)
])

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G7, seed=42)

# Draw graph
nx.draw(G7, pos, node_color='lightyellow', node_size=700)

# Node labels
node_labels = {node: f"★ {node}" for node in G7.nodes()}
nx.draw_networkx_labels(G7, pos, labels=node_labels, font_size=14)

# Edge labels
edge_labels = nx.get_edge_attributes(G7, 'weight')
edge_labels = {k: f"w={v}" for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(G7, pos, edge_labels=edge_labels, 
                            font_size=10, font_color='blue')

plt.title("Example 7: Combined Node and Edge Labels")
plt.show(block=True)

print("✅ Example 7 completed")