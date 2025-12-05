from .graph_mst import GraphMST

def run_prim(graph: GraphMST, start: int = 0):
    return graph.prim_mst(start)
