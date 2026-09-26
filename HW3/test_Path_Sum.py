import tempfile
import unittest
from pathlib import Path

from Path_Sum import minimum_path_sum, read_matrix


class TestPathSum(unittest.TestCase):
    """
    Test minimum right/down path sums and matrix file parsing.
    """

    def test_example_matrix(self) -> None:
        """
        Check the example matrix has the documented minimum path sum of 2427.
        """
        matrix = [
            [131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331],
        ]

        self.assertEqual(minimum_path_sum(matrix), 2427)

    def test_single_cell(self) -> None:
        """
        Check a one-cell matrix returns its only value.
        """
        self.assertEqual(minimum_path_sum([[7]]), 7)

    def test_rectangular_matrix(self) -> None:
        """
        Check the minimum path sum for a non-square matrix.
        """
        self.assertEqual(minimum_path_sum([[1, 100, 1], [2, 2, 1]]), 6)

    def test_empty_matrix_raises_value_error(self) -> None:
        """
        Check that an empty matrix is rejected.
        """
        with self.assertRaises(ValueError):
            minimum_path_sum([])

    def test_non_rectangular_matrix_raises_value_error(self) -> None:
        """
        Check that rows of different lengths are rejected.
        """
        with self.assertRaises(ValueError):
            minimum_path_sum([[1, 2], [3]])

    def test_read_matrix(self) -> None:
        """
        Check that comma-separated rows are parsed as integer values.
        """
        with tempfile.TemporaryDirectory() as directory:
            matrix_file = Path(directory) / "matrix.txt"
            matrix_file.write_text("1,2\n3,4\n", encoding="utf-8")

            self.assertEqual(read_matrix(matrix_file), [[1, 2], [3, 4]])


if __name__ == "__main__":
    unittest.main()
