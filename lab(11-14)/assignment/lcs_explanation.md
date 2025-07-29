# Longest Common Subsequence (LCS) Explanation

This document explains the approach used to solve the Longest Common Subsequence (LCS) problem.

## Dynamic Programming Approach

The problem is solved using dynamic programming. We use a 2D table (a grid) to store the lengths of the longest common subsequences of the prefixes of the two input strings.

Let the two strings be `X` and `Y`.

1.  **Create a Table:** We create a table `dp` where `dp[i][j]` stores the length of the LCS of `X[0...i-1]` and `Y[0...j-1]`.

2.  **Fill the Table:** We fill the table using the following rules:
    *   If the characters `X[i-1]` and `Y[j-1]` are the same, then the LCS is one character longer than the LCS of the strings without these characters. So, `dp[i][j] = dp[i-1][j-1] + 1`.
    *   If the characters are different, we take the maximum of the LCS of the two subproblems: `dp[i-1][j]` (ignoring the last character of `X`) and `dp[i][j-1]` (ignoring the last character of `Y`). So, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

3.  **Backtracking:** Once the table is filled, the value at `dp[m][n]` (where `m` and `n` are the lengths of the strings) is the length of the LCS. To find the actual subsequence, we backtrack from `dp[m][n]`:
    *   If `X[i-1]` and `Y[j-1]` are the same, we add this character to our result and move diagonally up-left in the table.
    *   If they are different, we move in the direction of the larger value in the table (either up or left).

This process gives us the LCS in reverse order, so we reverse it at the end to get the final result.
