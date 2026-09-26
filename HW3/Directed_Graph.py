from __future__ import annotations

from typing import Generic, TypeVar

VertexType = TypeVar("VertexType")


class Graph(Generic[VertexType]):
    """A directed graph whose vertices have type ``VertexType``."""

    def __init__(self) -> None:
        self.verticies: list[VertexType] = []
        self.edges: dict[VertexType, dict[VertexType, float]] = {}

    def get_vertices(self) -> set[VertexType]:
        """
        Return the vertices in the graph.

        Returns:
        self.verticies (list): A list of all the verticies in the graph.
        """
        return set(self.verticies)

    def add_edge(
        self, from_vertex: VertexType, to_vertex: VertexType, cost: float
    ) -> None:
        """
        Add an edge from ``from_vertex`` to ``to_vertex`` with weight ``cost``.

        Args:
        from_vertex: The starting vertex.
        to_vertex: The vertex connected to ```from_vertex```.
        cost (float): The edge weight.

        """
        if from_vertex not in self.verticies:
            self.verticies.append(from_vertex)
        if to_vertex not in self.verticies:
            self.verticies.append(to_vertex)

        if from_vertex not in self.edges:
            self.edges[from_vertex] = {}
        self.edges[from_vertex][to_vertex] = cost

    def get_edges(self, from_vertex: VertexType) -> dict[VertexType, float]:
        """
        Return each vertex connected from ``from_vertex`` and its edge weight.

        Args:
        from_vertex: The vertex whose connections are being returned.

        Returns:
        self.edges[from_vertex] (dict): A dictionary returning both the verticies connected to ```from_vertex``` and their edge weights.
        """
        return self.edges.get(from_vertex, {}).copy()

    def remove_vertex(self, vertex: VertexType) -> None:
        """Remove a vertex and every edge connected to it."""
        if vertex not in self.verticies:
            return

        self.verticies.remove(vertex)
        self.edges.pop(vertex, None)
        for outgoing_edges in self.edges.values():
            outgoing_edges.pop(vertex, None)

    def clear(self) -> None:
        """Remove all edges and vertices from the graph."""
        self.verticies = []
        self.edges = {}
