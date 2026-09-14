from typing import Generic, TypeVar
from linked_list import Node, LinkedList

T = TypeVar("T")


class Queue(Generic[T]):
    """
    Generic Queue class using already implemented linked list class.
    """

    def __init__(self) -> None:
        """Initializer for queue. Initializes an empty linked list to serve as the queue."""
        self.queue: LinkedList[T] = LinkedList()

    def enqueue(self, data: T) -> None:
        """
        Add [data] to the end of the queue.

        Args:
            data: Data to be added to the end of the queue.
        """
        self.queue.pushBack(data)
        return None

    def dequeue(self) -> T | None:
        """
        Remove and return the value at the front of the queue.

        Returns:
            self.queue.popFront(): The value at the front of the queue.
        """
        return self.queue.popFront()

    def peek(self) -> T | None:
        """
        Return the value at the front of the queue without removing it.

        Returns:
            self.queue.peekFront: the value at the front of the queue.
        """
        return self.queue.peekFront()

    def isEmpty(self) -> bool:
        """
        Return whether the queue is empty.

        Returns:
            self.queue.isEmpty() (Boolean): returns True if the list is empty and False otherwise.
        """
        return self.queue.isEmpty()
