"""Data model for scheduled meetings."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Meeting:
    """A meeting represented by start and end times in comparable units.

    Attributes:
        start (int): The meeting's start time.
        end (int): The meeting's end time.
    """

    start: int
    end: int

    def __post_init__(self) -> None:
        """Reject meetings whose end time comes before their start time.

        Returns:
            None: This method validates the meeting in place.

        Raises:
            ValueError: If the meeting ends before it starts.
        """

        if self.start > self.end:
            raise ValueError("a meeting cannot end before it starts")
