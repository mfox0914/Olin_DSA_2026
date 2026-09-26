from __future__ import annotations

from collections.abc import Hashable
from typing import Generic, TypeVar

T = TypeVar("T", bound=Hashable)


class MinHeap(Generic[T]):
    """
    Store unique elements in a min-heap, using an index map for lookups.
    """

    def __init__(self) -> None:
        """
        Initialize an empty min-heap and its index map.
        """
        self.vertices: list[tuple[T, float]] = []
        self.index_map: dict[T, int] = {}

    def is_empty(self) -> bool:
        """
        Check whether the heap contains no elements.

        Returns:
            True if the heap is empty, otherwise False.
        """
        return not self.vertices

    def insert(self, data: T, heap_number: float) -> bool:
        """
        Insert an element with its priority.

        The priority is used to order the heap: lower values are returned first
        by ``get_min``.

        Args:
            data: The element to add.
            heap_number: The element's priority in the heap.

        Returns:
            True if the element was added, or False if it was already present.
        """
        if data in self.index_map:
            return False

        self.vertices.append((data, heap_number))
        index = len(self.vertices) - 1
        self.index_map[data] = index
        self._percolate_up(index)
        return True

    def get_min(self) -> T | None:
        """
        Remove and return the element with the lowest priority, if any.

        Returns:
            The lowest-priority element, or None if the heap is empty.
        """
        if not self.vertices:
            return None

        minimum = self.vertices[0][0]
        last = self.vertices.pop()
        del self.index_map[minimum]

        if self.vertices:
            self.vertices[0] = last
            self.index_map[last[0]] = 0
            self._bubble_down(0)

        return minimum

    def adjust_heap_number(self, vertex: T, new_number: float) -> None:
        """
        Change an element's priority if it is in the heap.

        Args:
            vertex: The element whose priority to change.
            new_number: The element's new priority.
        """
        index = self._get_index(vertex)
        if index is None:
            return

        self.vertices[index] = (vertex, new_number)
        self._percolate_up(index)
        self._bubble_down(index)

    def contains(self, vertex: T) -> bool:
        """
        Check whether an element is in the heap.

        Args:
            vertex: The element to look for.

        Returns:
            True if the element is in the heap, otherwise False.
        """
        return self._get_index(vertex) is not None

    def _get_index(self, vertex: T) -> int | None:
        """
        Find the index of an element in the heap.

        Args:
            vertex: The element to find.

        Returns:
            The element's index, or None if it is not in the heap.
        """
        return self.index_map.get(vertex)

    def _bubble_down(self, start_index: int) -> None:
        """
        Restore heap order by moving an element down from the given index.

        Args:
            start_index: The index of the element to move down.
        """
        smallest = start_index
        left_index = self._get_left_index(start_index)
        right_index = self._get_right_index(start_index)

        if (
            left_index < len(self.vertices)
            and self.vertices[left_index][1] < self.vertices[smallest][1]
        ):
            smallest = left_index
        if (
            right_index < len(self.vertices)
            and self.vertices[right_index][1] < self.vertices[smallest][1]
        ):
            smallest = right_index

        if smallest != start_index:
            self._swap(start_index, smallest)
            self._bubble_down(smallest)

    def _swap(self, index1: int, index2: int) -> None:
        """
        Swap two elements and update their stored indices.

        Args:
            index1: The index of the first element.
            index2: The index of the second element.
        """
        self.vertices[index1], self.vertices[index2] = (
            self.vertices[index2],
            self.vertices[index1],
        )
        self.index_map[self.vertices[index1][0]] = index1
        self.index_map[self.vertices[index2][0]] = index2

    def _percolate_up(self, start_index: int) -> None:
        """
        Restore heap order by moving an element up from the given index.

        Args:
            start_index: The index of the element to move up.
        """
        parent_index = self._get_parent_index(start_index)
        if (
            parent_index >= 0
            and self.vertices[start_index][1] < self.vertices[parent_index][1]
        ):
            self._swap(parent_index, start_index)
            self._percolate_up(parent_index)

    @staticmethod
    def _get_parent_index(index: int) -> int:
        """
        Get the index of an element's parent.

        Args:
            index: The index of the element.

        Returns:
            The parent's index, or -1 if the element is the root.
        """
        return (index - 1) // 2

    @staticmethod
    def _get_left_index(index: int) -> int:
        """
        Get the index of an element's left child.

        Args:
            index: The index of the parent element.

        Returns:
            The left child's index.
        """
        return index * 2 + 1

    @staticmethod
    def _get_right_index(index: int) -> int:
        """
        Get the index of an element's right child.

        Args:
            index: The index of the parent element.

        Returns:
            The right child's index.
        """
        return index * 2 + 2


class MinPriorityQueue(Generic[T]):
    """
    Maintain a queue where elements with lower priorities are removed first.
    """

    def __init__(self) -> None:
        """
        Initialize an empty priority queue.
        """
        self._heap: MinHeap[T] = MinHeap()

    def is_empty(self) -> bool:
        """
        Check whether the priority queue contains no elements.

        Returns:
            True if the queue is empty, otherwise False.
        """
        return self._heap.is_empty()

    def add_with_priority(self, elem: T, priority: float) -> None:
        """
        Add an element with its priority to the queue.

        Args:
            elem: The element to add.
            priority: The element's priority; lower values are removed first.
        """
        self._heap.insert(elem, priority)

    def next(self) -> T | None:
        """
        Remove and return the next element in priority order.

        Returns:
            The element with the lowest priority, or None if the queue is empty.
        """
        return self._heap.get_min()

    def adjust_priority(self, elem: T, new_priority: float) -> None:
        """
        Change an element's priority if it is in the queue.

        Args:
            elem: The element whose priority to change.
            new_priority: The new priority; lower values are removed first.
        """
        self._heap.adjust_heap_number(elem, new_priority)
