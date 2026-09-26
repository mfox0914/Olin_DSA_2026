import unittest

from Directed_Graph import Graph
from Dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    """
    Test shortest-path search through a directed weighted graph.
    """

    def setUp(self) -> None:
        """
        Create a graph with both direct and indirect routes.
        """
        self.graph = Graph[str]()
        self.graph.add_edge("A", "B", 10)
        self.graph.add_edge("A", "C", 1)
        self.graph.add_edge("C", "B", 1)
        self.graph.add_edge("B", "D", 1)
        self.graph.add_edge("C", "D", 20)

    def test_returns_lowest_cost_path(self) -> None:
        """
        Check that the algorithm returns the full path with minimum cost.
        """
        self.assertEqual(dijkstra(self.graph, "A", "D"), ["A", "C", "B", "D"])

    def test_returns_none_when_no_path_exists(self) -> None:
        """
        Check that an unreachable destination returns None.
        """
        self.assertIsNone(dijkstra(self.graph, "D", "A"))

    def test_returns_none_for_missing_endpoint(self) -> None:
        """
        Check that a vertex absent from the graph returns None.
        """
        self.assertIsNone(dijkstra(self.graph, "A", "missing"))

    def test_same_start_and_destination(self) -> None:
        """
        Check that a vertex is its own zero-edge shortest path.
        """
        self.assertEqual(dijkstra(self.graph, "A", "A"), ["A"])


if __name__ == "__main__":
    unittest.main()
