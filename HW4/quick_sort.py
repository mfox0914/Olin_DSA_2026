import random


def quick_sort(unsorted_array: list[int]) -> None:
    """Sort a list of integers in place using randomized quicksort.

    Args:
        unsorted_array (list[int]): The list of integers to sort.

    Returns:
        None (None): No value is returned; the input list is sorted in place.
    """
    pending_ranges = [(0, len(unsorted_array) - 1)]
    while pending_ranges:
        low, high = pending_ranges.pop()
        while low < high:
            pivot = unsorted_array[random.randrange(low, high + 1)]
            lower = low
            current = low
            upper = high

            while current <= upper:
                if unsorted_array[current] < pivot:
                    unsorted_array[lower], unsorted_array[current] = (
                        unsorted_array[current],
                        unsorted_array[lower],
                    )
                    lower += 1
                    current += 1
                elif unsorted_array[current] > pivot:
                    unsorted_array[current], unsorted_array[upper] = (
                        unsorted_array[upper],
                        unsorted_array[current],
                    )
                    upper -= 1
                else:
                    current += 1

            left_low, left_high = low, lower - 1
            right_low, right_high = upper + 1, high
            left_size = lower - low
            right_size = high - upper

            if left_size < right_size:
                if right_low < right_high:
                    pending_ranges.append((right_low, right_high))
                low, high = left_low, left_high
            else:
                if left_low < left_high:
                    pending_ranges.append((left_low, left_high))
                low, high = right_low, right_high

    # Time: O(n) best case for all-equal values; O(n log n) expected; O(n^2) worst case.
    # Randomized pivots give balanced partitions (expected), while three-way
    # partitioning processes values equal to the pivot together.
    # Space: O(log n) auxiliary space for pending ranges; the list is sorted in place.
    # Processing the smaller partition immediately bounds the pending-range stack.
