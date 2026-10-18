import unittest

from smith_waterman import smith_waterman


class TestSmithWaterman(unittest.TestCase):
    """Tests for local sequence alignment."""

    def test_aligns_sequences_using_example_scoring(self) -> None:
        """Produces the example's best local alignment and score."""
        alignment1, alignment2, score = smith_waterman(
            "TGTTACGG",
            "GGTTGACTA",
        )

        self.assertEqual((alignment1, alignment2, score), ("GTT-AC", "GTTGAC", 13))

    def test_returns_empty_alignment_when_no_positive_score_exists(self) -> None:
        """Returns score zero and empty alignments when there is no match."""
        self.assertEqual(
            smith_waterman("AAA", "CCC"),
            ("", "", 0),
        )

    def test_handles_empty_sequences(self) -> None:
        """An empty input has no local alignment."""
        self.assertEqual(smith_waterman("", "AC"), ("", "", 0))
        self.assertEqual(smith_waterman("AC", ""), ("", "", 0))
        self.assertEqual(smith_waterman("", ""), ("", "", 0))

    def test_handles_sequences_with_different_lengths(self) -> None:
        """The scoring matrix supports non-square dimensions."""
        self.assertEqual(
            smith_waterman("GGACGTCC", "TACGTA"),
            ("ACGT", "ACGT", 12),
        )

    def test_uses_custom_scoring_values(self) -> None:
        """The caller can customize match, mismatch, and gap scores."""
        self.assertEqual(
            smith_waterman(
                "AC",
                "AGC",
                match_score=2,
                mismatch_score=-2,
                gap_penalty=1,
            ),
            ("A-C", "AGC", 3),
        )

    def test_rejects_negative_gap_penalty(self) -> None:
        """Gap penalty is a non-negative cost."""
        with self.assertRaises(ValueError):
            smith_waterman("A", "A", gap_penalty=-1)


if __name__ == "__main__":
    unittest.main()
