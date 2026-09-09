"""Straightforward pairwise solution to the meeting-conflict problem."""

from collections.abc import Sequence

from meeting import Meeting


def has_conflict(meetings: Sequence[Meeting]) -> bool:
    """Return whether any pair of meetings overlaps.

    Two meetings overlap exactly when each starts before the other ends.
    Therefore, meetings that only touch at an endpoint are not a conflict.

    This checks every pair in the worst case, so its running time is
    Theta(n^2), where n is the number of meetings.

    Args:
        meetings (Sequence[Meeting]): The meetings to compare.

    Returns:
        bool: True if any two meetings overlap; otherwise, False.
    """

    for first_index in range(len(meetings)):
        first: Meeting = meetings[first_index]
        for second_index in range(first_index + 1, len(meetings)):
            second: Meeting = meetings[second_index]
            if first.start < second.end and second.start < first.end:
                return True
    return False
