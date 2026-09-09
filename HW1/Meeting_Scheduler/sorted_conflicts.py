"""Sorting-based solution to the meeting-conflict problem."""

from collections.abc import Sequence

from meeting import Meeting


def has_conflict(meetings: Sequence[Meeting]) -> bool:
    """Return whether any pair of meetings overlaps.

    After sorting by start time, a conflict must occur between two adjacent
    meetings if one exists. The built-in ``sorted`` function takes
    Theta(n log n) time, and the scan takes Theta(n), so the total is
    Theta(n log n).

    Args:
        meetings (Sequence[Meeting]): The meetings to sort and compare.

    Returns:
        bool: True if any two meetings overlap; otherwise, False.
    """

    ordered_meetings: list[Meeting] = sorted(
        meetings, key=lambda meeting: (meeting.start, meeting.end)
    )
    for previous, current in zip(ordered_meetings, ordered_meetings[1:]):
        if current.start < previous.end:
            return True
    return False
