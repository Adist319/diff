# tests/test_ccdiff.py

import pytest
from src.diff import longest_common_subsequence

def test_lcs_identical_strings():
    assert longest_common_subsequence("ABCDEF", "ABCDEF") == "ABCDEF"

def test_lcs_no_common():
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_partial_common():
    assert longest_common_subsequence("AABCXY", "XYZ") == "XY"

def test_lcs_empty_strings():
    assert longest_common_subsequence("", "") == ""

def test_lcs_subset():
    assert longest_common_subsequence("ABCD", "AC") == "AC"

# Additional edge cases
def test_lcs_one_empty():
    assert longest_common_subsequence("ABC", "") == ""

def test_lcs_single_character():
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_lcs_repeated_characters():
    assert longest_common_subsequence("AAABBB", "AB") == "AB"

def test_lcs_complex():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"
