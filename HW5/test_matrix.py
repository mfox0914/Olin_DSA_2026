import unittest

import numpy as np

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """Tests for square matrix storage and quadrant splitting."""

    def test_matrix_is_initialized_with_zeros(self) -> None:
        """New matrices have the requested square shape and contain zeros."""
        matrix = Matrix(3)

        self.assertEqual(matrix.matrix.shape, (3, 3))
        self.assertEqual(matrix.matrix.tolist(), [[0, 0, 0]] * 3)

    def test_non_positive_size_raises_value_error(self) -> None:
        """Matrix sizes must be positive."""
        for size in (0, -1):
            with self.subTest(size=size):
                with self.assertRaises(ValueError):
                    Matrix(size)

    def test_get_and_set(self) -> None:
        """Values can be stored and retrieved at zero-based indices."""
        matrix = Matrix(2)

        self.assertIsNone(matrix.set(1, 0, 42))
        self.assertEqual(matrix.get(1, 0), 42)
        self.assertIsInstance(matrix.get(1, 0), int)
        self.assertEqual(matrix.get(0, 0), 0)

    def test_split_returns_quadrants_in_documented_order(self) -> None:
        """Splitting returns top-left, top-right, bottom-left, bottom-right."""
        matrix = Matrix(4)
        for row in range(4):
            for column in range(4):
                matrix.set(row, column, row * 4 + column + 1)

        quadrants = matrix.split()

        self.assertEqual(
            [quadrant.matrix.tolist() for quadrant in quadrants],
            [
                [[1, 2], [5, 6]],
                [[3, 4], [7, 8]],
                [[9, 10], [13, 14]],
                [[11, 12], [15, 16]],
            ],
        )

    def test_split_quadrants_are_independent_copies(self) -> None:
        """Changing a quadrant does not modify the source matrix."""
        matrix = Matrix(2)
        matrix.set(0, 0, 7)

        top_left, _, _, _ = matrix.split()
        top_left.set(0, 0, 99)

        self.assertEqual(matrix.get(0, 0), 7)

    def test_split_odd_sized_matrix_raises_value_error(self) -> None:
        """Matrices with odd dimensions cannot be split into equal quadrants."""
        with self.assertRaises(ValueError):
            Matrix(3).split()

    def test_multiply_returns_product_of_two_matrices(self) -> None:
        """Regular multiplication returns the expected matrix product."""
        left = Matrix(2)
        right = Matrix(2)
        left.matrix[:, :] = [[1, 2], [3, 4]]
        right.matrix[:, :] = [[5, 6], [7, 8]]

        result = left.multiply(right)

        self.assertEqual(result.matrix.tolist(), [[19, 22], [43, 50]])

    def test_strassen_multiply_matches_multiply_for_recursive_sizes(self) -> None:
        """Strassen multiplication agrees with the standard algorithm."""
        for size in (1, 2, 4, 8):
            with self.subTest(size=size):
                matrix1 = Matrix(size)
                matrix2 = Matrix(size)
                matrix1.matrix[:, :] = np.arange(size * size).reshape(size, size)
                matrix2.matrix[:, :] = np.arange(size * size, 0, -1).reshape(size, size)

                expected = matrix1.multiply(matrix2)
                actual = matrix1.strassenMultiply(matrix2)

                self.assertEqual(actual.matrix.tolist(), expected.matrix.tolist())

    def test_strassen_multiply_falls_back_for_odd_sized_inputs(self) -> None:
        """Odd-sized inputs use ordinary multiplication."""
        left = Matrix(3)
        right = Matrix(3)
        left.matrix[:, :] = np.arange(1, 10).reshape(3, 3)
        right.matrix[:, :] = np.arange(9, 0, -1).reshape(3, 3)

        expected = left.multiply(right)
        actual = left.strassenMultiply(right)

        self.assertEqual(actual.matrix.tolist(), expected.matrix.tolist())


if __name__ == "__main__":
    unittest.main()
