import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

persons = ['Peter', 'Max', 'Alex', 'Anna', 'Luca', 'Emma', 'Jan', 'Flo']
connections = [(0,1), (1,2), (1,3), (0,3), (4,5), (4,6), (5,6), (7,7)]
for c in connections:
	G.add_edge(persons[c[0]], persons[c[1]])

pos = nx.circular_layout(G)

# nx.draw_networkx_nodes(G, pos,
#                        nodelist=persons,
#                        node_color='r',
#                        node_size=2000,
#                        alpha=0.8)

nx.draw_networkx_nodes(G, pos,
                       nodelist=persons[0:4],
                       node_color='r',
                       node_size=2000,
                       alpha=0.6)
nx.draw_networkx_nodes(G, pos,
                       nodelist=persons[7:8],
                       node_color='y',
                       node_size=2000,
                       alpha=0.6)
nx.draw_networkx_nodes(G, pos,
                       nodelist=persons[4:7],
                       node_color='b',
                       node_size=2000,
                       alpha=0.6)

nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
### example edges:
# nx.draw_networkx_edges(G, pos,
#                        edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
#                        width=8, alpha=0.5, edge_color='b')
nx.draw_networkx_labels(G, pos, font_size=14)

plt.axis('off')
plt.subplots_adjust(bottom=0.03, top=0.97)

plt.savefig('filename.png', dpi=300)
