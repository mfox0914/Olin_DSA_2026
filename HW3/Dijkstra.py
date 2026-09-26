from __future__ import annotations

from collections.abc import Hashable
from typing import TypeVar

from Directed_Graph import Graph
from MinPriorityQueue import MinPriorityQueue

VertexType = TypeVar("VertexType", bound=Hashable)


def dijkstra(
    graph: Graph[VertexType], start: VertexType, destination: VertexType
) -> list[VertexType] | None:
    """
    Find a shortest path between two vertices in a graph.

    The graph must have nonnegative edge weights.

    Args:
        graph: The directed graph to search.
        start: The vertex where the path begins.
        destination: The vertex where the path ends.

    Returns:
        A shortest path including its start and destination, or None if no path
        exists or either endpoint is not in the graph.
    """
    vertices = graph.get_vertices()
    if start not in vertices or destination not in vertices:
        return None
    if start == destination:
        return [start]

    distances: dict[VertexType, float] = {start: 0.0}
    previous: dict[VertexType, VertexType] = {}
    visited: set[VertexType] = set()
    queue: MinPriorityQueue[VertexType] = MinPriorityQueue()
    queue.add_with_priority(start, 0.0)

    while not queue.is_empty():
        current = queue.next()
        if current is None:
            break
        if current in visited:
            continue
        if current == destination:
            path = [destination]
            while path[-1] != start:
                path.append(previous[path[-1]])
            path.reverse()
            return path

        visited.add(current)
        current_distance = distances[current]

        for neighbor, edge_weight in graph.get_edges(current).items():
            if neighbor in visited:
                continue

            candidate_distance = current_distance + edge_weight
            known_distance = distances.get(neighbor)
            if known_distance is None:
                distances[neighbor] = candidate_distance
                previous[neighbor] = current
                queue.add_with_priority(neighbor, candidate_distance)
            elif candidate_distance < known_distance:
                distances[neighbor] = candidate_distance
                previous[neighbor] = current
                queue.adjust_priority(neighbor, candidate_distance)

    return None
