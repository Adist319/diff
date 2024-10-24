# src/diff.py
#!/usr/bin/env python3
import argparse


def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    # Initialize the DP table
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    # Build the table in bottom-up manner
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + str1[i]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)

    return dp[m][n]


def longest_common_subsequence_lines(lines1, lines2):
    m, n = len(lines1), len(lines2)
    # Initialize the DP table with zeros
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill the DP table
    for i in range(m):
        for j in range(n):
            if lines1[i] == lines2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    # Reconstruct the LCS by backtracking
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if lines1[i-1] == lines2[j-1]:
            lcs.insert(0, lines1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

def generate_diff(lines1, lines2):
    lcs = longest_common_subsequence_lines(lines1, lines2)
    diff = []
    i = j = 0
    for common_line in lcs:
        # Remove lines from lines1 not in LCS
        while i < len(lines1) and lines1[i] != common_line:
            diff.append(f"< {lines1[i]}")
            i += 1
        # Remove lines from lines2 not in LCS
        while j < len(lines2) and lines2[j] != common_line:
            diff.append(f"> {lines2[j]}")
            j += 1
        # Skip the common line
        if i < len(lines1):
            i += 1
        if j < len(lines2):
            j += 1
    # Handle any remaining lines
    while i < len(lines1):
        diff.append(f"< {lines1[i]}")
        i += 1
    while j < len(lines2):
        diff.append(f"> {lines2[j]}")
        j += 1
    return diff


def main():
    parser = argparse.ArgumentParser(description='CCDiff: A simple diff tool.')
    parser.add_argument('original_file', help='Path to the original file.')
    parser.add_argument('new_file', help='Path to the new file.')
    args = parser.parse_args()

    try:
        with open(args.original_file, 'r', encoding='utf-8') as f:
            lines1 = f.read().replace('\r\n', '\n').splitlines()
        with open(args.new_file, 'r', encoding='utf-8') as f:
            lines2 = f.read().replace('\r\n', '\n').splitlines()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return
    except IOError as e:
        print(f"IO Error: {e}")
        return

    diffs = generate_diff(lines1, lines2)
    for line in diffs:
        print(line)


if __name__ == "__main__":
    main()