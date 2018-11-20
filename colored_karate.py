import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

pos = nx.kamada_kawai_layout(G)


nx.draw_networkx_nodes(G, pos,
					   nodelist=[16,6,5,4,10,11,0,17,21,1,3,7,19,13,12,8,13],
                       node_color='r',
                       node_size=200,
                       alpha=0.9)
nx.draw_networkx_nodes(G, pos,
					   nodelist=[14,15,18,20,22,26,29,23,24,25,27,28,9,33,32,31,30,8,2],
                       node_color='b',
                       node_size=200,
                       alpha=0.9)
nx.draw_networkx_nodes(G, pos,
					   nodelist=[30,32,33,8,2,31,7,3,9,13],
                       node_color='#800080',
                       node_size=200,
                       alpha=0.9)

nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.7)

# nx.draw_kamada_kawai(G, with_labels=True)

plt.axis('off')
plt.subplots_adjust(bottom=0.03, top=0.97)

plt.savefig('filename.png', dpi=300)
