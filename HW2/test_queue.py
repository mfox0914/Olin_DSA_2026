import unittest

from queue import Queue


class TestQueue(unittest.TestCase):
    """
    Test cases for the generic queue implementation.
    """

    def test_empty_queue(self) -> None:
        """
        Test operations on an empty queue.

        Verifies that an empty queue reports its state and returns None for
        peek and pop operations.
        """
        queue: Queue[int] = Queue()

        self.assertTrue(queue.isEmpty())
        self.assertIsNone(queue.peek())
        self.assertIsNone(queue.dequeue())

    def test_enqueue_and_peek(self) -> None:
        """
        Test adding an element to the back and inspecting the front of the queue.

        Verifies that enqueue makes the queue non-empty and that peek does not
        remove the element.
        """
        queue: Queue[str] = Queue()

        queue.enqueue("first")

        self.assertFalse(queue.isEmpty())
        self.assertEqual(queue.peek(), "first")
        self.assertEqual(queue.peek(), "first")

    def test_dequeue_returns_values_in_first_in_first_out_order(self) -> None:
        """
        Test that values are removed in first-in, first-out order.
        """
        queue: Queue[int] = Queue()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_dequeue_empties_queue(self) -> None:
        """
        Test that removing the only element leaves the queue empty.
        """
        queue: Queue[int] = Queue()
        queue.enqueue(10)

        self.assertEqual(queue.dequeue(), 10)
        self.assertTrue(queue.isEmpty())
        self.assertIsNone(queue.peek())
        self.assertIsNone(queue.dequeue())


if __name__ == "__main__":
    unittest.main()
