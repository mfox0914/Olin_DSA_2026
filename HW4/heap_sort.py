def heap_sort(unsorted_array: list[int]) -> None:
    """Sort a list of integers in ascending order in place.

    Args:
        unsorted_array (list[int]): The list of integers to sort.

    Returns:
        None (None): No value is returned; the input list is sorted in place.
    """

    array_length = len(unsorted_array)
    for root_index in range(array_length // 2 - 1, -1, -1):
        sift_down(unsorted_array, root_index, array_length)

    for heap_end in range(array_length - 1, 0, -1):
        unsorted_array[0], unsorted_array[heap_end] = (
            unsorted_array[heap_end],
            unsorted_array[0],
        )
        sift_down(unsorted_array, 0, heap_end)

    return None


def sift_down(unsorted_array: list[int], root_index: int, heap_size: int) -> None:
    """Restore max-heap order below a subtree root.

    Args:
        unsorted_array (list[int]): The list containing the heap.
        root_index (int): The root index of the subtree to restore.
        heap_size (int): The number of elements in the active heap.

    Returns:
        None (None): No value is returned; the heap is modified in place.
    """
    while True:
        left_index = 2 * root_index + 1
        if left_index >= heap_size:
            return

        largest_index = left_index
        right_index = left_index + 1
        if (
            right_index < heap_size
            and unsorted_array[right_index] > unsorted_array[left_index]
        ):
            largest_index = right_index

        if unsorted_array[root_index] >= unsorted_array[largest_index]:
            return

        unsorted_array[root_index], unsorted_array[largest_index] = (
            unsorted_array[largest_index],
            unsorted_array[root_index],
        )
        root_index = largest_index


# Time: O(n log n) in the best, average, and worst cases.
# Building the heap takes O(n); removing each maximum and restoring heap order
# takes O(log n), repeated for each element.
# Space: O(1) auxiliary space; the list is sorted in place.
