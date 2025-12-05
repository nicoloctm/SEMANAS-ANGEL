from semana_7_arboles.graph_mst import GraphMST

def test_kruskal_simple():
    g = GraphMST(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    edges, cost = g.kruskal_mst()

    assert cost == 19
    assert len(edges) == 3

def test_kruskal_disconnected_creates_forest():
    g = GraphMST(4)
    g.add_edge(0, 1, 1)
    g.add_edge(2, 3, 2)

    edges, cost = g.kruskal_mst()

    assert cost == 3
    assert len(edges) == 2     # forest
