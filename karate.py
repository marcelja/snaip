import matplotlib.pyplot as plt
import networkx as nx


def find_highest_betweenness(G):
	betweenness_centralities = nx.edge_betweenness_centrality(G)

	max_value = 0
	edge = None

	for x,y in betweenness_centralities:
		value = betweenness_centralities[(x,y)]
		if value > max_value:
			max_value = value
			edge = (x,y)

	if edge:
		return {edge: round(max_value,2)}
	else:
		print('no edge found')


def main():
	G = nx.karate_club_graph()

	pos = nx.kamada_kawai_layout(G)

	while True:
		deleted_edge = find_highest_betweenness(G)
		nx.draw_kamada_kawai(G, with_labels=True)
		nx.draw_networkx_edge_labels(G,pos=nx.kamada_kawai_layout(G), edge_labels=deleted_edge)

		edge = list(deleted_edge.keys())[0]
		G.remove_edge(edge[0], edge[1])

		plt.show()
		if deleted_edge[edge] > 0.5:
			return


if __name__ == '__main__':
	main()
