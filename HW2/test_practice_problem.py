import unittest

from practice_problem import copy_stack
from stack import Stack


class TestCopyStack(unittest.TestCase):
    """Test the copy_stack practice problem."""

    def test_copy_preserves_stack_order(self) -> None:
        """
        Test that the copied stack returns values in the original LIFO order.
        """
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        stack_copy = copy_stack(stack)

        self.assertIsNot(stack_copy, stack)
        self.assertEqual(stack_copy.pop(), 3)
        self.assertEqual(stack_copy.pop(), 2)
        self.assertEqual(stack_copy.pop(), 1)
        self.assertTrue(stack_copy.isEmpty())

    def test_copy_of_empty_stack_is_empty(self) -> None:
        """Test that copying an empty stack produces an empty stack."""
        stack: Stack[int] = Stack()

        stack_copy = copy_stack(stack)

        self.assertIsNot(stack_copy, stack)
        self.assertTrue(stack_copy.isEmpty())


if __name__ == "__main__":
    unittest.main()
