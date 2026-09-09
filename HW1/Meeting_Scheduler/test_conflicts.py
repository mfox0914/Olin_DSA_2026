"""Unit tests for both meeting-conflict algorithms."""

import unittest
from collections.abc import Callable, Sequence

import pairwise_conflicts
import sorted_conflicts
from meeting import Meeting


class ConflictAlgorithmTests(unittest.TestCase):
    def setUp(self) -> None:
        """Prepare both conflict algorithms for each test.

        Returns:
            None: This method stores the algorithms on the test instance.
        """

        self.algorithms: tuple[Callable[[Sequence[Meeting]], bool], ...] = (
            pairwise_conflicts.has_conflict,
            sorted_conflicts.has_conflict,
        )

    def assert_algorithms_agree(
        self, meetings: tuple[Meeting, ...], expected: bool
    ) -> None:
        """Check that both algorithms return the expected result.

        Args:
            meetings (tuple[Meeting, ...]): The meetings to check.
            expected (bool): The result both algorithms should produce.

        Returns:
            None: This method raises an assertion error if a result differs.
        """

        for algorithm in self.algorithms:
            with self.subTest(algorithm=algorithm.__module__):
                self.assertEqual(algorithm(meetings), expected)

    def test_empty_collection_has_no_conflict(self) -> None:
        """Verify that an empty collection has no conflict.

        Returns:
            None: The test passes when both algorithms return False.
        """

        self.assert_algorithms_agree((), False)

    def test_one_meeting_has_no_conflict(self) -> None:
        """Verify that one meeting has no conflict.

        Returns:
            None: The test passes when both algorithms return False.
        """

        self.assert_algorithms_agree((Meeting(10, 11),), False)

    def test_meetings_touching_at_endpoint_do_not_conflict(self) -> None:
        """Verify that meetings touching at an endpoint do not conflict.

        Returns:
            None: The test passes when both algorithms return False.
        """

        meetings = (Meeting(10, 11), Meeting(11, 11 + 30))
        self.assert_algorithms_agree(meetings, False)

    def test_overlapping_meetings_conflict(self) -> None:
        """Verify that partially overlapping meetings conflict.

        Returns:
            None: The test passes when both algorithms return True.
        """

        meetings = (Meeting(600, 660), Meeting(645, 690))
        self.assert_algorithms_agree(meetings, True)

    def test_contained_meeting_conflicts(self) -> None:
        """Verify that a meeting contained in another meeting conflicts.

        Returns:
            None: The test passes when both algorithms return True.
        """

        meetings = (Meeting(9, 15), Meeting(10, 11))
        self.assert_algorithms_agree(meetings, True)

    def test_unsorted_non_overlapping_meetings_have_no_conflict(self) -> None:
        """Verify that unsorted, non-overlapping meetings have no conflict.

        Returns:
            None: The test passes when both algorithms return False.
        """

        meetings = (Meeting(13, 14), Meeting(11, 12), Meeting(10, 11))
        self.assert_algorithms_agree(meetings, False)

    def test_later_pair_can_be_the_conflict(self) -> None:
        """Verify that a conflict is found beyond the first pair.

        Returns:
            None: The test passes when both algorithms return True.
        """

        meetings = (Meeting(8, 9), Meeting(13, 14), Meeting(13, 15))
        self.assert_algorithms_agree(meetings, True)

    def test_zero_duration_meeting_does_not_conflict(self) -> None:
        """Verify that a zero-duration meeting does not conflict.

        Returns:
            None: The test passes when both algorithms return False.
        """

        meetings = (Meeting(10, 11), Meeting(10, 10))
        self.assert_algorithms_agree(meetings, False)

    def test_invalid_meeting_times_are_rejected(self) -> None:
        """Verify that a meeting ending before it starts is rejected.

        Returns:
            None: The test passes when constructing the meeting raises ValueError.
        """

        with self.assertRaises(ValueError):
            Meeting(12, 11)


if __name__ == "__main__":
    unittest.main()
