from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """
    Class to define a node object with a value that could be doubly-linked to other nodes.
    """

    def __init__(
        self,
        value: T,
        next: Node[T] | None = None,
        previous: Node[T] | None = None,
    ) -> None:
        """
        Initializer for Node class.

        Args:
            value: The value of the node.
            next (Node): The node that comes after the current node.
            previous (Node): The node that comes before the current node.
        """
        self.value = value
        self.next = next
        self.previous = previous

    def get_value(self) -> T:
        """
        Function to return Node value.

        Returns:
            self.value: The value of the node.
        """
        return self.value

    def get_next(self) -> Node[T] | None:
        """
        Function to get the next Node in the list.

        Returns:
            self.next: The node that comes after the current node.
        """
        return self.next

    def set_value(self, new_value: T) -> None:
        """
        Function to set a new value for the current Node.

        Args:
            new_value: The new value for the current Node.
        """
        self.value = new_value
        return None

    def set_next(self, next: Node[T] | None) -> None:
        """
        Set a new Node to come after the current Node.

        Args:
            next (Node): Node to come after the current Node.
        """
        self.next = next
        return None

    def get_previous(self) -> Node[T] | None:
        """
        Function to get the previous Node in the list.

        Returns:
            self.previous: The node that comes before the current node.
        """
        return self.previous

    def set_previous(self, previous: Node[T] | None) -> None:
        """
        Set a new Node to come before the current Node.

        Args:
            previous (Node): Node to come before the current Node.
        """
        self.previous = previous
        return None


class LinkedList(Generic[T]):
    """
    Class to define a doubly linked list.

    """

    def __init__(self) -> None:
        """
        Initializer for doubly-linked list. Sets head and tail to None.
        """
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None

    def pushFront(self, data: T) -> None:
        """
        Method that adds the element [data] to the front of the linked list.

        Args:
            data: Data to be added to the front of the linked list.
        """
        data_node = Node(data, next=self.head)
        if self.head is None:
            self.tail = data_node
        else:
            self.head.set_previous(data_node)
        self.head = data_node
        return None

    def pushBack(self, data: T) -> None:
        """
        Method that adds the element [data] to the back of the linked list.

        Args:
            data: Data to be added to the back of the linked list.
        """
        data_node = Node(data, previous=self.tail)
        tail = self.tail
        if tail is None:
            self.head = data_node
        else:
            tail.set_next(data_node)
        self.tail = data_node
        return None

    def popFront(self) -> T | None:
        """
        Removes an element from the front of the list. If the list is empty, it is unchanged.

        Returns:
            temp.get_value(): The value at the front of the list, or None if none exists.
        """
        head = self.head
        if head is None:
            print("There is no value at the front of the list. It is empty.")
            return None
        temp = head
        self.head = temp.get_next()
        if self.head is None:
            self.tail = None
        else:
            self.head.set_previous(None)
        temp.set_next(None)
        return temp.get_value()

    def popBack(self) -> T | None:
        """
        Removes an element from the back of the list. If the list is empty, it is unchanged.

        Returns:
            temp.get_value(): The value at the back of the list, or None if none exists.
        """
        tail = self.tail
        if tail is None:
            print("There is no value at the end of the list. It is empty.")
            return None
        temp = tail
        self.tail = temp.get_previous()
        if self.tail is None:
            self.head = None
        else:
            self.tail.set_next(None)
        temp.set_previous(None)
        return temp.get_value()

    def peekFront(self) -> T | None:
        """
        Returns the value at the front of the list or None if none exists.

        Returns:
            self.head.get_value(): The value at the front of the list.
        """
        head = self.head
        if head is None:
            print("There is no value at the front of the list. It is empty.")
            return None
        return head.get_value()

    def peekBack(self) -> T | None:
        """
        Return the value at the back of the list or None if none exists.

        Returns:
            self.tail.get_value(): The value at the back of the list.
        """
        tail = self.tail
        if tail is None:
            print("There is no value at the front of the list. It is empty.")
            return None
        return tail.get_value()

    def isEmpty(self) -> bool:
        """
        Returns True if the list is empty and False otherwise.
        """
        if self.head == None and self.tail == None:
            return True
        else:
            return False
