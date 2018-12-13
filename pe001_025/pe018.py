import networkx as nx
import numpy as np

"""
Problem:
https://projecteuler.net/problem=18

Find the maximum total from top to bottom of the triangle (see pe18.txt)

Solution:
Define the triangle as a graph. 
* Each number n represents an edge with length -n. 
* The number of nodes is equal to the size of the triangle + 1 (source node).
* The shortest path algorithm will find the largest path, as we initialize
    our graph with negative lengths.

"""
L = [l.split(" ") for l in open("pe18.txt", "r").read().splitlines()]
trianglelist = [[-int(x) for x in l] for l in L]

def triangle_to_graph(trianglelist):
    """Makes a nx.DiGraph from a trianglelist."""
    G = nx.DiGraph()
    k = len(trianglelist)
    N = k*(k+1)//2 - k + 1
    n = 1

    for layer in trianglelist:
        layerlen = len(layer)
        for i in range(layerlen):
            # Add two edges for the first n-1 layers
            if n < N:
                G.add_weighted_edges_from([(n, n+layerlen, layer[i]), 
                    (n, n+layerlen+1, layer[i])])

            # Add one edge for the last layer
            else:
                G.add_edge(n, n+layerlen, weight = layer[i])
            n +=1
    
    return(G)

def maxpathsum(trianglelist):
    """Returns the maximum path sum from a triangle graph."""
    G = triangle_to_graph(trianglelist)
    target = len(G.nodes())
    n = len(trianglelist)
    minimum = 0
    for i in range(target-n, target+1):
        new = nx.bellman_ford_path_length(G, 1, i) 
        if new < minimum:
            minimum = new
    
    return(-minimum)


print(maxpathsum(trianglelist))
