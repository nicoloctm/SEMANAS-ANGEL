import unittest
from semana_5_grafos.graph_traversal import (
    bfs,
    dfs,
    connected_components,
    is_cyclic,
)


class TestGraphTraversal(unittest.TestCase):

    def setUp(self):
        self.graph = {
            "A": ["B", "D"],
            "B": ["A", "C"],
            "C": ["B"],
            "D": ["A", "E", "F"],
            "E": ["D", "F"],
            "F": ["D", "E"],
            "G": ["H"],
            "H": ["G"],
        }

    def test_bfs(self):
        self.assertEqual(bfs(self.graph, "A"), ["A", "B", "D", "C", "E", "F"])

    def test_dfs(self):
        self.assertEqual(dfs(self.graph, "A"), ["A", "B", "C", "D", "E", "F"])

    def test_connected_components(self):
        components = connected_components(self.graph)
        self.assertEqual(len(components), 2)

    def test_is_cyclic(self):
        self.assertTrue(is_cyclic(self.graph))

if __name__ == "__main__":
    unittest.main()