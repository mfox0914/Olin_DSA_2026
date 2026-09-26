import unittest

from MinPriorityQueue import MinHeap, MinPriorityQueue


class TestMinHeap(unittest.TestCase):
    """
    Test the operations and priority ordering of MinHeap.
    """

    def setUp(self) -> None:
        """
        Initialize an empty heap for each test.
        """
        self.heap = MinHeap[str]()

    def test_insert_and_get_min_in_priority_order(self) -> None:
        """
        Check insertion, duplicate rejection, and minimum removal order.
        """
        self.assertTrue(self.heap.insert("slow", 8))
        self.assertTrue(self.heap.insert("fast", 2))
        self.assertTrue(self.heap.insert("middle", 5))
        self.assertFalse(self.heap.insert("fast", 1))

        self.assertEqual(self.heap.get_min(), "fast")
        self.assertEqual(self.heap.get_min(), "middle")
        self.assertEqual(self.heap.get_min(), "slow")
        self.assertIsNone(self.heap.get_min())
        self.assertTrue(self.heap.is_empty())

    def test_adjust_priority(self) -> None:
        """
        Check that adjusting priorities changes removal order correctly.
        """
        self.heap.insert("A", 3)
        self.heap.insert("B", 1)
        self.heap.insert("C", 2)

        self.heap.adjust_heap_number("A", 0)
        self.assertEqual(self.heap.get_min(), "A")

        self.heap.adjust_heap_number("C", 5)
        self.assertEqual(self.heap.get_min(), "B")
        self.assertEqual(self.heap.get_min(), "C")

    def test_contains(self) -> None:
        """
        Check membership before and after removing an element.
        """
        self.heap.insert("item", 1)

        self.assertTrue(self.heap.contains("item"))
        self.assertFalse(self.heap.contains("missing"))
        self.assertEqual(self.heap.get_min(), "item")
        self.assertFalse(self.heap.contains("item"))


class TestMinPriorityQueue(unittest.TestCase):
    """
    Test the operations and priority ordering of MinPriorityQueue.
    """

    def setUp(self) -> None:
        """
        Initialize an empty priority queue for each test.
        """
        self.queue = MinPriorityQueue[str]()

    def test_empty_and_priority_order(self) -> None:
        """
        Check empty behavior and removal order by priority.
        """
        self.assertTrue(self.queue.is_empty())
        self.assertIsNone(self.queue.next())

        self.queue.add_with_priority("slow", 8)
        self.queue.add_with_priority("fast", 2)
        self.queue.add_with_priority("middle", 5)

        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.next(), "fast")
        self.assertEqual(self.queue.next(), "middle")
        self.assertEqual(self.queue.next(), "slow")
        self.assertIsNone(self.queue.next())
        self.assertTrue(self.queue.is_empty())

    def test_adjust_priority(self) -> None:
        """
        Check that adjusting priorities changes removal order correctly.
        """
        self.queue.add_with_priority("A", 3)
        self.queue.add_with_priority("B", 1)
        self.queue.add_with_priority("C", 2)

        self.queue.adjust_priority("A", 0)
        self.assertEqual(self.queue.next(), "A")

        self.queue.adjust_priority("C", 5)
        self.assertEqual(self.queue.next(), "B")
        self.assertEqual(self.queue.next(), "C")


if __name__ == "__main__":
    unittest.main()
