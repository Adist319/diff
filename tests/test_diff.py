# tests/test_ccdiff.py

import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.diff import longest_common_subsequence, longest_common_subsequence_lines, generate_diff

# tests/test_diff.py

from src.diff import longest_common_subsequence, longest_common_subsequence_lines, generate_diff

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

# Additional tests
def test_lcs_one_empty():
    assert longest_common_subsequence("ABC", "") == ""

def test_lcs_single_character():
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_lcs_repeated_characters():
    assert longest_common_subsequence("AAABBB", "AB") == "AB"

def test_lcs_complex():
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_single_line_common():
    lines1 = [
        "Coding Challenges helps you become a better software engineer through",
        "this is the lcs"
    ]
    lines2 = [
        "this is the lcs",
        "we're testing"
    ]
    expected = ["this is the lcs"]
    assert longest_common_subsequence_lines(lines1, lines2) == expected

def test_lcs_multiple_lines_common():
    lines1 = [
        "Coding Challenges helps you become a better software engineer through that build real applications.",
        "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
        "I’ve used or am using these coding challenges as exercises to learn a new programming language or technology.",
        "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
    ]
    lines2 = [
        "Helping you become a better software engineer through coding challenges that build real applications.",
        "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
        "These are challenges that I’ve used or am using as exercises to learn a new programming language or technology.",
        "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
    ]
    expected = [
        "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
        "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
    ]
    assert longest_common_subsequence_lines(lines1, lines2) == expected

def test_generate_diff():
    lines1 = [
        "Coding Challenges helps you become a better software engineer through that build real applications.",
        "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
        "I’ve used or am using these coding challenges as exercises to learn a new programming language or technology.",
        "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
    ]
    lines2 = [
        "Helping you become a better software engineer through coding challenges that build real applications.",
        "I share a weekly coding challenge aimed at helping software engineers level up their skills through deliberate practice.",
        "These are challenges that I’ve used or am using as exercises to learn a new programming language or technology.",
        "Each challenge will have you writing a full application or tool. Most of which will be based on real world tools and utilities."
    ]
    expected_diff = [
        "< Coding Challenges helps you become a better software engineer through that build real applications.",
        "> Helping you become a better software engineer through coding challenges that build real applications.",
        "< I’ve used or am using these coding challenges as exercises to learn a new programming language or technology.",
        "> These are challenges that I’ve used or am using as exercises to learn a new programming language or technology."
    ]
    assert generate_diff(lines1, lines2) == expected_diff

def test_generate_diff_identical_files():
    lines1 = [
        "Line 1: Identical line.",
        "Line 2: Another identical line.",
        "Line 3: Yet another identical line."
    ]
    lines2 = [
        "Line 1: Identical line.",
        "Line 2: Another identical line.",
        "Line 3: Yet another identical line."
    ]
    expected_diff = []
    assert generate_diff(lines1, lines2) == expected_diff

def test_generate_diff_one_file_empty():
    lines1 = []
    lines2 = [
        "Line 1: Only in the second file.",
        "Line 2: Another line in the second file."
    ]
    expected_diff = [
        "> Line 1: Only in the second file.",
        "> Line 2: Another line in the second file."
    ]
    assert generate_diff(lines1, lines2) == expected_diff

def test_generate_diff_multiple_additions_removals():
    lines1 = [
        "Line 1: Start of the file.",
        "Line 2: Middle line 1.",
        "Line 3: Middle line 2.",
        "Line 4: End of the file."
    ]
    lines2 = [
        "Line 1: Start of the file.",
        "Line 2: Middle line 1.",
        "Line 2.5: Inserted line.",
        "Line 3: Middle line 2.",
        "Line 4: End of the file.",
        "Line 5: Added at the end."
    ]
    expected_diff = [
        "> Line 2.5: Inserted line.",
        "> Line 5: Added at the end."
    ]
    assert generate_diff(lines1, lines2) == expected_diff


def test_generate_diff_whitespace_changes():
    lines1 = ["No spaces", "  Two spaces", "One space "]
    lines2 = ["No spaces", " Two spaces", "One space"]
    expected_diff = [
        "<   Two spaces",   
        "< One space ",     
        ">  Two spaces",    
        "> One space"       
    ]
    assert generate_diff(lines1, lines2) == expected_diff

