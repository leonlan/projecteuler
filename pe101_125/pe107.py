"""
Problem 107: Minimal network
https://projecteuler.net/problem=107

Solution:
This is an instance of the minimal spanning tree problem.
"""
import networkx as nx


def minimal_network(adj_list):
    """Finds the biggest sum of removed edges by finding the minimal spanning
    tree given an adjancy list of a graph."""
    G = nx.Graph()
    for u in range(len(adj_list)):
        for v in range(len(adj_list[u])):
            edge_weight = adj_list[u][v]
            if edge_weight != "-":
                G.add_edge(u, v, weight = int(adj_list[u][v]))

    def graph_weighted_edges_sum(G):
        """Computes the sum of all edges in a weighted graph G."""
        return(sum([v for k, v in nx.get_edge_attributes(G, 'weight').items()]))

    original_weight = graph_weighted_edges_sum(G)
    MST = nx.minimum_spanning_tree(G)
    new_weight = graph_weighted_edges_sum(MST)

    return(original_weight - new_weight)


if __name__ == "__main__":
    f = open('pe107.txt', 'r')
    adjacency_list = [x.strip().split(',') for x in f.readlines()]
    print(minimal_network(adjacency_list))
