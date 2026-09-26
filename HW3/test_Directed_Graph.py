import unittest

from Directed_Graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        """
        Create an empty graph before each test.

        Returns:
        None: The graph is stored on ``self.graph`` for the test.
        """
        self.graph = Graph[str]()

    def test_empty_graph(self) -> None:
        """
        Test that a new graph has no vertices or edges.

        Returns:
        None: The test passes when both collections are empty.
        """
        self.assertEqual(self.graph.get_vertices(), set())
        self.assertEqual(self.graph.get_edges("missing"), {})

    def test_add_edge_adds_vertices_and_edge(self) -> None:
        """
        Test that adding an edge adds both vertices and the edge.

        Returns:
        None: The test passes when the vertices and edge are stored correctly.
        """
        self.graph.add_edge("A", "B", 2.5)

        self.assertEqual(self.graph.get_vertices(), {"A", "B"})
        self.assertEqual(self.graph.get_edges("A"), {"B": 2.5})

    def test_edges_are_directed(self) -> None:
        """
        Test that an edge only connects its starting vertex to its destination.

        Returns:
        None: The test passes when the reverse edge does not exist.
        """
        self.graph.add_edge("A", "B", 1.0)

        self.assertEqual(self.graph.get_edges("B"), {})

    def test_duplicate_vertices_are_not_added(self) -> None:
        """
        Test that adding multiple edges does not duplicate vertices.

        Returns:
        None: The test passes when each vertex appears once in the graph.
        """
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("A", "C", 2.0)

        self.assertEqual(self.graph.get_vertices(), {"A", "B", "C"})

    def test_existing_edge_cost_is_updated(self) -> None:
        """
        Test that adding an existing edge updates its cost.

        Returns:
        None: The test passes when the edge has the new cost.
        """
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("A", "B", 3.5)

        self.assertEqual(self.graph.get_edges("A"), {"B": 3.5})

    def test_get_edges_returns_a_copy(self) -> None:
        """
        Test that changing returned edges does not change the graph.

        Returns:
        None: The test passes when the graph's stored edges remain unchanged.
        """
        self.graph.add_edge("A", "B", 1.0)
        edges = self.graph.get_edges("A")
        edges["C"] = 2.0

        self.assertEqual(self.graph.get_edges("A"), {"B": 1.0})

    def test_clear_removes_vertices_and_edges(self) -> None:
        """
        Test that clearing the graph removes all vertices and edges.

        Returns:
        None: The test passes when both collections are empty after clearing.
        """
        self.graph.add_edge("A", "B", 1.0)
        self.graph.clear()

        self.assertEqual(self.graph.get_vertices(), set())
        self.assertEqual(self.graph.get_edges("A"), {})


if __name__ == "__main__":
    unittest.main()
