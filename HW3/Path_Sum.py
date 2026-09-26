from __future__ import annotations

import csv
from collections.abc import Sequence
from pathlib import Path

from Dijkstra import dijkstra
from Directed_Graph import Graph


def minimum_path_sum(matrix: Sequence[Sequence[int]]) -> int:
    """
    Find the minimum sum from the top-left to bottom-right, moving right/down.

    Args:
        matrix: A non-empty rectangular matrix of integer values.

    Returns:
        The minimum sum along any allowed path, including both endpoints.
        ValueError: If the matrix is empty or its rows have different lengths.
    """
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")

    column_count = len(matrix[0])
    if any(len(row) != column_count for row in matrix):
        raise ValueError("matrix must be rectangular")

    if len(matrix) == 1 and column_count == 1:
        return matrix[0][0]

    graph: Graph[tuple[int, int]] = Graph()
    row_count = len(matrix)
    for row_index, row in enumerate(matrix):
        for column_index, value in enumerate(row):
            current = (row_index, column_index)
            if column_index + 1 < column_count:
                graph.add_edge(
                    current,
                    (row_index, column_index + 1),
                    matrix[row_index][column_index + 1],
                )
            if row_index + 1 < row_count:
                graph.add_edge(
                    current,
                    (row_index + 1, column_index),
                    matrix[row_index + 1][column_index],
                )

    path = dijkstra(graph, (0, 0), (row_count - 1, column_count - 1))
    if path is None:
        raise RuntimeError("the bottom-right cell is unreachable in this grid")

    return matrix[0][0] + sum(
        matrix[row_index][column_index] for row_index, column_index in path[1:]
    )


def read_matrix(file_path: str | Path) -> list[list[int]]:
    """
    Read a comma-separated integer matrix from a text file.

    Args:
        file_path: The path to the matrix file.

    Returns:
        The matrix as a list of integer rows.
    """
    with Path(file_path).open(newline="", encoding="utf-8") as matrix_file:
        return [[int(value) for value in row] for row in csv.reader(matrix_file) if row]


def main() -> None:
    """
    Print the minimum path sum for the matrix stored beside this file.
    """
    matrix_path = Path(__file__).with_name("matrix.txt")
    print(minimum_path_sum(read_matrix(matrix_path)))


if __name__ == "__main__":
    main()
