from .graph_traversal import bfs, dfs, connected_components, is_cyclic

def main():
    graph = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": ["A", "E", "F"],
        "E": ["D", "F"],
        "F": ["D", "E"],
        "G": ["H"],
        "H": ["G"],
    }

    print("BFS desde A:", bfs(graph, "A"))
    print("DFS desde A:", dfs(graph, "A"))
    print("Componentes conectadas:", connected_components(graph))
    print("¿Tiene ciclos?:", is_cyclic(graph))

if __name__ == "__main__":
    main()
