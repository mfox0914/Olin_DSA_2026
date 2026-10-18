import numpy as np


class Matrix:
    """A square matrix of integers."""

    def __init__(self, n: int) -> None:
        """Create an n-by-n matrix initialized with zeros.

        Args:
            n (int): The number of rows and columns in the matrix.

        Returns:
            None (None): No value is returned; the matrix is initialized.
        """
        if n <= 0:
            raise ValueError("n must be a positive number.")

        self.matrix: np.ndarray = np.zeros((n, n), dtype=int)

    def get(self, row: int, column: int) -> int:
        """Get the value at a specified row and column.

        Args:
            row (int): The zero-based row index.
            column (int): The zero-based column index.

        Returns:
            int (int): The value stored at the specified indices.
        """
        return int(self.matrix[row, column])

    def set(self, row: int, column: int, value: int) -> None:
        """Set the value at a specified row and column.

        Args:
            row (int): The zero-based row index.
            column (int): The zero-based column index.
            value (int): The integer value to store.

        Returns:
            None (None): No value is returned; the matrix is updated.
        """
        self.matrix[row, column] = value

    @classmethod
    def _from_array(cls, values: np.ndarray) -> "Matrix":
        """Create a matrix from an array without zero-initializing its storage.

        Args:
            values (np.ndarray): The square array to copy into the matrix.

        Returns:
            Matrix: A matrix containing an independent copy of the array.
        """
        matrix = cls.__new__(cls)
        matrix.matrix = values.copy()
        return matrix

    def split(self) -> tuple["Matrix", "Matrix", "Matrix", "Matrix"]:
        """Divide the matrix into four equal-sized quadrants.

        Args:
            None: This method takes no arguments.

        Returns:
            tuple[Matrix, Matrix, Matrix, Matrix]: The top-left, top-right,
                bottom-left, and bottom-right quadrants, in that order.
        """
        rows, columns = self.matrix.shape
        if rows != columns or rows % 2 != 0:
            raise ValueError("Matrix must be square with an even size to split.")

        half = rows // 2
        top_left = self._from_array(self.matrix[:half, :half])
        top_right = self._from_array(self.matrix[:half, half:])
        bottom_left = self._from_array(self.matrix[half:, :half])
        bottom_right = self._from_array(self.matrix[half:, half:])

        return top_left, top_right, bottom_left, bottom_right

    def multiply(
        self,
        matrix2: "Matrix",
    ) -> "Matrix":
        """
        Multiply this matrix by another matrix using the standard algorithm.

        Args:
            matrix2 (Matrix): The matrix to multiply this matrix by.

        Returns:
            Matrix: The product of this matrix and matrix2.
        """
        if self.matrix.shape[1] != matrix2.matrix.shape[0]:
            raise ValueError(
                "The # of columns in the first matrix must equal the # of rows in the second matrix."
            )

        final_matrix: np.ndarray = np.zeros(
            (self.matrix.shape[0], matrix2.matrix.shape[1]), dtype=int
        )
        for i in range(final_matrix.shape[0]):
            for j in range(final_matrix.shape[1]):
                for k in range(self.matrix.shape[1]):
                    final_matrix[i, j] += self.matrix[i, k] * matrix2.matrix[k, j]

        return self._from_array(final_matrix)

    def strassenMultiply(
        self,
        matrix2: "Matrix",
    ) -> "Matrix":
        """
        Multiply this matrix by another matrix using Strassen's algorithm.

        For small, odd-sized, or non-square matrices, uses standard
        multiplication instead.

        Args:
            matrix2 (Matrix): The matrix to multiply this matrix by.

        Returns:
            Matrix: The product of this matrix and matrix2.
        """
        if self.matrix.shape[1] != matrix2.matrix.shape[0]:
            raise ValueError(
                "The # of columns in the first matrix must equal the # of rows in the second matrix."
            )

        rows, inner_size = self.matrix.shape
        columns = matrix2.matrix.shape[1]
        if (
            inner_size <= 2
            or rows != inner_size
            or inner_size != columns
            or inner_size % 2 != 0
        ):
            return self.multiply(matrix2)

        a, b, c, d = self.split()
        e, f, g, h = matrix2.split()

        m1 = self._from_array(a.matrix + d.matrix).strassenMultiply(
            self._from_array(e.matrix + h.matrix)
        )
        m2 = self._from_array(c.matrix + d.matrix).strassenMultiply(e)
        m3 = a.strassenMultiply(self._from_array(f.matrix - h.matrix))
        m4 = d.strassenMultiply(self._from_array(g.matrix - e.matrix))
        m5 = self._from_array(a.matrix + b.matrix).strassenMultiply(h)
        m6 = self._from_array(c.matrix - a.matrix).strassenMultiply(
            self._from_array(e.matrix + f.matrix)
        )
        m7 = self._from_array(b.matrix - d.matrix).strassenMultiply(
            self._from_array(g.matrix + h.matrix)
        )

        top_left = m1.matrix + m4.matrix - m5.matrix + m7.matrix
        top_right = m3.matrix + m5.matrix
        bottom_left = m2.matrix + m4.matrix
        bottom_right = m1.matrix - m2.matrix + m3.matrix + m6.matrix
        return self._from_array(
            np.concatenate(
                (
                    np.concatenate((top_left, top_right), axis=1),
                    np.concatenate((bottom_left, bottom_right), axis=1),
                ),
                axis=0,
            )
        )
