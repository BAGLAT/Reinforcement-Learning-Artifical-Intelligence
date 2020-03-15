#https://www.datacamp.com/community/tutorials/networkx-python-graph-tutorial
#https://www-m9.ma.tum.de/graph-algorithms/directed-chinese-postman/index_en.html

import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

print("Hello World!")

edgelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/e570c38bcc72a8d102422f2af836513b/raw/89c76b2563dbc0e88384719a35cba0dfc04cd522/edgelist_sleeping_giant.csv')
nodelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/f989e10af17fb4c85b11409fea47895b/raw/a3a8da0fa5b094f1ca9d82e1642b384889ae16e8/nodelist_sleeping_giant.csv')

g = nx.Graph()

# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())

# Add node attributes
for i, nlrow in nodelist.iterrows():
    g._node[nlrow['id']] = nlrow[1:].to_dict()

# Preview first 5 edges
# print(g.edges(data=True))
# print(g.nodes(data=True))
# print('# of edges: {}'.format(g.number_of_edges()))
# print('# of nodes: {}'.format(g.number_of_nodes()))

# Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]['X'], -node[1]['Y']) for node in g.nodes(data=True)}

# Preview of node_positions with a bit of hack (there is no head/slice method for dictionaries).
# print(dict(list(node_positions.items())[0:5]))

# Define data structure (list) of edge colors for plotting
edge_colors = [e[2]['attr_dict']['color'] for e in g.edges(data=True)]

# Preview first 10
# print (edge_colors[0:10])

plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
plt.title('Graph Representation of Sleeping Giant Trail Map', size=15)
#plt.show()