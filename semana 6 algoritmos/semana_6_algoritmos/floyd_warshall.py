from .weighted_graph import WeightedGraph

def floyd_shortest_path(graph: WeightedGraph, src: int, dest: int):
    dist = graph.floyd_warshall()
    d = dist[src][dest]

    return d
