def radix_sort(unsorted_array: list[int]) -> None:
    """Sort a list of integers in ascending order in place.

    Args:
        unsorted_array (list[int]): The list of integers to sort.

    Returns:
        None (None): No value is returned; the input list is sorted in place.
    """

    if len(unsorted_array) <= 1:
        return

    negatives = [value for value in unsorted_array if value < 0]
    non_negatives = [value for value in unsorted_array if value >= 0]

    def radix_sort_non_negative(values: list[int]) -> list[int]:
        """Sort a list of non-negative integers in ascending order.

        Args:
            values (list[int]): The non-negative integers to sort.

        Returns:
            list[int]: A sorted list of the same integers in ascending order.
        """
        if len(values) < 2:
            return values

        max_value = max(values)
        place_value = 1

        while max_value // place_value > 0:
            output = [0] * len(values)
            counts = [0] * 10

            for value in values:
                digit = (value // place_value) % 10
                counts[digit] += 1

            for index in range(1, 10):
                counts[index] += counts[index - 1]

            for value in reversed(values):
                digit = (value // place_value) % 10
                counts[digit] -= 1
                output[counts[digit]] = value

            values = output
            place_value *= 10

        return values

    if negatives:
        negatives = radix_sort_non_negative([-value for value in negatives])
        negatives = [-value for value in reversed(negatives)]
    else:
        negatives = []

    if non_negatives:
        non_negatives = radix_sort_non_negative(non_negatives)
    else:
        non_negatives = []

    unsorted_array[:] = negatives + non_negatives

    # Time: O(nk) where k is the number of digits in the largest absolute value.
    # We process the list once for each digit place, using counting sort at each step.
    # Space: O(n) auxiliary space for the output buffer and digit-count arrays.
