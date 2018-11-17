import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

persons = ['Peter', 'Max', 'Alex', 'Anna', 'Luca', 'Emma', 'Jan', 'Flo']
connections = [(0,1), (1,2), (1,3), (0,3), (4,5), (4,6), (5,6), (7,7)]
for c in connections:
	G.add_edge(persons[c[0]], persons[c[1]])

pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos,
                       nodelist=persons,
                       node_color='r',
                       node_size=2000,
                       alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=13)

plt.axis('off')
plt.subplots_adjust(bottom=0.05, top=0.95)
plt.show()
