from semana_7_arboles.graph_mst import GraphMST

def test_prim_simple():
    g = GraphMST(4)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(0, 3, 10)

    edges, cost = g.prim_mst(0)

    assert cost == 6
    assert len(edges) == 3

def test_prim_star_graph():
    g = GraphMST(4)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 1)

    edges, cost = g.prim_mst(0)

    assert cost == 3
    assert len(edges) == 3
