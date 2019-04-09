import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Grab edge list data
# Edge is the connection between 2 nodes.
# Header is none, anders pakt ie de eerste rij als kolom naam. 
edgelist = pd.read_csv('ConnectiesHolland.csv', header=None, names=["station1", "station2", "minuten"])

# Preview edgelist
edgelist.head()

# Grab node list data hosted on Gist
# De nodes zijn de stations met bijbehorende coordinaten.
nodelist = pd.read_csv('StationsHolland.csv',header=None, names=["station", "X", "Y", "kritiek"])

# Preview nodelist
nodelist

# Create empty graph
g = nx.Graph()

# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())

# Edge list example
print(elrow[0]) # node1
print(elrow[1]) # node2
print(elrow[2:].to_dict()) # edge attribute dict

# Add node attributes
for i, nlrow in nodelist.iterrows():
    g.node[nlrow[0]].update(nlrow[1:].to_dict())

# Node list example
print(nlrow)

# Preview first 5 edges
list(g.edges(data=True))[0:5]

# Preview first 10 nodes
list(g.nodes(data=True))[0:5]

# Summary Stats
print('# of edges: {}'.format(g.number_of_edges()))
print('# of nodes: {}'.format(g.number_of_nodes()))

# Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]["Y"], node[1]["X"]) for node in g.nodes(data=True)}

# Preview of node_positions with a bit of hack (there is no head/slice method for dictionaries).
dict(list(node_positions.items())[0:5])

plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, node_size=40, node_color='black')
plt.title('Graph Representation of Noord Holland Train Map', size=15)
plt.show()


nx.shortest_path(g,'Hoorn', 'Delft', 'minuten')