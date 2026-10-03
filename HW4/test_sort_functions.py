import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(module_name: str, file_name: str):
    """Load a Python module from a file in the same folder.

    Args:
        module_name (str): The name to assign to the imported module.
        file_name (str): The filename of the module to load.

    Returns:
        ModuleType: The loaded Python module.
    """
    module_path = ROOT / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SORT_FUNCTIONS = [
    load_module("insertion_sort", "insertion_sort.py").insertion_sort,
    load_module("heap_sort", "heap_sort.py").heap_sort,
    load_module("quick_sort", "quick_sort.py").quick_sort,
    load_module("radix_sort", "radix_sort.py").radix_sort,
]


class TestSortFunctions(unittest.TestCase):
    def assert_sort_correct(self, sort_function, values):
        """Check that a sorting function produces a correctly sorted list.

        Args:
            sort_function: The sort implementation to test.
            values (list[int]): The list to sort.
        """
        original = values[:]
        sort_function(original)
        self.assertEqual(
            original, sorted(values), f"{sort_function.__name__} failed for {values}"
        )

    def test_empty_list(self):
        """Verify sorting an empty list leaves it unchanged."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [])

    def test_single_element(self):
        """Verify sorting a single-element list leaves it unchanged."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [42])

    def test_basic_unsorted_list(self):
        """Verify a basic unsorted list is sorted correctly."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [9, 4, 7, 1, 3, 8, 2, 5])

    def test_duplicates(self):
        """Verify duplicates are preserved and sorted correctly."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [5, 2, 9, 2, 1, 5, 3, 9, 1])

    def test_negative_numbers(self):
        """Verify negative values are handled correctly alongside positives."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [-3, 0, 7, -1, 2, -5, 6])

    def test_already_sorted_list(self):
        """Verify already-sorted input remains correctly sorted."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [1, 2, 3, 4, 5, 6])

    def test_reverse_sorted_list(self):
        """Verify reverse-sorted input is sorted correctly in the worst direction."""
        for sort_function in SORT_FUNCTIONS:
            self.assert_sort_correct(sort_function, [9, 8, 7, 6, 5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
