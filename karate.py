import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

pos = nx.kamada_kawai_layout(G)

nx.draw_kamada_kawai(G, with_labels=True)

plt.axis('off')
plt.subplots_adjust(bottom=0.03, top=0.97)

plt.savefig('filename.png', dpi=300)
