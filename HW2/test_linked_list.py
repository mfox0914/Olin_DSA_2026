import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    Test cases for the generic doubly linked list implementation.
    """

    def test_empty_list(self) -> None:
        """
        Test operations on an empty linked list.

        Verifies that an empty list reports its state and returns None for
        peek and pop operations.
        """
        linked_list: LinkedList[int] = LinkedList()

        self.assertTrue(linked_list.isEmpty())
        self.assertIsNone(linked_list.peekFront())
        self.assertIsNone(linked_list.peekBack())
        self.assertIsNone(linked_list.popFront())
        self.assertIsNone(linked_list.popBack())

    def test_push_front_and_peek_front(self) -> None:
        """
        Test adding elements to the front of the linked list.

        Verifies that the newest front element is returned by peekFront and
        that the original element remains at the back.
        """
        linked_list: LinkedList[int] = LinkedList()

        linked_list.pushFront(2)
        linked_list.pushFront(1)

        self.assertFalse(linked_list.isEmpty())
        self.assertEqual(linked_list.peekFront(), 1)
        self.assertEqual(linked_list.peekBack(), 2)

    def test_push_back_and_peek_back(self) -> None:
        """
        Test adding elements to the back of the linked list.

        Verifies that the newest back element is returned by peekBack and
        that the original element remains at the front.
        """
        linked_list: LinkedList[str] = LinkedList()

        linked_list.pushBack("first")
        linked_list.pushBack("last")

        self.assertEqual(linked_list.peekFront(), "first")
        self.assertEqual(linked_list.peekBack(), "last")

    def test_pop_front_updates_links(self) -> None:
        """
        Test removing the front element and updating forward links.

        Verifies that the new head has no previous node and that its next
        node points back to it.
        """
        linked_list: LinkedList[int] = LinkedList()
        linked_list.pushBack(1)
        linked_list.pushBack(2)
        linked_list.pushBack(3)

        self.assertEqual(linked_list.popFront(), 1)
        self.assertEqual(linked_list.peekFront(), 2)
        head = linked_list.head
        assert head is not None
        self.assertIsNone(head.get_previous())
        next_node = head.get_next()
        assert next_node is not None
        self.assertIs(next_node.get_previous(), head)

    def test_pop_back_updates_links(self) -> None:
        """
        Test removing the back element and updating backward links.

        Verifies that the new tail has no next node and that its previous
        node points forward to it.
        """
        linked_list: LinkedList[int] = LinkedList()
        linked_list.pushBack(1)
        linked_list.pushBack(2)
        linked_list.pushBack(3)

        self.assertEqual(linked_list.popBack(), 3)
        self.assertEqual(linked_list.peekBack(), 2)
        tail = linked_list.tail
        assert tail is not None
        self.assertIsNone(tail.get_next())
        previous_node = tail.get_previous()
        assert previous_node is not None
        self.assertIs(previous_node.get_next(), tail)

    def test_single_element_removal_empties_list(self) -> None:
        """
        Test that removing the only element empties the linked list.

        Verifies this behavior for both front and back removal operations.
        """
        linked_list: LinkedList[int] = LinkedList()
        linked_list.pushFront(10)

        self.assertEqual(linked_list.popFront(), 10)
        self.assertTrue(linked_list.isEmpty())
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

        linked_list.pushBack(20)
        self.assertEqual(linked_list.popBack(), 20)
        self.assertTrue(linked_list.isEmpty())


if __name__ == "__main__":
    unittest.main()
