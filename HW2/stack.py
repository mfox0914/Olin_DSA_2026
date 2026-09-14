from typing import Generic, TypeVar
from linked_list import Node, LinkedList

T = TypeVar("T")


class Stack(Generic[T]):
    """
    Generic stack class using already implemented linked list.
    """

    def __init__(self) -> None:
        """Initializer for stack. Initializes an empty linked list to serve as the stack."""
        self.stack: LinkedList[T] = LinkedList()

    def push(self, data: T) -> None:
        """
        Add data to the top of the stack.

        Args:
            data: The value to add to the stack.
        """
        self.stack.pushFront(data)
        return None

    def pop(self) -> T | None:
        """
        Remove and return the value at the top of the stack.

        Returns:
            self.stack.popFront(): The value at the top of the stack, or None if the stack is empty.
        """
        return self.stack.popFront()

    def peek(self) -> T | None:
        """
        Return the value at the top of the stack without removing it.

        Returns:
            self.stack.peekFront(): The value at the top of the stack, or None if the stack is empty.
        """
        return self.stack.peekFront()

    def isEmpty(self) -> bool:
        """
        Return whether the stack is empty.

        Returns:
            self.stack.isEmpty(): True if the stack is empty and False otherwise.
        """
        return self.stack.isEmpty()
