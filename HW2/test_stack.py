import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    """
    Test cases for the generic stack implementation.
    """

    def test_empty_stack(self) -> None:
        """
        Test operations on an empty stack.

        Verifies that an empty stack reports its state and returns None for
        peek and pop operations.
        """
        stack: Stack[int] = Stack()

        self.assertTrue(stack.isEmpty())
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())

    def test_push_and_peek(self) -> None:
        """
        Test adding an element and inspecting the top of the stack.

        Verifies that push makes the stack non-empty and that peek does not
        remove the element.
        """
        stack: Stack[str] = Stack()

        stack.push("first")

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), "first")
        self.assertEqual(stack.peek(), "first")

    def test_pop_returns_values_in_last_in_first_out_order(self) -> None:
        """
        Test that values are removed in last-in, first-out order.
        """
        stack: Stack[int] = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_pop_empties_stack(self) -> None:
        """
        Test that removing the only element leaves the stack empty.
        """
        stack: Stack[int] = Stack()
        stack.push(10)

        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.isEmpty())
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())


if __name__ == "__main__":
    unittest.main()
