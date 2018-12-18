import matplotlib.pyplot as plt
import networkx as nx


class Graph():
    def __init__(self, persons, connections):
        self.persons = persons
        self.connections = connections
        print('init')

    def draw_graph(self):
        plt.figure(figsize=(14, 9))
        g = nx.Graph()
        edge_labels = {}

        persons = list(self.persons)
        for connection in self.connections:
            emails = connection[0].split(';')
            g.add_edge(emails[0], emails[1])
            edge_labels[(emails[0], emails[1])] = connection[2]

        pos = nx.kamada_kawai_layout(g)
        nx.draw_networkx_nodes(g, pos,
                               nodelist=persons,
                               node_color='r',
                               node_size=2000,
                               alpha=0.6)
        nx.draw_networkx_labels(g, pos, font_size=6)

        widths = [c[1] / 200 for c in self.connections]
        nx.draw_networkx_edges(g, pos, alpha=0.8, width=widths)
        nx.draw_networkx_edge_labels(g, pos=nx.kamada_kawai_layout(g),
                                     edge_labels=edge_labels)

        plt.subplots_adjust(bottom=0, top=1, left=0, right=1)

        plt.axis('off')
        plt.show()
