import heapq
from typing import List, Tuple
from .union_find import UnionFind


class GraphMST:
    def __init__(self, vertices: int):
        if vertices <= 0:
            raise ValueError("El grafo debe tener al menos 1 nodo.")
        self.V = vertices
        self.edges = []
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u: int, v: int, w: float):
        if u < 0 or v < 0 or u >= self.V or v >= self.V:
            raise IndexError("Nodo fuera de rango.")
        self.edges.append((u, v, w))
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # -------- PRIM -----------------------------------------------------
    def prim_mst(self, start_node=0) -> Tuple[List[Tuple[int, int, float]], float]:
        visited = [False] * self.V
        visited[start_node] = True

        pq = []
        for neigh, w in self.adj[start_node]:
            heapq.heappush(pq, (w, start_node, neigh))

        mst_edges = []
        mst_cost = 0

        while pq:
            w, u, v = heapq.heappop(pq)
            if visited[v]:
                continue

            visited[v] = True
            mst_edges.append((u, v, w))
            mst_cost += w

            for next_node, next_w in self.adj[v]:
                if not visited[next_node]:
                    heapq.heappush(pq, (next_w, v, next_node))

        return mst_edges, mst_cost

    # -------- KRUSKAL -------------------------------------------------
    def kruskal_mst(self) -> Tuple[List[Tuple[int, int, float]], float]:
        uf = UnionFind(self.V)
        mst_edges = []
        mst_cost = 0

        sorted_edges = sorted(self.edges, key=lambda e: e[2])

        for u, v, w in sorted_edges:
            if uf.union(u, v):  # Only add if does NOT create cycle
                mst_edges.append((u, v, w))
                mst_cost += w

        return mst_edges, mst_cost
