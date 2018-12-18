import matplotlib.pyplot as plt
import networkx as nx


class Graph():
    def __init__(self, persons, connections):
        self.persons = persons
        self.connections = connections

    def draw_graph(self):
        plt.figure(figsize=(14, 9))
        g = nx.Graph()
        edge_labels = {}

        persons = list(self.persons)
        persons = [self._parse_addr(person) for person in self.persons]
        for connection in self.connections:
            emails = self._parse_email_addresses(connection[0])
            g.add_edge(emails[0], emails[1])
            edge_labels[(emails[0], emails[1])] = connection[2]

        pos = nx.kamada_kawai_layout(g)
        nx.draw_networkx_nodes(g, pos,
                               nodelist=persons,
                               node_color=self._node_colors(),
                               node_size=1500,
                               alpha=0.85)
        nx.draw_networkx_labels(g, pos, font_size=6)

        widths = [c[1] / 200 for c in self.connections]
        nx.draw_networkx_edges(g, pos, alpha=0.8, width=widths)
        nx.draw_networkx_edge_labels(g, pos=nx.kamada_kawai_layout(g),
                                     edge_labels=edge_labels)

        plt.subplots_adjust(bottom=0, top=1, left=0, right=1)

        plt.axis('off')
        plt.show()

    def _parse_email_addresses(self, email_addresses):
        addrs = email_addresses.split(';')
        return self._parse_addr(addrs[0]), self._parse_addr(addrs[1])

    def _parse_addr(self, addr):
        addr = addr.replace('@enron.com', '')
        if '@' in addr:
            splitted = addr.split('@')
            return splitted[0] + '\n(' + splitted[1].split('.')[0] + ')'
        return addr

    def _node_colors(self):
        return ['skyblue' if '@enron.com' in person else 'r'
                for person in self.persons]
