from .weighted_graph import WeightedGraph
from .dijkstra import dijkstra_shortest_path
from .floyd_warshall import floyd_shortest_path

def main():
    g = WeightedGraph(6)

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 8)
    g.add_edge(3, 4, 4)
    g.add_edge(1, 5, 15)
    g.add_edge(4, 5, 7)

    d_dist, d_path = dijkstra_shortest_path(g, 0, 5)
    print("Dijkstra → Distancia a 5:", d_dist)
    print("Dijkstra → Camino:", d_path)

    fw_dist = floyd_shortest_path(g, 0, 5)
    print("Floyd–Warshall → Distancia a 5:", fw_dist)


if __name__ == "__main__":
    main()
