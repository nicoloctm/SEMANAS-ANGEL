from .weighted_graph import WeightedGraph

def dijkstra_shortest_path(graph: WeightedGraph, src: int, dest: int):
    dist, parent = graph.dijkstra(src)
    if dist[dest] == float("inf"):
        return float("inf"), []

    path = []
    cur = dest

    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return dist[dest], path
