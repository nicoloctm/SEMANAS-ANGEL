from .graph_mst import GraphMST

def main():
    g = GraphMST(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    print("PRIM:")
    e1, c1 = g.prim_mst(0)
    print("Edges:", e1)
    print("Cost:", c1)

    print("\nKRUSKAL:")
    e2, c2 = g.kruskal_mst()
    print("Edges:", e2)
    print("Cost:", c2)

if __name__ == "__main__":
    main()
