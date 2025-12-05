from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    visited_set = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited_set:
            visited.append(vertex)
            visited_set.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited_set)

    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

    return visited


def connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = dfs(graph, node, [])
            visited.update(component)
            components.append(component)

    return components


def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    def visit(v):
        if v in rec_stack:
            return True
        if v in visited:
            return False

        visited.add(v)
        rec_stack.add(v)

        for neighbor in graph[v]:
            if visit(neighbor):
                return True

        rec_stack.remove(v)
        return False

    for vertex in graph:
        if visit(vertex):
            return True

    return False
