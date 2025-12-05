import heapq
import math
from typing import List, Tuple


class WeightedGraph:
    def __init__(self, n: int):
        if n <= 0:
            raise ValueError("El grafo debe tener al menos 1 nodo.")
        self.n = n
        self.adj = {i: [] for i in range(n)}

    def add_edge(self, u: int, v: int, w: float):
        if u < 0 or v < 0 or u >= self.n or v >= self.n:
            raise IndexError("Nodo fuera de rango.")
        self.adj[u].append((v, w))

    # Dijkstra
    def dijkstra(self, src: int) -> Tuple[List[float], List[int]]:
        if src < 0 or src >= self.n:
            raise IndexError("Nodo fuente inválido.")
        dist = [math.inf] * self.n
        parent = [-1] * self.n
        visited = [False] * self.n

        dist[src] = 0
        pq = [(0, src)]

        while pq:
            cost, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True

            for v, w in self.adj[u]:
                if w < 0:
                    raise ValueError("Dijkstra no permite pesos negativos.")

                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))

        return dist, parent

    # Floyd–Warshall
    def floyd_warshall(self) -> List[List[float]]:
        dist = [[math.inf] * self.n for _ in range(self.n)]

        for i in range(self.n):
            dist[i][i] = 0

        for u in range(self.n):
            for v, w in self.adj[u]:
                dist[u][v] = min(dist[u][v], w)

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(self.n):
            if dist[i][i] < 0:
                raise ValueError("Ciclo negativo detectado.")

        return dist
