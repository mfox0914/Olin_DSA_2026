def insertion_sort(unsorted_array: list[int]) -> None:
    """
    Implementation of the insertion sort algorithm.

    Args:
        unsorted_array (list[int]): A list of unsorted integers.
    """
    for i in range(1, len(unsorted_array)):
        curr_el = unsorted_array[i]
        for j in reversed(range(i)):
            if unsorted_array[j] > curr_el:
                unsorted_array[j + 1] = unsorted_array[j]
                unsorted_array[j] = curr_el
            else:
                break


# Time: O(n) best case for an already-sorted list; O(n^2) average and worst cases.
# The early break gives the best case: each element needs only one comparison. In the
# average and worst cases, values may need to shift multiple times, requiring a check across all elements at worst.
# Space: O(1) auxiliary space; the list is sorted in place.
