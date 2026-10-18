"""Local sequence alignment using the Smith-Waterman algorithm."""

import numpy as np

from matrix import Matrix


def smith_waterman(
    sequence1: str,
    sequence2: str,
    match_score: int = 3,
    mismatch_score: int = -3,
    gap_penalty: int = 2,
) -> tuple[str, str, int]:
    """
    Find the highest-scoring local alignment of two sequences.

    Args:
        sequence1 (str): The first sequence to align.
        sequence2 (str): The second sequence to align.
        match_score (int): Score added when two characters match.
        mismatch_score (int): Score added when two characters differ.
        gap_penalty (int): Non-negative cost subtracted for a gap.

    Returns:
        tuple[str, str, int]: The aligned subsequences, with gaps represented
            by hyphens, and their alignment score.

    Raises:
        ValueError: If gap_penalty is negative.
    """
    if gap_penalty < 0:
        raise ValueError("gap_penalty must be non-negative.")

    rows = len(sequence1) + 1
    columns = len(sequence2) + 1
    scores = Matrix._from_array(np.zeros((rows, columns), dtype=int))
    highest_score = 0
    max_row = 0
    max_column = 0

    for row in range(1, rows):
        for column in range(1, columns):
            substitution_score = (
                match_score
                if sequence1[row - 1] == sequence2[column - 1]
                else mismatch_score
            )
            score = max(
                0,
                scores.get(row - 1, column - 1) + substitution_score,
                scores.get(row - 1, column) - gap_penalty,
                scores.get(row, column - 1) - gap_penalty,
            )
            scores.set(row, column, score)

            if score > highest_score:
                highest_score = score
                max_row = row
                max_column = column

    aligned1: list[str] = []
    aligned2: list[str] = []
    row = max_row
    column = max_column

    while row > 0 and column > 0 and scores.get(row, column) > 0:
        current_score = scores.get(row, column)
        substitution_score = (
            match_score
            if sequence1[row - 1] == sequence2[column - 1]
            else mismatch_score
        )

        if current_score == scores.get(row - 1, column - 1) + substitution_score:
            aligned1.append(sequence1[row - 1])
            aligned2.append(sequence2[column - 1])
            row -= 1
            column -= 1
        elif current_score == scores.get(row - 1, column) - gap_penalty:
            aligned1.append(sequence1[row - 1])
            aligned2.append("-")
            row -= 1
        else:
            aligned1.append("-")
            aligned2.append(sequence2[column - 1])
            column -= 1

    aligned1.reverse()
    aligned2.reverse()
    return "".join(aligned1), "".join(aligned2), highest_score
